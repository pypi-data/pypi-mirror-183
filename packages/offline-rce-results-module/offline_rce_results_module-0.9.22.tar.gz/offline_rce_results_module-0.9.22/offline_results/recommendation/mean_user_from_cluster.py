import time

import numpy as np
from cachetools import cached, TTLCache
from pandas import DataFrame

from offline_results.common.config import (
    VISIONPLUS_DEV,
    USER_CLUSTER_DIST,
    PAY_TV_CENTROID_FEATURES,
    NO_PAY_TV_CENTROID_FEATURES,
    PAY_TV_USER_CLUSTER_FEATURE,
    NO_PAY_TV_USER_CLUSTER_FEATURE,
)
from offline_results.common.constants import (
    S3,
    GRAPH_DB,
    CUSTOMER_ID,
    MEAN_CLUSTER_DIST,
    MINIBATCH_KMEANS,
    DISTANCE_FROM_CENTROID,
    USER_DETAIL_UDKEY,
    NO_PAY_TV,
    PAY_TV,
    PAYTVPROVIDER_ID,
    DISTANCE_FROM_MEAN_USER,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.utils import class_custom_exception, custom_exception, Logging


class MeanUserFromCluster:
    def __init__(self, pay_tv_label=NO_PAY_TV):
        self.centroid_df = DataFrame()
        self.user_cluster_info = DataFrame()
        self.user_profile = DataFrame()
        self.user_df = DataFrame()
        self.pay_tv_label = pay_tv_label

    @class_custom_exception()
    def get_from_s3(
        self,
        bucket_name="",
    ):
        """
        param: bucket_name: from where we fetch the data
        param: pay_tv_label: it can be "pay_tv" or "no_pay_tv"

        """
        try:
            ctl = ConnectS3()
            resource = ctl.create_connection()
            centroid_key = (
                PAY_TV_CENTROID_FEATURES
                if self.pay_tv_label == PAY_TV
                else NO_PAY_TV_CENTROID_FEATURES
            )
            user_cluster_info_key = (
                PAY_TV_USER_CLUSTER_FEATURE
                if self.pay_tv_label == PAY_TV
                else NO_PAY_TV_USER_CLUSTER_FEATURE
            )
            self.centroid_df = ctl.read_csv_from_s3(
                bucket_name=bucket_name, object_name=centroid_key, resource=resource
            )
            self.user_cluster_info = ctl.read_csv_from_s3(
                bucket_name=bucket_name,
                object_name=user_cluster_info_key,
                resource=resource,
            )
        except Exception as e:
            Logging.error(f"Error while getting data. Error: {e}")

    @class_custom_exception()
    def get_from_graph_db(self):
        # update the code here once data is dumped into graph db
        pass

    @class_custom_exception()
    def data_gathering(
        self,
        centroid=None,
        user_cluster_info=None,
        bucket_name=None,
        source=None,
    ):
        try:
            if source == S3:
                self.get_from_s3(bucket_name)
                return

            elif source == GRAPH_DB:
                self.get_from_graph_db()
                return

            self.user_cluster_info = user_cluster_info
            self.centroid_df = centroid

        except Exception as e:
            Logging.error(f"Error while feting data. Error: {e}")

    @class_custom_exception()
    def calculate_euclidean_dist(self, centroid, data_point):
        try:
            centroid, data_point = np.array(centroid), np.array(data_point)
            differences = centroid - data_point
            squared_sums = np.dot(differences.T, differences)
            distance = np.sqrt(squared_sums)
            return abs(distance)
        except Exception as e:
            Logging.error(f"Error while calculating euclidean dist. Error: {e}")

    @staticmethod
    @custom_exception()
    def save_user_cluster_dist(pay_tv_label, user_cluster_dist):
        try:
            user_cluster_dist = user_cluster_dist[
                [
                    CUSTOMER_ID,
                    MINIBATCH_KMEANS,
                    DISTANCE_FROM_CENTROID,
                    MEAN_CLUSTER_DIST,
                ]
            ]
            object_name = (
                USER_CLUSTER_DIST.split(".")[0]
                + pay_tv_label
                + "."
                + USER_CLUSTER_DIST.split(".")[1]
            )
            ctl = ConnectS3()
            resource = ctl.create_connection()
            ctl.write_pkl_to_s3(
                bucket_name=VISIONPLUS_DEV,
                object_name=object_name,
                data=user_cluster_dist,
                resource=resource,
            )
        except Exception as e:
            Logging.error(f"Error while saving user cluster dist info. Error: {e}")

    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=60 * 10))
    @custom_exception()
    def get_all_user_cluster_dist(pay_tv_label):
        try:
            Logging.info("Start fetching 'User Cluster distance' file from s3")
            object_name = (
                USER_CLUSTER_DIST.split(".")[0]
                + pay_tv_label
                + "."
                + USER_CLUSTER_DIST.split(".")[1]
            )
            ctl = ConnectS3()
            resource = ctl.create_connection()
            df = ctl.read_pkl_from_s3(
                bucket_name=VISIONPLUS_DEV, object_name=object_name, resource=resource
            )
            df[CUSTOMER_ID] = df[CUSTOMER_ID].apply(str)
            df[MINIBATCH_KMEANS] = df[MINIBATCH_KMEANS].apply(int)

            return df
        except Exception as e:
            Logging.error(
                f"Error while reading user cluster dist info file. Error: {e}"
            )

    @class_custom_exception()
    def mean_cluster_dist(self):
        try:
            self.user_cluster_info[MEAN_CLUSTER_DIST] = 0
            for cluster_id in self.centroid_df.index:
                filtered_df = self.user_cluster_info[
                    self.user_cluster_info[MINIBATCH_KMEANS] == cluster_id
                ]
                self.user_cluster_info.loc[
                    filtered_df.index, MEAN_CLUSTER_DIST
                ] = filtered_df[DISTANCE_FROM_CENTROID].mean()
        except Exception as e:
            Logging.error(f"Error while cal mean dist. Error: {e}")

    @class_custom_exception()
    def users_distance_from_centroid(self):
        try:
            self.user_cluster_info[DISTANCE_FROM_CENTROID] = 0
            self.user_cluster_info.columns = [
                col.replace("content_", "") if "content_" in col else col
                for col in self.user_cluster_info.columns
            ]
            features = self.centroid_df.columns.difference(
                [PAYTVPROVIDER_ID, USER_DETAIL_UDKEY, MINIBATCH_KMEANS]
            )
            for cluster_id in self.centroid_df.index:
                filtered_df = self.user_cluster_info[
                    self.user_cluster_info[MINIBATCH_KMEANS] == cluster_id
                ]
                centroid = self.centroid_df.loc[cluster_id, features]
                for idx in filtered_df.index:
                    dist = self.calculate_euclidean_dist(
                        centroid, filtered_df.loc[idx, features]
                    )
                    self.user_cluster_info.at[idx, DISTANCE_FROM_CENTROID] = dist
                time.sleep(1)

        except Exception as e:
            Logging.error(f"Error while cal dist from centroid. Error: {e}")

    @staticmethod
    @custom_exception()
    def get_mean_user(cluster_id, pay_tv_label, users_dist=None):
        if users_dist is None:
            users_dist = MeanUserFromCluster.get_all_user_cluster_dist(pay_tv_label)
        cluster_users = users_dist[
            users_dist[MINIBATCH_KMEANS] == cluster_id
        ].reset_index(drop=True)
        mean_value = cluster_users.iloc[0][MEAN_CLUSTER_DIST]
        idx = np.abs(
            cluster_users[DISTANCE_FROM_CENTROID].to_numpy() - mean_value
        ).argmin()
        mean_user = cluster_users.iloc[idx][CUSTOMER_ID]
        return int(mean_user)

    @class_custom_exception()
    def update_mean_users(self):
        self.data_gathering(
            bucket_name=VISIONPLUS_DEV,
            source=S3,
        )
        self.users_distance_from_centroid()
        self.mean_cluster_dist()
        self.save_user_cluster_dist(self.pay_tv_label, self.user_cluster_info)

    @staticmethod
    @custom_exception()
    def similar_users(
        cluster_id,
        pay_tv_label,
        users_dist=None,
        no_of_similar_user=None,
        mean_user=None,
    ):

        try:
            if users_dist is None:
                users_dist = MeanUserFromCluster.get_all_user_cluster_dist(pay_tv_label)
            df = users_dist[users_dist[MINIBATCH_KMEANS] == cluster_id].copy()
            df[DISTANCE_FROM_MEAN_USER] = (
                df[MEAN_CLUSTER_DIST] - df[DISTANCE_FROM_CENTROID]
            )
            df[DISTANCE_FROM_MEAN_USER] = df[DISTANCE_FROM_MEAN_USER].apply(abs)
            df = df.sort_values([DISTANCE_FROM_MEAN_USER], ignore_index=True)
            df = df.drop_duplicates(subset=[DISTANCE_FROM_CENTROID]).reset_index(
                drop=True
            )
            mean_distance = df[DISTANCE_FROM_MEAN_USER].mean()
            df = df if no_of_similar_user is None else df[df[DISTANCE_FROM_MEAN_USER] < mean_distance]
            similar_user = df[[CUSTOMER_ID, DISTANCE_FROM_MEAN_USER]]
            return similar_user

        except Exception as e:
            Logging.error(f"Error while fetching similar user. Error: {e}")
            return DataFrame({CUSTOMER_ID: [mean_user], DISTANCE_FROM_MEAN_USER: [0]})


# #test code here calculating mean user dist
# cfl = MeanUserFromCluster("pay_tv")
# cfl.data_gathering(
#     bucket_name="visionplus-dev",
#     source=S3,
# )
# cfl.users_distance_from_centroid()
# cfl.mean_cluster_dist()
# cfl.save_user_cluster_dist()


##get mean user for cluster_id:
# cfl = MeanUserFromCluster()
# user = cfl.get_mean_user(2) # pass cluster id here
# print(user)
