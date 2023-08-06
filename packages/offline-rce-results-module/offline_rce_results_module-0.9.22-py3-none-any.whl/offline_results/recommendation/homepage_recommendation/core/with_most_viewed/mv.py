from graphdb import GraphDb

from offline_results.common.constants import (
    CREATED_ON,
    CUSTOMER_ID,
    CONTENT_ID,
    HOMEPAGE_ID,
    IS_PAY_TV,
    CLUSTER_ID,
    PAY_TV,
    NO_PAY_TV,
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    MOST_VIEWED_MODULE_NAME,
    HOMEPAGE_ID_BASED,
    REC_TYPE,
    CLUSTER_IS_PAY_TV, SCORE,
)
from offline_results.recommendation.homepage_recommendation.core.with_most_viewed.mv_utils import (
    MVUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class MV:
    graph: GraphDb

    def __init__(self):
        MV.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def get_all_contents_based_df(
        user_label, homepage_id_wise, user_content, user_cluster_mapping
    ):
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
                    MV().graph, user_label, homepage_id_wise
                )
            )

            content_homepage_mapping = content_homepage_mapping[
                ~content_homepage_mapping[CONTENT_ID].isin(
                    RecommendationUtils.get_tv_channels(is_pay_tv=True if user_label == PAY_TV else False)
                )
            ].reset_index(drop=True)

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = MVUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            Logging.info(f"Merging log with user-cluster mapping for {user_label}")

            cluster_homepage_mapped_user_content_df = MVUtils.get_inner_merged_df(
                homepage_mapped_user_content_df, user_cluster_mapping, on=CUSTOMER_ID
            )

            most_viewed_df = MVUtils.get_cluster_wise_most_viewed_contents(
                cluster_homepage_mapped_user_content_df
            )

            most_viewed_df = most_viewed_df.drop_duplicates(
                subset=[CLUSTER_ID, CONTENT_ID]
            ).reset_index(drop=True)

            most_viewed_df = MVUtils.add_created_on_attribute(most_viewed_df)
            most_viewed_df = MVUtils.add_recommendation_type_attribute(
                most_viewed_df, MOST_VIEWED_MODULE_NAME.upper()
            )

            most_viewed_df = most_viewed_df.sort_values(
                [CLUSTER_ID, SCORE], ascending=(True, False)
            ).reset_index(drop=True)
            most_viewed_df = most_viewed_df[
                [CLUSTER_ID, CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
            ].reset_index(drop=True)
            return most_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing most viewed rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_homepage_id_wise_df(
        user_label, homepage_id_wise, user_content, user_cluster_mapping
    ):
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
                    MV().graph, user_label, homepage_id_wise
                )
            )

            reserved_homepage_ids = RecommendationUtils.reserved_homepage_id(
                is_pay_tv=True if user_label == PAY_TV else False
            )

            content_homepage_mapping = content_homepage_mapping[
                ~content_homepage_mapping[HOMEPAGE_ID].isin(reserved_homepage_ids)
            ].reset_index(drop=True)

            Logging.info(f"Merging log with content-homepage mapping for {user_label}")

            homepage_mapped_user_content_df = MVUtils.get_inner_merged_df(
                user_content_df, content_homepage_mapping, on=CONTENT_ID
            )

            Logging.info(f"Merging log with user-cluster mapping for {user_label}")

            cluster_homepage_mapped_user_content_df = MVUtils.get_inner_merged_df(
                homepage_mapped_user_content_df, user_cluster_mapping, on=CUSTOMER_ID
            )

            most_viewed_df = MVUtils.get_cluster_and_homepage_wise_most_viewed_contents(
                cluster_homepage_mapped_user_content_df
            )

            most_viewed_df = most_viewed_df.drop_duplicates(
                subset=[CLUSTER_ID, HOMEPAGE_ID, CONTENT_ID]
            ).reset_index(drop=True)

            most_viewed_df = MVUtils.add_created_on_attribute(most_viewed_df)
            most_viewed_df = MVUtils.add_recommendation_type_attribute(
                most_viewed_df, MOST_VIEWED_MODULE_NAME.upper()
            )

            most_viewed_df = most_viewed_df.sort_values(
                [CLUSTER_ID, HOMEPAGE_ID, SCORE], ascending=(True, True, False)
            ).reset_index(drop=True)
            most_viewed_df = most_viewed_df[
                [CLUSTER_ID, HOMEPAGE_ID, CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
            ].reset_index(drop=True)
            return most_viewed_df
        except Exception as e:
            Logging.error(
                f"Error while preparing most viewed rec for {user_label}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_most_viewed_all_contents():
        try:
            homepage_id_wise = False

            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            user_cluster_mapping = RecommendationUtils.user_cluster_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(
                    f"PREPARING MOST VIEWED REC BASED ON ALL CONTENTS FOR {user_label}"
                )
                output_df = MV.get_all_contents_based_df(
                    user_label, homepage_id_wise, user_content_df, user_cluster_mapping
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + MOST_VIEWED_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            (
                most_viewed_pay_tv_all_content,
                most_viewed_no_pay_tv_all_content,
            ) = list_output_df

            Logging.info("Preparing expected output schema")

            # Convert the dataframe output to json output format
            most_viewed_pay_tv_all_content_json = MVUtils.get_json_format_output(
                most_viewed_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
            )
            most_viewed_no_pay_tv_all_content_json = MVUtils.get_json_format_output(
                most_viewed_no_pay_tv_all_content,
                list_of_key_prefix[1],
                homepage_id_wise,
            )
            return (
                most_viewed_pay_tv_all_content_json,
                most_viewed_no_pay_tv_all_content_json,
            )
        except Exception as e:
            Logging.error(f"Error while preparing all_content_based rec, Error: {e}")

    @staticmethod
    @custom_exception()
    def get_most_viewed_homepage_id():
        try:
            homepage_id_wise = True

            user_content_df = RecommendationUtils.user_viewed_data_from_s3()

            user_cluster_mapping = RecommendationUtils.user_cluster_from_s3()

            list_of_key_prefix = []
            list_label = [PAY_TV, NO_PAY_TV]
            list_output_df = []
            for user_label in list_label:
                Logging.info(
                    f"PREPARING MOST VIEWED REC BASED ON HOMEPAGE_ID FOR {user_label}"
                )
                output_df = MV.get_homepage_id_wise_df(
                    user_label, homepage_id_wise, user_content_df, user_cluster_mapping
                )
                key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + MOST_VIEWED_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
                )
                list_of_key_prefix.append(key_prefix)
                list_output_df.append(output_df)
            (
                most_viewed_pay_tv_homepage_id,
                most_viewed_no_pay_tv_homepage_id,
            ) = list_output_df

            Logging.info("Preparing expected output schema")

            # Convert the dataframe output to json output format
            most_viewed_pay_tv_homepage_id_json = MVUtils.get_json_format_output(
                most_viewed_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
            )
            most_viewed_no_pay_tv_homepage_id_json = MVUtils.get_json_format_output(
                most_viewed_no_pay_tv_homepage_id,
                list_of_key_prefix[1],
                homepage_id_wise,
            )
            return (
                most_viewed_pay_tv_homepage_id_json,
                most_viewed_no_pay_tv_homepage_id_json,
            )
        except Exception as e:
            Logging.error(f"Error while preparing homepage_id_based rec, Error: {e}")