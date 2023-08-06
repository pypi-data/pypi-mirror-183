from datetime import datetime
from itertools import chain

from pandas import DataFrame, merge

from offline_results.common.config import (
    MAXIMUM_NUMBER_OF_RECOMMENDATIONS,
)
from offline_results.common.constants import (
    CUSTOMER_ID,
    CONTENT_ID,
    VIEW_COUNT,
    NO_PAY_TV_CONTENT,
    PAY_TV_CONTENT,
    LEFT,
    HOMEPAGE_ID,
    RECOMMENDED_CONTENT_ID,
    CLUSTER_ID,
    CREATED_ON,
    SCORE,
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    RECORDS,
    HOMEPAGE_ID_BASED,
    PAY_TV,
    ITEM_TO_ITEM_MODULE_NAME,
    STATUS,
    CONTENT_STATUS,
    ACTIVE,
    IS_PAY_TV,
    MEAN_USER,
    SUM,
    REC_TYPE,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.similarity.content_profile.similarity_all_contents import (
    SimilarityAllContents,
)
from offline_results.similarity.content_profile.similarity_homepage_contents import (
    SimilarityHomepageContents,
)
from offline_results.utils import custom_exception, Logging


class ItemToItemUtils:
    @staticmethod
    @custom_exception()
    def read_join_viewed_from_s3() -> DataFrame:
        return RecommendationUtils.user_viewed_data_from_s3()

    @staticmethod
    @custom_exception()
    def read_join_kmeans_from_s3() -> DataFrame:
        return RecommendationUtils.user_cluster_from_s3()

    @staticmethod
    @custom_exception()
    def user_cluster_mapping_with_user_log() -> DataFrame:
        Logging.info("Merging viewed data with user-cluster mapping")
        merged_df = ItemToItemUtils.merge_on_customer_id(
            ItemToItemUtils.read_join_viewed_from_s3(),
            ItemToItemUtils.read_join_kmeans_from_s3(),
        )
        return merged_df

    @staticmethod
    @custom_exception()
    def queried_network_response_to_dataframe(response) -> DataFrame:
        return DataFrame(list(chain.from_iterable(response)))

    @staticmethod
    @custom_exception()
    def homepage_data(pay_tv_label, features=[CONTENT_ID, HOMEPAGE_ID]):
        feature_str = ""
        for feature in features:
            feature_str += "values('" + feature + "'),"
        query = f"""
            g.V().hasLabel('{pay_tv_label}','{STATUS}','Active').
            outE('HAS_HOMEPAGE').
            project('HAS_HOMEPAGE', '{CONTENT_ID}', 'homepage_id').
            by(label).
            by(outV().values('{CONTENT_ID}')).
            by(inV().union(
            {feature_str[:-1]}).fold())
            """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data)
        return df

    @staticmethod
    @custom_exception()
    def get_active_paytv_and_no_paytv_user_log(user_log):
        Logging.info("Getting active paytv & no_paytv user log")
        paytv_user_log = user_log[
            (user_log[CONTENT_STATUS] == ACTIVE) & (user_log[IS_PAY_TV] == True)
        ]
        no_paytv_user_log = user_log[
            (user_log[CONTENT_STATUS] == ACTIVE) & (user_log[IS_PAY_TV] == False)
        ]
        return paytv_user_log, no_paytv_user_log

    @staticmethod
    @custom_exception()
    def similarity_dict_of_dict_to_dataframe(similarity_response) -> DataFrame:
        df = DataFrame([similarity_response]).T
        df[CONTENT_ID] = df.index
        temp_df = (
            DataFrame([*df[0]], df.index)
            .stack()
            .rename_axis([None, RECOMMENDED_CONTENT_ID])
            .reset_index(1, name=SCORE)
        )
        recommendation_df = df[[CONTENT_ID]].join(temp_df).iloc[:, :10]
        return recommendation_df

    @staticmethod
    @custom_exception()
    def get_similar_contents_based_on_all(content_label):
        paytv_df = ItemToItemUtils.similarity_dict_of_dict_to_dataframe(
            SimilarityAllContents.prepare_similarity_based_on_all_content(content_label)
        )
        return paytv_df

    @staticmethod
    @custom_exception()
    def find_maximum_view_count(data) -> DataFrame:
        return data.sort_values(VIEW_COUNT, ascending=False)

    @staticmethod
    @custom_exception()
    def merge_on_content_id(dataframe1, dataframe2) -> DataFrame:
        return merge(dataframe1, dataframe2, on=[CONTENT_ID], how=LEFT)

    @staticmethod
    @custom_exception()
    def merge_on_customer_id(dataframe1, dataframe2) -> DataFrame:
        return merge(dataframe1, dataframe2, on=[CUSTOMER_ID], how=LEFT)

    @staticmethod
    @custom_exception()
    def add_created_on_attribute(dataframe) -> DataFrame:
        dataframe[CREATED_ON] = datetime.utcnow().isoformat()
        return dataframe

    @staticmethod
    @custom_exception()
    def get_mean_user_df(dataframe, pay_tv_label) -> DataFrame:
        unique_cluster_id_list = sorted(dataframe[CLUSTER_ID].unique())
        mean_user_array = []
        user_cluster_dist = MeanUserFromCluster.get_all_user_cluster_dist(pay_tv_label)
        for cluster_id in unique_cluster_id_list:
            mean_user_dict = {}
            mean_user = MeanUserFromCluster.get_mean_user(
                cluster_id=cluster_id,
                pay_tv_label=pay_tv_label,
                users_dist=user_cluster_dist,
            )
            mean_user_dict[CLUSTER_ID] = cluster_id
            mean_user_dict[MEAN_USER] = mean_user
            mean_user_array.append(mean_user_dict)

        mean_user_df = DataFrame(mean_user_array, columns=[CLUSTER_ID, MEAN_USER])
        final_df = merge(dataframe, mean_user_df, on=[CLUSTER_ID], how=LEFT)
        return final_df

    @staticmethod
    @custom_exception()
    def cf_ii_all_content_based_rec(dataframe, similarity_df, pay_tv_label):

        try:
            dataframe = dataframe[[VIEW_COUNT, CONTENT_ID, CLUSTER_ID]].sort_values(
                by=CLUSTER_ID, ascending=True
            )
            unique_cluster_id_list = sorted(dataframe[CLUSTER_ID].unique())
            all_content_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + ITEM_TO_ITEM_MODULE_NAME
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            for cluster_id in unique_cluster_id_list:
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                cluster_df = dataframe[dataframe[CLUSTER_ID] == cluster_id]
                highest_view_df = (
                    cluster_df.groupby(CONTENT_ID, as_index=False)[VIEW_COUNT]
                    .agg(SUM)
                    .sort_values(by=VIEW_COUNT, ascending=False)
                    .iloc[:1, :]
                )
                result_df = ItemToItemUtils.merge_on_content_id(
                    highest_view_df, similarity_df
                )
                result_df = (
                    result_df.sort_values(by=SCORE, ascending=False)
                    .head(MAXIMUM_NUMBER_OF_RECOMMENDATIONS)
                    .drop(columns=[CONTENT_ID, VIEW_COUNT])
                    .rename(columns={RECOMMENDED_CONTENT_ID: CONTENT_ID})
                )
                result_df[CREATED_ON] = datetime.utcnow().isoformat()
                result_df[REC_TYPE] = ITEM_TO_ITEM_MODULE_NAME
                all_content_based_rec[key_prefix_cls] = result_df.to_dict(RECORDS)
            return all_content_based_rec

        except Exception as e:
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def cf_ii_homepage_based_rec(dataframe, homepage_id, paytv_label):
        try:
            content_label = (
                PAY_TV_CONTENT if paytv_label == PAY_TV else NO_PAY_TV_CONTENT
            )
            similarity_df = (
                SimilarityHomepageContents.prepare_similarity_based_on_homepage_id(
                    content_label, int(homepage_id)
                )
            )
            homepage_based_rec = {}
            if len(similarity_df) > 0:
                similarity_merged_df = merge(
                    similarity_df, dataframe, on=[HOMEPAGE_ID, CONTENT_ID], how=LEFT
                )
                unique_cluster_id_list = sorted(
                    similarity_merged_df[CLUSTER_ID].dropna().unique()
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + ITEM_TO_ITEM_MODULE_NAME
                    + ":"
                    + paytv_label
                    + ":"
                    + HOMEPAGE_ID_BASED
                )
                for cluster_id in unique_cluster_id_list:
                    cluster_df = similarity_merged_df[
                        similarity_merged_df[CLUSTER_ID] == cluster_id
                    ]
                    key_prefix_cls = (
                        key_prefix
                        + ":"
                        + str(int(cluster_id))
                        + ":"
                        + str(int(homepage_id))
                    )
                    mean_user = MeanUserFromCluster.get_mean_user(
                        cluster_id=int(cluster_id), pay_tv_label=paytv_label
                    )
                    mean_user_df = cluster_df[cluster_df[CUSTOMER_ID] == mean_user]

                    if len(mean_user_df) > 0:
                        recommendation_df = mean_user_df[
                            [RECOMMENDED_CONTENT_ID, SCORE]
                        ].rename(columns={RECOMMENDED_CONTENT_ID: CONTENT_ID})
                        recommendation_df[CLUSTER_ID] = int(cluster_id)
                        recommendation_df[HOMEPAGE_ID] = int(homepage_id)
                        recommendation_df[CREATED_ON] = datetime.utcnow().isoformat()
                        result = recommendation_df.to_json(orient=RECORDS)[1:-1]
                        homepage_based_rec[key_prefix_cls] = result

                    else:
                        recommendation_df = cluster_df[
                            [
                                CUSTOMER_ID,
                                CONTENT_ID,
                                RECOMMENDED_CONTENT_ID,
                                VIEW_COUNT,
                                SCORE,
                            ]
                        ]
                        recommendation_df = recommendation_df[
                            recommendation_df[VIEW_COUNT]
                            == recommendation_df[VIEW_COUNT].max()
                        ].sort_values(by=[SCORE], ascending=False)
                        recommendation_df = recommendation_df[
                            [RECOMMENDED_CONTENT_ID, SCORE]
                        ].rename(columns={RECOMMENDED_CONTENT_ID: CONTENT_ID})
                        recommendation_df[CLUSTER_ID] = int(cluster_id)
                        recommendation_df[HOMEPAGE_ID] = int(homepage_id)
                        recommendation_df[CREATED_ON] = datetime.utcnow().isoformat()
                        homepage_based_rec[key_prefix_cls] = recommendation_df.to_dict(
                            RECORDS
                        )

            return homepage_based_rec

        except Exception as e:
            Logging.error(
                f"Error while preparing homepage based rec for {paytv_label}, Error: {e}"
            )
            homepage_based_rec = {}

            return homepage_based_rec
