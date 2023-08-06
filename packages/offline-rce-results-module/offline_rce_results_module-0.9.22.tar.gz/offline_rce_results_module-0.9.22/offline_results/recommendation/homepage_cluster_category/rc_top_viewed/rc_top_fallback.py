from graphdb import GraphDb

from offline_results.common.constants import (
    PAY_TV,
    HOMEPAGE_ID,
    CONTENT_ID,
    VIEW_COUNT,
    CREATED_ON,
    SERVICE_NAME,
    DEFAULT_TOP_VIEWED_MODULE_NAME,
    NO_PAY_TV,
    REC_TYPE,
    IS_PAY_TV, SCORE,
)
from offline_results.recommendation.homepage_cluster_category.rc_top_viewed.top_viewed_utils import TopViewedUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class TVFallback:
    graph: GraphDb

    def __init__(self):
        TVFallback.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def generate_rec(user_label, user_content):
        try:
            if user_label == PAY_TV:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == True]

            else:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == False]

            content_homepage_mapping = (
                RecommendationUtils.get_label_wise_homepage_for_contents(
                    TVFallback().graph, user_label, homepage_id_wise=True
                )
            )

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = TopViewedUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            top_viewed_df = TopViewedUtils.get_default_top_viewed_homepages(
                homepage_mapped_user_content_df
            )

            top_viewed_df = top_viewed_df.drop_duplicates(
                subset=[HOMEPAGE_ID]
            ).reset_index(drop=True)

            top_viewed_df = TopViewedUtils.add_created_on_attribute(top_viewed_df)
            top_viewed_df = TopViewedUtils.add_recommendation_type_attribute(
                top_viewed_df, DEFAULT_TOP_VIEWED_MODULE_NAME.upper()
            )

            top_viewed_df = top_viewed_df.sort_values(
                [VIEW_COUNT], ascending=False
            ).reset_index(drop=True)

            top_viewed_df = top_viewed_df[
                [HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE]
            ]
            return top_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK top-viewed homepage_id rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def fallback_rc_top_viewed_data():
        try:
            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(f"PREPARING FALLBACK TOP-VIEWED HOMEPAGE_ID REC FOR {user_label}")
                output_df = TVFallback.generate_rec(
                    user_label, user_content_df
                )
                key_prefix = (
                        SERVICE_NAME
                        + ":"
                        + DEFAULT_TOP_VIEWED_MODULE_NAME.lower()
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
            top_viewed_pay_tv_homepage_id_json = TopViewedUtils.get_default_json_format_output(
                top_viewed_pay_tv_homepage_id, list_of_key_prefix[0]
            )
            top_viewed_no_pay_tv_homepage_id_json = (
                TopViewedUtils.get_default_json_format_output(
                    top_viewed_no_pay_tv_homepage_id, list_of_key_prefix[1]
                )
            )
            return (
                top_viewed_pay_tv_homepage_id_json,
                top_viewed_no_pay_tv_homepage_id_json,
            )
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK top-viewed homepage_id rec, Error: {e}"
            )
