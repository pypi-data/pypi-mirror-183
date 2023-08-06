import time
from datetime import datetime

import pandas as pd
from graphdb import GraphDb

from offline_results.common.constants import (
    PAY_TV,
    NO_PAY_TV,
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    HOMEPAGE_ID_BASED,
    DEFAULT_SEASONAL_MODULE_NAME, CONTENT_ID, HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE,
)
from offline_results.recommendation.homepage_recommendation.seasonal.seasonal_model_utils import SeasonalModelUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class SeasonalModelDefault:
    viewed_relation_history_df = pd.DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    graph: GraphDb

    def __init__(self):
        SeasonalModelDefault.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def default_seasonal_algorithm(obj, user_label, homepage_id_wise):
        homepage_wise_df = pd.DataFrame()
        rec_type = DEFAULT_SEASONAL_MODULE_NAME
        content_homepage_id_mapping, history_content_df = SeasonalModelUtils.fetch_historical_data(obj,
                                                                                                   SeasonalModelDefault().graph,
                                                                                                   user_label,
                                                                                                   homepage_id_wise)
        if content_homepage_id_mapping.empty:
            return content_homepage_id_mapping
        Logging.info("Finding Seasonal contents for " + user_label + " in UBD Data - DEFAULT MODE ")
        if homepage_id_wise:
            seasonal_content_df = SeasonalModelUtils.homepage_id_wise_scaling(rec_type, history_content_df)
        else:
            seasonal_content_df = SeasonalModelUtils.final_result_df(
                rec_type, history_content_df=history_content_df, homepage_id_wise=False
            )
        Logging.info("Finding Seasonal contents for " + user_label + " in NON-UBD Data - DEFAULT MODE ")
        content_in_seasonal_content_df = seasonal_content_df[CONTENT_ID].unique()
        additional_df = content_homepage_id_mapping[
            ~content_homepage_id_mapping[CONTENT_ID].isin(content_in_seasonal_content_df)
        ]
        if homepage_id_wise:
            additional_df = additional_df.sort_values(
                by=[HOMEPAGE_ID, CREATED_ON], ascending=[True, False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID, HOMEPAGE_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            seasonal_content_df = pd.concat(
                [seasonal_content_df, additional_df], ignore_index=True)
            unique_homepage = seasonal_content_df[HOMEPAGE_ID].unique()
            for i in unique_homepage:
                seasonal_content_df_tmp = seasonal_content_df[seasonal_content_df[HOMEPAGE_ID] == i]
                seasonal_content_df_tmp = RecommendationUtils().get_recommendation_scores(seasonal_content_df_tmp)
                homepage_wise_df = pd.concat([homepage_wise_df, seasonal_content_df_tmp], ignore_index=True)
        else:
            additional_df = additional_df.sort_values(
                by=[CREATED_ON], ascending=[False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            seasonal_content_df = pd.concat(
                [seasonal_content_df, additional_df], axis=0).reset_index(drop=True)
            seasonal_content_df = seasonal_content_df.drop_duplicates(subset=[CONTENT_ID], keep="first"). \
                reset_index(drop=True)
            seasonal_content_df = RecommendationUtils().get_recommendation_scores(seasonal_content_df)
        return homepage_wise_df if homepage_id_wise else seasonal_content_df

    @staticmethod
    @custom_exception()
    def get_default_seasonal_content_all_content():
        obj = SeasonalModelDefault
        SeasonalModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Seasonal Content based on All Content - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating seasonal content based on All Content for "
                + user_label
                + " users - DEFAULT MODE"
            )
            output_df = SeasonalModelDefault.default_seasonal_algorithm(
                obj, user_label, homepage_id_wise
            ).reset_index(drop=True)
            Logging.info(
                "Success Preparing Default Seasonal Dataframe Output - DEFAULT MODE"
            )
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_SEASONAL_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        (
            default_seasonal_pay_tv_all_content,
            default_seasonal_no_pay_tv_all_content,
        ) = list_output_df
        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if default_seasonal_pay_tv_all_content.empty:
            default_seasonal_pay_tv_all_content_dict = {}
        else:
            default_seasonal_pay_tv_all_content_dict = (
                SeasonalModelUtils.get_dict_format_output(
                    default_seasonal_pay_tv_all_content,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )

        if default_seasonal_no_pay_tv_all_content.empty:
            default_seasonal_no_pay_tv_all_content_dict = {}
        else:
            default_seasonal_no_pay_tv_all_content_dict = (
                SeasonalModelUtils.get_dict_format_output(
                    default_seasonal_no_pay_tv_all_content,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Default Seasonal Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        SeasonalModelUtils.clear_data(obj)
        return (
            default_seasonal_pay_tv_all_content_dict,
            default_seasonal_no_pay_tv_all_content_dict,
        )

    @staticmethod
    @custom_exception()
    def get_default_seasonal_content_homepage_id():
        obj = SeasonalModelDefault
        SeasonalModelUtils.clear_data(obj)
        SeasonalModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Seasonal Content based on Homepage_id - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating seasonal content based on Homepage_id for "
                + user_label
                + " users - DEFAULT MODE"
            )
            output_df = SeasonalModelDefault.default_seasonal_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info(
                "Success Preparing Default Seasonal Dataframe Output - DEFAULT MODE"
            )
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_SEASONAL_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        (
            default_seasonal_pay_tv_homepage_id,
            default_seasonal_no_pay_tv_homepage_id,
        ) = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if default_seasonal_pay_tv_homepage_id.empty:
            default_seasonal_pay_tv_homepage_id_dict = {}
        else:
            default_seasonal_pay_tv_homepage_id_dict = (
                SeasonalModelUtils.get_dict_format_output(
                    default_seasonal_pay_tv_homepage_id,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )
        if default_seasonal_no_pay_tv_homepage_id.empty:
            default_seasonal_no_pay_tv_homepage_id_dict = {}
        else:
            default_seasonal_no_pay_tv_homepage_id_dict = (
                SeasonalModelUtils.get_dict_format_output(
                    default_seasonal_no_pay_tv_homepage_id,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )

        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Default Seasonal Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return (
            default_seasonal_pay_tv_homepage_id_dict,
            default_seasonal_no_pay_tv_homepage_id_dict,
        )
