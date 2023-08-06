import time
import pandas as pd
from offline_results.common.constants import (
    SERVICE_NAME,
    TRENDING_MODULE_NAME,
    ALL_CONTENT_BASED,
    HOMEPAGE_ID_BASED,
    PAY_TV,
    NO_PAY_TV,
)
from offline_results.recommendation.homepage_recommendation.trending.trending_model_utils import TrendingModelUtils
from offline_results.utils import custom_exception, Logging


class TrendingModel:
    viewed_relation_history_df = pd.DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    content_homepage_paytv_homepage = []
    content_homepage_nopaytv_homepage = []
    content_homepage_paytv_allcontent = []
    content_homepage_nopaytv_allcontent = []

    @staticmethod
    @custom_exception()
    def trending_algorithm(obj, user_label, homepage_id_wise):
        rec_type = TRENDING_MODULE_NAME
        content_homepage_id_mapping, history_content_df = TrendingModelUtils.fetch_historical_data(obj,
                                                                                                   user_label,
                                                                                                   homepage_id_wise)
        latest_month_df = TrendingModelUtils.get_latest_week_df(history_content_df)
        if content_homepage_id_mapping.empty:
            return content_homepage_id_mapping
        Logging.info("Calculating Trending Score from " + user_label + " UBD data")
        if homepage_id_wise:
            trending_content_df = TrendingModelUtils.homepage_id_wise_scaling(rec_type, latest_month_df)
        else:
            trending_content_df = TrendingModelUtils.final_result_df(
                rec_type, history_content_df=latest_month_df, homepage_id_wise=False
            )
        return trending_content_df

    @staticmethod
    @custom_exception()
    def get_trending_content_homepage_id():
        obj = TrendingModel
        TrendingModelUtils.clear_data(obj)
        TrendingModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Trending Content based on Homepage_id")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating trending content based on Homepage_id for "
                + user_label
                + " users"
            )
            output_df = TrendingModel.trending_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Trending Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + TRENDING_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        trending_pay_tv_homepage_id, trending_no_pay_tv_homepage_id = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if trending_pay_tv_homepage_id.empty:
            trending_pay_tv_homepage_id_dict = {}
        else:
            trending_pay_tv_homepage_id_dict = TrendingModelUtils.get_dict_format_output(
                trending_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
            )
        if trending_no_pay_tv_homepage_id.empty:
            trending_no_pay_tv_homepage_id_dict = {}
        else:
            trending_no_pay_tv_homepage_id_dict = TrendingModelUtils.get_dict_format_output(
                trending_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Trending Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return trending_pay_tv_homepage_id_dict, trending_no_pay_tv_homepage_id_dict

    @staticmethod
    @custom_exception()
    def get_trending_content_all_content():
        obj = TrendingModel
        TrendingModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Trending Content based on All Content")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating trending content based on All Content for "
                + user_label
                + " users"
            )
            output_df = TrendingModel.trending_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Trending Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + TRENDING_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        trending_pay_tv_all_content, trending_no_pay_tv_all_content = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if trending_pay_tv_all_content.empty:
            trending_pay_tv_all_content_dict = {}
        else:
            trending_pay_tv_all_content_dict = TrendingModelUtils.get_dict_format_output(
                trending_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
            )
        if trending_no_pay_tv_all_content.empty:
            trending_no_pay_tv_all_content_dict = {}
        else:
            trending_no_pay_tv_all_content_dict = TrendingModelUtils.get_dict_format_output(
                trending_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Trending Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        TrendingModelUtils.clear_data(obj)
        return trending_pay_tv_all_content_dict, trending_no_pay_tv_all_content_dict
