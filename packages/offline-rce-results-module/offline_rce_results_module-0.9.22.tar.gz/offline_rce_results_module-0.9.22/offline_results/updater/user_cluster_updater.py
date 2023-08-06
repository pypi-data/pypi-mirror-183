import json

from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from pandas import DataFrame, concat, get_dummies
import numpy as np
from offline_results.common.constants import PREVIOUS_CLUSTER_ID, \
    CUSTOMER_ID, PAYTVPROVIDER_ID, IS_PAYTV, PREVIOUS_TO_PREVIOUS_CLUSTER_ID, \
    CLUSTER_ID, UPDATED_ON, CLUSTER_IS_PAY_TV, IS_PAY_TV, CREATED_ON, PAY_TV, NO_PAY_TV, GENDER, GENDER_NAN, \
    MINIBATCH_KMEANS, DISTANCE_FROM_CENTROID, MEAN_CLUSTER_DIST
from offline_results.common.config import S3_RESOURCE, CLUSTER_MODEL_PATH
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.similarity.user_profile.config import CLUSTER_NODE_LABEL, \
    NEW_USER_CLUSTER_RELATIONSHIP_LABEL
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.updater.utils import UpdaterUtils
from offline_results.repository.redis_cache import Redis
from datetime import datetime

from offline_results.utils import custom_exception
from offline_results.utils.logger import Logging


class ClusterUpdater:

    @staticmethod
    @custom_exception()
    def fetch_cluster_model(
            paytv: bool,
            bucket_name=None
    ):
        """
        Fetch saved cluster model from S3
        :param paytv: Either True or False
        :param bucket_name: S3 bucket name
        """
        filename = CLUSTER_NODE_LABEL + "_" + (PAY_TV if paytv else NO_PAY_TV) + ".pkl"
        cluster_model = ConnectS3().read_pkl_from_s3(bucket_name=bucket_name,
                                                     object_name=CLUSTER_MODEL_PATH + filename,
                                                     resource=S3_RESOURCE)
        return cluster_model


    @staticmethod
    @custom_exception()
    def update_user_dist_file(
            model,
            cluster_df,
            data,
            pay_tv
    ):
        try:
            ctl = MeanUserFromCluster()
            center_df = DataFrame(model.cluster_centers_, columns=model.feature_names_in_)
            cluster_df[CUSTOMER_ID] = [str(c_id) for c_id in cluster_df[CUSTOMER_ID]]
            data.index = [str(idx) for idx in data.index]
            pay_tv_label = PAY_TV if pay_tv else NO_PAY_TV
            users_dist = ctl.get_all_user_cluster_dist(pay_tv_label)
            users_dist = users_dist.dropna()
            df = users_dist[~users_dist[CUSTOMER_ID].isin(data.index)].copy()
            temp = users_dist[users_dist[CUSTOMER_ID].isin(list(data.index))].copy()
            temp = temp.append(cluster_df[~cluster_df[CUSTOMER_ID].isin(temp[CUSTOMER_ID])], ignore_index=True)
            if len(temp) == 0: temp[CUSTOMER_ID] = data.index
            for idx in temp.index:
                user = temp.loc[idx, CUSTOMER_ID]
                cluster_id = list(cluster_df[cluster_df[CUSTOMER_ID] == user][CLUSTER_NODE_LABEL])[0]
                temp.at[idx, MINIBATCH_KMEANS] = cluster_id
                centroid_feature = DataFrame(center_df.loc[cluster_id, :].copy()).T
                user_pref = DataFrame(data.loc[user, :]).T
                centroid_feature = concat([centroid_feature, user_pref]).fillna(0).reset_index(drop=True)
                centroid_feature = centroid_feature[center_df.columns]
                user_pref, centroid_feature = centroid_feature.loc[1, :], centroid_feature.loc[0, :]
                distance = RecommendationUtils.calculate_euclidean_dist(user_pref, centroid_feature)
                temp.at[idx, DISTANCE_FROM_CENTROID] = distance
            df = concat([df, temp], ignore_index=True)
            for cluster_id in set(cluster_df[MINIBATCH_KMEANS]):
                mean_dist = df[df[MINIBATCH_KMEANS] == cluster_id][DISTANCE_FROM_CENTROID].mean()
                df.loc[df[MINIBATCH_KMEANS] == cluster_id, MEAN_CLUSTER_DIST] = mean_dist
            MeanUserFromCluster.save_user_cluster_dist(pay_tv_label, df)
        except Exception as e:
            Logging.error(f"Error while updating user distance file. Exception: {e}")

    @staticmethod
    @custom_exception()
    def prepare_clustering_features(
            data: DataFrame,
            pay_tv: bool,
            bucket_name=None
    ) -> DataFrame:
        """
        Prepare data according to expected input in cluster model
        :param data: Dataframe object pandas
        :param pay_tv: Either True or False
        :param bucket_name: S3 bucket name
        :return: Dataframe object pandas
        """
        cluster_data = DataFrame()
        if pay_tv:
            data = data[~data[PAYTVPROVIDER_ID].isna()].reset_index(drop=True)
        else:
            data = data[data[PAYTVPROVIDER_ID].isna()].reset_index(drop=True)
        data = data.drop(columns=[IS_PAY_TV])
        if not data.empty:
            cluster_data[CUSTOMER_ID] = data[CUSTOMER_ID]
            data[PAYTVPROVIDER_ID] = data[PAYTVPROVIDER_ID].fillna(-1)
            data[PAYTVPROVIDER_ID] = data[PAYTVPROVIDER_ID].astype(int)
            data = data.set_index(CUSTOMER_ID)
            data = get_dummies(data, columns=[GENDER, PAYTVPROVIDER_ID])
            if GENDER_NAN in data.columns:
                data = data.drop(columns=[GENDER_NAN])
            cluster_model = ClusterUpdater.fetch_cluster_model(paytv=pay_tv, bucket_name=bucket_name)
            cluster_feature = cluster_model.feature_names_in_
            cols = data.columns.tolist()
            cols_to_add = np.setdiff1d(cluster_feature, cols)
            cols_to_drop = np.setdiff1d(cols, cluster_feature).tolist()
            # Only considering features that are available in cluster_features
            data = data.drop(columns=cols_to_drop)
            data = data.assign(**dict.fromkeys(cols_to_add, 0))
            data = data.reindex(columns=cluster_feature)
            # Predict and assign new cluster ids
            cluster_data[CLUSTER_NODE_LABEL] = cluster_model.predict(data)
            ClusterUpdater.update_user_dist_file(cluster_model, cluster_data, data, pay_tv)

        return cluster_data.reset_index(drop=True)

    @staticmethod
    @custom_exception()
    def assign_cluster_id(
            data: DataFrame,
            bucket_name=None
    ) -> DataFrame:
        """
        Function to call other methods to assign new
        cluster_id's to the users.
        :param data: Dataframe object pandas
        :param bucket_name: S3 bucket name
        :return: Dataframe object pandas
        """
        paytv_clusters = ClusterUpdater.prepare_clustering_features(data=data, pay_tv=True, bucket_name=bucket_name)
        if not paytv_clusters.empty:
            paytv_clusters[IS_PAYTV] = "True"
        no_paytv_clusters = ClusterUpdater.prepare_clustering_features(data=data, pay_tv=False, bucket_name=bucket_name)
        if not no_paytv_clusters.empty:
            no_paytv_clusters[IS_PAYTV] = "False"
        new_user_cluster = concat([paytv_clusters, no_paytv_clusters], ignore_index=True)
        return new_user_cluster

    @staticmethod
    @custom_exception()
    def save_cluster_relation_s3(
            new_cluster_data: DataFrame,
            existing_cluster_data: DataFrame,
            bucket_name=None,
            object_name=None
    ) -> DataFrame:
        """
        Function to save updated user-cluster relations on S3
        :param new_cluster_data: user-cluster relation dataframe
        :param existing_cluster_data: user-cluster relation dataframe
        :param bucket_name: s3 bucket name
        :param object_name: s3 file path
        :return: Dataframe object pandas
        """
        new_cluster_data = new_cluster_data.rename(columns={CLUSTER_NODE_LABEL: CLUSTER_ID,
                                                            IS_PAYTV: CLUSTER_IS_PAY_TV})
        new_cluster_data[CUSTOMER_ID] = new_cluster_data[CUSTOMER_ID].astype(str)
        new_cluster_data[CLUSTER_ID] = new_cluster_data[CLUSTER_ID].astype(int)
        new_cluster_data[IS_PAY_TV] = new_cluster_data[CLUSTER_IS_PAY_TV]
        new_cluster_data[IS_PAY_TV] = new_cluster_data[IS_PAY_TV].replace(["nan"], False)
        new_cluster_data[UPDATED_ON] = datetime.utcnow().isoformat()
        list_users = new_cluster_data[CUSTOMER_ID].tolist()
        new_cluster_data = new_cluster_data.set_index(CUSTOMER_ID)
        existing_cluster_data = existing_cluster_data.set_index(CUSTOMER_ID)
        existing_cluster_data.loc[list_users, PREVIOUS_TO_PREVIOUS_CLUSTER_ID] = \
            existing_cluster_data[PREVIOUS_CLUSTER_ID]
        existing_cluster_data.loc[list_users, PREVIOUS_CLUSTER_ID] = \
            existing_cluster_data[CLUSTER_ID]
        existing_cluster_data.update(new_cluster_data)
        existing_cluster_data[CLUSTER_ID] = existing_cluster_data[CLUSTER_ID].astype(int)
        existing_cluster_data = existing_cluster_data.reset_index().rename(columns={'index': CUSTOMER_ID})
        new_cluster_data = new_cluster_data.reset_index().rename(columns={'index': CUSTOMER_ID})
        print("Saving updated user-cluster relations to S3...")
        mapper = {"nan": np.nan, "False": False, "True": True}
        existing_cluster_data[IS_PAY_TV] = existing_cluster_data[IS_PAY_TV].replace(mapper)
        existing_cluster_data[CLUSTER_IS_PAY_TV] = existing_cluster_data[CLUSTER_IS_PAY_TV].replace(mapper)
        ConnectS3().write_df_to_pkl_S3(
            bucket_name=bucket_name, object_name=object_name, data=existing_cluster_data, resource=S3_RESOURCE
        )
        existing_cluster_data = existing_cluster_data[
            existing_cluster_data[CUSTOMER_ID].isin(new_cluster_data[CUSTOMER_ID])
        ]
        existing_cluster_data = existing_cluster_data.reset_index(drop=True)
        return existing_cluster_data

    @staticmethod
    @custom_exception()
    def update_redis_cache(data: DataFrame, redis_uri):
        """
        Function to update user-cluster relations in
        redis cache
        :param data: Dataframe object pandas
        :param redis_uri: redis uri
        """
        data_dict = data.to_dict(orient='records')
        cls = Redis.from_uri(redis_uri)
        for record in data_dict:
            try:
                key = "user_information:{}".format(record[CUSTOMER_ID])
                record.pop(CUSTOMER_ID, None)
                resp = cls.get_data(key)
                if resp is not None:
                    resp_dict = json.loads(resp)
                    resp_dict[CLUSTER_ID] = record[CLUSTER_ID]
                    resp_dict[IS_PAY_TV] = record[IS_PAY_TV]
                    resp_dict[CLUSTER_IS_PAY_TV] = record[CLUSTER_IS_PAY_TV]
                    resp_dict[PREVIOUS_CLUSTER_ID] = record[PREVIOUS_CLUSTER_ID]
                    resp_dict[PREVIOUS_TO_PREVIOUS_CLUSTER_ID] = record[PREVIOUS_TO_PREVIOUS_CLUSTER_ID]
                    resp_dict[CREATED_ON] = record[CREATED_ON]
                    resp_dict[UPDATED_ON] = record[UPDATED_ON]
                    cls.set(key, json.dumps(resp_dict))
            except Exception as e:
                Logging.error(f"Error while updating redis cache for {key}, Error:{e}")
        return True

    @staticmethod
    @custom_exception()
    def controller(
            data,
            bucket_name=None,
            object_name=None,
            redis_uri=None
    ):
        """
        Controller function for Cluster Updater network
        :param data: raw preferences dataframe
        :param bucket_name: S3 bucket name
        :param object_name: S3 object name
        :param redis_uri: redis uri
        """
        user_info = UpdaterUtils.fetch_user_in_graph(data[CUSTOMER_ID].tolist())
        data = UpdaterUtils.find_paytv_users(data)
        data = data.merge(user_info, on=CUSTOMER_ID, how='inner')
        new_user_clusters = ClusterUpdater.assign_cluster_id(data=data, bucket_name=bucket_name)
        existing_clusters = UpdaterUtils.fetch_existing_cluster(bucket_name=bucket_name,
                                                                object_name=object_name)
        existing_clusters[CUSTOMER_ID] = existing_clusters[CUSTOMER_ID].astype(str)
        updated_cluster_data = ClusterUpdater.save_cluster_relation_s3(new_cluster_data=new_user_clusters,
                                                                       existing_cluster_data=existing_clusters,
                                                                       bucket_name=bucket_name,
                                                                       object_name=object_name)
        ClusterUpdater.update_redis_cache(updated_cluster_data, redis_uri)
        UpdaterUtils.drop_existing_rel(data=new_user_clusters, relation_label=NEW_USER_CLUSTER_RELATIONSHIP_LABEL)
        UpdaterUtils.dump_cluster_relations(dump_data=new_user_clusters,
                                            destination_label=CLUSTER_NODE_LABEL,
                                            relation_label=NEW_USER_CLUSTER_RELATIONSHIP_LABEL,
                                            df_attribute=CLUSTER_NODE_LABEL)
