from graphdb import GraphDb

from offline_results.common.constants import (
    CREATED_ON,
    CUSTOMER_ID,
    CONTENT_ID,
    HOMEPAGE_ID,
    CLUSTER_ID,
    SERVICE_NAME,
    PAY_TV,
    NO_PAY_TV,
    IS_PAY_TV,
    HOMEPAGE_RECENCY_MODULE_NAME,
    REC_TYPE,
    CLUSTER_IS_PAY_TV, SCORE,
)
from offline_results.recommendation.homepage_cluster_category.rc_recency.recency_utils import (
    RecencyUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class Recency:
    graph: GraphDb

    def __init__(self):
        Recency.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def get_recent_df(user_label, user_content_df, user_cluster_mapping):
        try:
            if user_label == PAY_TV:
                user_content_df = user_content_df.loc[
                    user_content_df[IS_PAY_TV] == True
                ]

                user_cluster_mapping = user_cluster_mapping.loc[
                    user_cluster_mapping[IS_PAY_TV] == True
                ]
                user_cluster_mapping = user_cluster_mapping[
                    user_cluster_mapping[CLUSTER_IS_PAY_TV].notna()
                ]

            else:
                user_content_df = user_content_df.loc[
                    user_content_df[IS_PAY_TV] == False
                ]

                user_cluster_mapping = user_cluster_mapping.loc[
                    user_cluster_mapping[IS_PAY_TV] == False
                ]
                user_cluster_mapping = user_cluster_mapping[
                    user_cluster_mapping[CLUSTER_IS_PAY_TV].notna()
                ]

            active_static_homepage_data = (
                RecommendationUtils.get_active_homepage_ids_having_active_content(
                    Recency().graph, user_label
                )
            )

            content_homepage_mapping = RecommendationUtils.content_having_homepage(
                is_paytv=True if user_label == PAY_TV else False
            )

            Logging.info(f"Merging log with user-cluster mapping for {user_label}")

            cluster_mapped_user_content_df = RecencyUtils.get_inner_merged_df(
                user_content_df, user_cluster_mapping, on=CUSTOMER_ID
            )

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_cluster_mapped_user_content_df = RecencyUtils.get_inner_merged_df(
                cluster_mapped_user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            cluster_wise_homepage_id_not_in_ubd = (
                RecencyUtils.get_cluster_wise_homepage_id_not_in_ubd(
                    active_static_homepage_data, homepage_cluster_mapped_user_content_df
                )
            )

            recent_df = cluster_wise_homepage_id_not_in_ubd.sort_values\
                (by=[CLUSTER_ID, CREATED_ON], ascending=(True, False))\
                .reset_index(drop=True)
            recent_df = recent_df[[CLUSTER_ID, HOMEPAGE_ID, SCORE]]

            recent_df = RecencyUtils.add_created_on_attribute(recent_df)
            recent_df = RecencyUtils.add_recommendation_type_attribute(
                recent_df, HOMEPAGE_RECENCY_MODULE_NAME.upper()
            )

            recent_df = (
                recent_df[[CLUSTER_ID, HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE]]
                .drop_duplicates(subset=[CLUSTER_ID, HOMEPAGE_ID])
                .reset_index(drop=True)
            )
            return recent_df
        except Exception as e:
            Logging.error(
                f"Error while preparing recency-based homepage_id rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_recent_homepage_id():
        try:
            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            user_cluster_mapping = RecommendationUtils.user_cluster_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(
                    f"PREPARING RECENCY-BASED HOMEPAGE_ID REC FOR {user_label}"
                )
                output_df = Recency.get_recent_df(
                    user_label, user_content_df, user_cluster_mapping
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + HOMEPAGE_RECENCY_MODULE_NAME.lower()
                    + ":"
                    + user_label
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            recent_pay_tv_homepage_id, recent_no_pay_tv_homepage_id = list_output_df

            Logging.info("Preparing expected output schema")

            # Convert the dataframe output to json output format
            recent_pay_tv_homepage_id_json = RecencyUtils.get_json_format_output(
                recent_pay_tv_homepage_id, list_of_key_prefix[0]
            )
            recent_no_pay_tv_homepage_id_json = RecencyUtils.get_json_format_output(
                recent_no_pay_tv_homepage_id, list_of_key_prefix[1]
            )
            return recent_pay_tv_homepage_id_json, recent_no_pay_tv_homepage_id_json
        except Exception as e:
            Logging.error(
                f"Error while preparing recency-based homepage_id rec, Error: {e}"
            )
