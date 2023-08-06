import time
import pandas as pd
from offline_results.common.constants import (
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    POPULAR_MODULE_NAME,
    HOMEPAGE_ID_BASED,
    PAY_TV,
    NO_PAY_TV, CONTENT_ID, RATING_COUNT, INNER, RATING_AVERAGE, WEIGHTED_RATING, )
from offline_results.recommendation.homepage_recommendation.popular.popular_model_utils import PopularModelUtils
from offline_results.utils import custom_exception, Logging


class PopularModel:
    viewed_relation_history_df = pd.DataFrame()
    implicit_rating_df = pd.DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    content_homepage_paytv_homepage = []
    content_homepage_nopaytv_homepage = []
    content_homepage_paytv_allcontent = []
    content_homepage_nopaytv_allcontent = []

    @staticmethod
    @custom_exception()
    def popular_algorithm(obj, user_label, homepage_id_wise):
        rec_type = POPULAR_MODULE_NAME
        content_homepage_id_mapping, history_content_df = PopularModelUtils.fetch_historical_data(obj,
                                                                                                  user_label,
                                                                                                  homepage_id_wise)
        if content_homepage_id_mapping.empty:
            return content_homepage_id_mapping
        prepared_data = PopularModelUtils.prepare_rating_data(obj, history_content_df, user_label)

        Logging.info("Calculating Weighted Rating")
        C = prepared_data[RATING_AVERAGE].mean()
        m = prepared_data[RATING_COUNT].quantile(0.3)
        listed_content_df = prepared_data.loc[prepared_data[RATING_COUNT] >= 1]
        listed_content_df[WEIGHTED_RATING] = listed_content_df.apply(
            lambda x: PopularModelUtils.weighted_rating_formula(x, m=m, C=C), axis=1
        )
        listed_content_df = pd.merge(
            listed_content_df, content_homepage_id_mapping, on=CONTENT_ID, how=INNER
        )

        Logging.info("Calculating Popular Score from " + user_label + " UBD data")
        if homepage_id_wise:
            popular_content_df = PopularModelUtils.homepage_id_wise_scaling(rec_type, listed_content_df)
        else:
            popular_content_df = PopularModelUtils.final_result_df(
                rec_type, history_content_df=listed_content_df, homepage_id_wise=False
            )
        return popular_content_df

    @staticmethod
    @custom_exception()
    def get_popular_content_all_content():
        obj = PopularModel
        PopularModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Popular Content based on All Content")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating popular content based on All Content for "
                + user_label
                + " users"
            )
            output_df = PopularModel.popular_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Popular Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + POPULAR_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        popular_pay_tv_all_content, popular_no_pay_tv_all_content = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if popular_pay_tv_all_content.empty:
            popular_pay_tv_all_content_dict = {}
        else:
            popular_pay_tv_all_content_dict = PopularModelUtils.get_dict_format_output(
                popular_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
            )
        if popular_no_pay_tv_all_content.empty:
            popular_no_pay_tv_all_content_dict = {}
        else:
            popular_no_pay_tv_all_content_dict = PopularModelUtils.get_dict_format_output(
                popular_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Popular Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        PopularModelUtils.clear_data(obj)
        return popular_pay_tv_all_content_dict, popular_no_pay_tv_all_content_dict

    @staticmethod
    @custom_exception()
    def get_popular_content_homepage_id():
        obj = PopularModel
        PopularModelUtils.clear_data(obj)
        PopularModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Popular Content based on Homepage_id")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating popular content based on Homepage_id for "
                + user_label
                + " users"
            )
            output_df = PopularModel.popular_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Popular Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + POPULAR_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        popular_pay_tv_homepage_id, popular_no_pay_tv_homepage_id = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if popular_pay_tv_homepage_id.empty:
            popular_pay_tv_homepage_id_dict = {}
        else:
            popular_pay_tv_homepage_id_dict = PopularModelUtils.get_dict_format_output(
                popular_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
            )
        if popular_no_pay_tv_homepage_id.empty:
            popular_no_pay_tv_homepage_id_dict = {}
        else:
            popular_no_pay_tv_homepage_id_dict = PopularModelUtils.get_dict_format_output(
                popular_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Popular Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return popular_pay_tv_homepage_id_dict, popular_no_pay_tv_homepage_id_dict

