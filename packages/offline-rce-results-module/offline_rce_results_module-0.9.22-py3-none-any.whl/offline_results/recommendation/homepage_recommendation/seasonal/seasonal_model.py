import time

from graphdb import GraphDb
from pandas import DataFrame

from offline_results.common.constants import (
    SERVICE_NAME,
    SEASONAL_MODULE_NAME,
    HOMEPAGE_ID_BASED,
    PAY_TV,
    NO_PAY_TV,
    ALL_CONTENT_BASED
)
from offline_results.recommendation.homepage_recommendation.seasonal.seasonal_model_utils import SeasonalModelUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class SeasonalModel:
    viewed_relation_history_df = DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    graph: GraphDb

    def __init__(self):
        SeasonalModel.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def seasonal_algorithm(obj, user_label, homepage_id_wise):
        rec_type = SEASONAL_MODULE_NAME
        content_homepage_id_mapping, history_content_df = SeasonalModelUtils.fetch_historical_data(obj,
                                                                                                   SeasonalModel().graph,
                                                                                                   user_label,
                                                                                                   homepage_id_wise)
        if content_homepage_id_mapping.empty:
            return content_homepage_id_mapping
        Logging.info("Calculating Seasonal Score from " + user_label + " UBD data")
        if homepage_id_wise:
            seasonal_content_df = SeasonalModelUtils.homepage_id_wise_scaling(rec_type, history_content_df)
        else:
            seasonal_content_df = SeasonalModelUtils.final_result_df(
                rec_type, history_content_df=history_content_df, homepage_id_wise=False
            )
        return seasonal_content_df

    @staticmethod
    @custom_exception()
    def get_seasonal_content_all_content():
        obj = SeasonalModel
        SeasonalModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Seasonal Content based on All Content")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating seasonal content based on All Content for "
                + user_label
                + " users"
            )
            output_df = SeasonalModel.seasonal_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Seasonal Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + SEASONAL_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        seasonal_pay_tv_all_content, seasonal_no_pay_tv_all_content = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if seasonal_pay_tv_all_content.empty:
            seasonal_pay_tv_all_content_dict = {}
        else:
            seasonal_pay_tv_all_content_dict = SeasonalModelUtils.get_dict_format_output(
                seasonal_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
            )
        if seasonal_no_pay_tv_all_content.empty:
            seasonal_no_pay_tv_all_content_dict = {}
        else:
            seasonal_no_pay_tv_all_content_dict = SeasonalModelUtils.get_dict_format_output(
                seasonal_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Seasonal Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        SeasonalModelUtils.clear_data(obj)
        return seasonal_pay_tv_all_content_dict, seasonal_no_pay_tv_all_content_dict

    @staticmethod
    @custom_exception()
    def get_seasonal_content_homepage_id():
        obj = SeasonalModel
        SeasonalModelUtils.clear_data(obj)
        SeasonalModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Seasonal Content based on Homepage_id")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating seasonal content based on Homepage_id for "
                + user_label
                + " users"
            )
            output_df = SeasonalModel.seasonal_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Seasonal Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + SEASONAL_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        seasonal_pay_tv_homepage_id, seasonal_no_pay_tv_homepage_id = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if seasonal_pay_tv_homepage_id.empty:
            seasonal_pay_tv_homepage_id_dict = {}
        else:
            seasonal_pay_tv_homepage_id_dict = SeasonalModelUtils.get_dict_format_output(
                seasonal_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
            )
        if seasonal_no_pay_tv_homepage_id.empty:
            seasonal_no_pay_tv_homepage_id_dict = {}
        else:
            seasonal_no_pay_tv_homepage_id_dict = SeasonalModelUtils.get_dict_format_output(
                seasonal_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Seasonal Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return seasonal_pay_tv_homepage_id_dict, seasonal_no_pay_tv_homepage_id_dict
