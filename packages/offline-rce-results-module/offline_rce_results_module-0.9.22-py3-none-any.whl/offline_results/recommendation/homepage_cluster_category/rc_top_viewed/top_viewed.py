from graphdb import GraphDb

from offline_results.common.constants import (
    VIEW_COUNT,
    CREATED_ON,
    CONTENT_ID,
    HOMEPAGE_ID,
    SERVICE_NAME,
    TOP_VIEWED_MODULE_NAME,
    PAY_TV,
    NO_PAY_TV,
    IS_PAY_TV,
    REC_TYPE,
    CLUSTER_IS_PAY_TV,
    CUSTOMER_ID,
    CLUSTER_ID, SCORE,
)
from offline_results.recommendation.homepage_cluster_category.rc_top_viewed.top_viewed_utils import (
    TopViewedUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class TopViewed:
    graph: GraphDb

    def __init__(self):
        TopViewed.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def get_top_viewed_df(user_label, user_content, user_cluster_mapping):
        try:
            if user_label == PAY_TV:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == True]

                user_cluster_mapping = user_cluster_mapping.loc[
                    user_cluster_mapping[IS_PAY_TV] == True
                ]
                user_cluster_mapping = user_cluster_mapping[
                    user_cluster_mapping[CLUSTER_IS_PAY_TV].notna()
                ]

            else:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == False]

                user_cluster_mapping = user_cluster_mapping.loc[
                    user_cluster_mapping[IS_PAY_TV] == False
                ]
                user_cluster_mapping = user_cluster_mapping[
                    user_cluster_mapping[CLUSTER_IS_PAY_TV].notna()
                ]

            content_homepage_mapping = (
                RecommendationUtils.get_label_wise_homepage_for_contents(
                    TopViewed().graph, user_label, homepage_id_wise=True
                )
            )

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = TopViewedUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            Logging.info(f"Merging log with user-cluster mapping for {user_label}")

            cluster_homepage_mapped_user_content_df = (
                TopViewedUtils.get_inner_merged_df(
                    homepage_mapped_user_content_df,
                    user_cluster_mapping,
                    on=CUSTOMER_ID,
                )
            )

            top_viewed_df = TopViewedUtils.get_cluster_wise_top_viewed_homepages(
                cluster_homepage_mapped_user_content_df
            )

            top_viewed_df = top_viewed_df.drop_duplicates(
                subset=[CLUSTER_ID, HOMEPAGE_ID]
            ).reset_index(drop=True)

            top_viewed_df = TopViewedUtils.add_created_on_attribute(top_viewed_df)
            top_viewed_df = TopViewedUtils.add_recommendation_type_attribute(
                top_viewed_df, TOP_VIEWED_MODULE_NAME.upper()
            )

            top_viewed_df = top_viewed_df.sort_values(
                [CLUSTER_ID, SCORE], ascending=(True, False)
            ).reset_index(drop=True)

            top_viewed_df = top_viewed_df[
                [CLUSTER_ID, HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE]
            ]
            return top_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing top-viewed homepage_id rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_top_viewed_homepage_id():
        try:
            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            user_cluster_mapping = RecommendationUtils.user_cluster_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(f"PREPARING TOP-VIEWED HOMEPAGE_ID REC FOR {user_label}")
                output_df = TopViewed.get_top_viewed_df(
                    user_label, user_content_df, user_cluster_mapping
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + TOP_VIEWED_MODULE_NAME.lower()
                    + ":"
                    + user_label
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            (
                top_viewed_pay_tv_homepage_id,
                top_viewed_no_pay_tv_homepage_id,
            ) = list_output_df

            Logging.info("Preparing expected output schema")

            # Convert the dataframe output to json output format
            top_viewed_pay_tv_homepage_id_json = TopViewedUtils.get_json_format_output(
                top_viewed_pay_tv_homepage_id, list_of_key_prefix[0]
            )
            top_viewed_no_pay_tv_homepage_id_json = (
                TopViewedUtils.get_json_format_output(
                    top_viewed_no_pay_tv_homepage_id, list_of_key_prefix[1]
                )
            )
            return (
                top_viewed_pay_tv_homepage_id_json,
                top_viewed_no_pay_tv_homepage_id_json,
            )
        except Exception as e:
            Logging.error(
                f"Error while preparing top-viewed homepage_id rec, Error: {e}"
            )
