from graphdb import GraphDb

from offline_results.common.constants import (
    CREATED_ON,
    CONTENT_ID,
    HOMEPAGE_ID,
    IS_PAY_TV,
    PAY_TV,
    NO_PAY_TV,
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    HOMEPAGE_ID_BASED,
    VIEW_COUNT,
    FALLBACK_LEAST_VIEWED_MODULE_NAME,
    REC_TYPE, SCORE,
)
from offline_results.recommendation.homepage_recommendation.core.with_least_viewed.lv_utils import (
    LVUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class LVFallback:
    graph: GraphDb

    def __init__(self):
        LVFallback.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def get_fallback_all_contents_based_df(user_label, homepage_id_wise, user_content):
        try:
            if user_label == PAY_TV:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == True]
            else:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == False]

            content_homepage_mapping = (
                RecommendationUtils.get_label_wise_homepage_for_contents(
                    LVFallback().graph, user_label, homepage_id_wise
                )
            )

            content_homepage_mapping = content_homepage_mapping[
                ~content_homepage_mapping[CONTENT_ID].isin(
                    RecommendationUtils.get_tv_channels(is_pay_tv=True if user_label == PAY_TV else False)
                )
            ].reset_index(drop=True)

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = LVUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            least_viewed_df = LVUtils.get_default_least_viewed_contents(
                homepage_mapped_user_content_df
            )

            least_viewed_df = least_viewed_df.drop_duplicates(
                subset=[CONTENT_ID]
            ).reset_index(drop=True)

            least_viewed_df = LVUtils.add_created_on_attribute(least_viewed_df)
            least_viewed_df = LVUtils.add_recommendation_type_attribute(
                least_viewed_df, FALLBACK_LEAST_VIEWED_MODULE_NAME.upper()
            )

            least_viewed_df = least_viewed_df.sort_values(
                [SCORE], ascending=False
            ).reset_index(drop=True)
            least_viewed_df = least_viewed_df[
                [CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
            ].reset_index(drop=True)
            return least_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK least viewed rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_fallback_homepage_id_wise_df(user_label, homepage_id_wise, user_content):
        try:
            if user_label == PAY_TV:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == True]
            else:
                user_content_df = user_content.loc[user_content[IS_PAY_TV] == False]

            content_homepage_mapping = (
                RecommendationUtils.get_label_wise_homepage_for_contents(
                    LVFallback().graph, user_label, homepage_id_wise
                )
            )

            reserved_homepage_ids = RecommendationUtils.reserved_homepage_id(
                is_pay_tv=True if user_label == PAY_TV else False
            )

            content_homepage_mapping = content_homepage_mapping[
                ~content_homepage_mapping[HOMEPAGE_ID].isin(reserved_homepage_ids)
            ].reset_index(drop=True)

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = LVUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            least_viewed_df = LVUtils.get_default_homepage_wise_least_viewed_contents(
                homepage_mapped_user_content_df
            )

            least_viewed_df = least_viewed_df.drop_duplicates(
                subset=[HOMEPAGE_ID, CONTENT_ID]
            ).reset_index(drop=True)

            least_viewed_df = LVUtils.add_created_on_attribute(least_viewed_df)
            least_viewed_df = LVUtils.add_recommendation_type_attribute(
                least_viewed_df, FALLBACK_LEAST_VIEWED_MODULE_NAME.upper()
            )

            least_viewed_df = least_viewed_df.sort_values(
                [HOMEPAGE_ID, SCORE], ascending=(True, False)
            ).reset_index(drop=True)
            least_viewed_df = least_viewed_df[
                [HOMEPAGE_ID, CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
            ].reset_index(drop=True)
            return least_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK least viewed rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_fallback_least_viewed_all_contents():
        try:
            homepage_id_wise = False

            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(
                    f"PREPARING FALLBACK least VIEWED REC BASED ON ALL CONTENTS FOR {user_label}"
                )
                output_df = LVFallback.get_fallback_all_contents_based_df(
                    user_label, homepage_id_wise, user_content_df
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + FALLBACK_LEAST_VIEWED_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            (
                least_viewed_pay_tv_all_content,
                least_viewed_no_pay_tv_all_content,
            ) = list_output_df

            Logging.info("Preparing FALLBACK expected output schema")

            # Convert the dataframe output to json output format
            least_viewed_pay_tv_all_content_json = (
                LVUtils.get_default_json_format_output(
                    least_viewed_pay_tv_all_content,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )
            least_viewed_no_pay_tv_all_content_json = (
                LVUtils.get_default_json_format_output(
                    least_viewed_no_pay_tv_all_content,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )
            return (
                least_viewed_pay_tv_all_content_json,
                least_viewed_no_pay_tv_all_content_json,
            )
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK all_content_based rec, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_fallback_least_viewed_homepage_id():
        try:
            homepage_id_wise = True

            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(
                    f"PREPARING FALLBACK least VIEWED REC BASED ON HOMEPAGE_ID FOR {user_label}"
                )
                output_df = LVFallback.get_fallback_homepage_id_wise_df(
                    user_label, homepage_id_wise, user_content_df
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + FALLBACK_LEAST_VIEWED_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            (
                least_viewed_pay_tv_homepage_id,
                least_viewed_no_pay_tv_homepage_id,
            ) = list_output_df

            Logging.info("Preparing FALLBACK expected output schema")

            # Convert the dataframe output to json output format
            least_viewed_pay_tv_homepage_id_json = (
                LVUtils.get_default_json_format_output(
                    least_viewed_pay_tv_homepage_id,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )
            least_viewed_no_pay_tv_homepage_id_json = (
                LVUtils.get_default_json_format_output(
                    least_viewed_no_pay_tv_homepage_id,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )
            return (
                least_viewed_pay_tv_homepage_id_json,
                least_viewed_no_pay_tv_homepage_id_json,
            )
        except Exception as e:
            Logging.error(
                f"Error while preparing FALLBACK homepage_id_based rec, Error: {e}"
            )
