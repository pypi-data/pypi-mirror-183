import time
from datetime import datetime
import pandas as pd
from offline_results.common.constants import PAY_TV, NO_PAY_TV, SERVICE_NAME, HOMEPAGE_ID_BASED, \
    DEFAULT_TRENDING_MODULE_NAME, ALL_CONTENT_BASED, CONTENT_ID, HOMEPAGE_ID, CREATED_ON, SCORE, REC_TYPE
from offline_results.recommendation.homepage_recommendation.trending.trending_model_utils import TrendingModelUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class TrendingFallback:
    viewed_relation_history_df = pd.DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    content_homepage_paytv_homepage = []
    content_homepage_nopaytv_homepage = []
    content_homepage_paytv_allcontent = []
    content_homepage_nopaytv_allcontent = []

    @staticmethod
    @custom_exception()
    def default_trending_algorithm(obj, user_label, homepage_id_wise):
        homepage_wise_df = pd.DataFrame()
        rec_type = DEFAULT_TRENDING_MODULE_NAME
        content_homepage_id_mapping, history_content_df = TrendingModelUtils.fetch_historical_data(obj,
                                                                                                   user_label,
                                                                                                   homepage_id_wise)
        if content_homepage_id_mapping.empty:
            return content_homepage_id_mapping
        Logging.info("Calculating Trending Score from " + user_label + " UBD data - DEFAULT MODE ")
        if homepage_id_wise:
            trending_content_df = TrendingModelUtils.homepage_id_wise_scaling(rec_type, history_content_df)
        else:
            trending_content_df = TrendingModelUtils.final_result_df(
                rec_type, history_content_df=history_content_df, homepage_id_wise=False
            )
        Logging.info("Finding Trending contents for " + user_label + " in NON-UBD Data - DEFAULT MODE ")
        content_in_trending_content_df = trending_content_df[CONTENT_ID].unique()
        additional_df = content_homepage_id_mapping[
            ~content_homepage_id_mapping[CONTENT_ID].isin(content_in_trending_content_df)
        ]
        if homepage_id_wise:
            additional_df = additional_df.sort_values(
                by=[HOMEPAGE_ID, CREATED_ON], ascending=[True, False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID, HOMEPAGE_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            trending_content_df = pd.concat(
                [trending_content_df, additional_df], ignore_index=True)
            unique_homepage = trending_content_df[HOMEPAGE_ID].unique()
            for i in unique_homepage:
                trending_content_df_tmp = trending_content_df[trending_content_df[HOMEPAGE_ID] == i]
                trending_content_df_tmp = RecommendationUtils().get_recommendation_scores(trending_content_df_tmp)
                homepage_wise_df = pd.concat([homepage_wise_df, trending_content_df_tmp], ignore_index=True)
        else:
            additional_df = additional_df.sort_values(
                by=[CREATED_ON], ascending=[False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            trending_content_df = pd.concat(
                [trending_content_df, additional_df], axis=0).reset_index(drop=True)
            trending_content_df = trending_content_df.drop_duplicates(subset=[CONTENT_ID], keep="first"). \
                reset_index(drop=True)
            trending_content_df = RecommendationUtils().get_recommendation_scores(trending_content_df)
        return homepage_wise_df if homepage_id_wise else trending_content_df

    @staticmethod
    @custom_exception()
    def get_default_trending_homepage_id():
        obj = TrendingFallback
        TrendingModelUtils.clear_data(obj)
        TrendingModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_dict = []
        Logging.info("Get Fallback Trending Content based on Homepage_id")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating fallback trending content based on Homepage_id for "
                + user_label
                + " users"
            )
            output_df = TrendingFallback.default_trending_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Fallback Trending Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_TRENDING_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_dict.append(output_df)
        fallback_trending_pay_tv_homepage_id, fallback_trending_no_pay_tv_homepage_id = list_output_dict

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if fallback_trending_pay_tv_homepage_id.empty:
            fallback_trending_pay_tv_homepage_id_dict = {}
        else:
            fallback_trending_pay_tv_homepage_id_dict = TrendingModelUtils.get_dict_format_output(
                fallback_trending_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
            )
        if fallback_trending_no_pay_tv_homepage_id.empty:
            fallback_trending_no_pay_tv_homepage_id_dict = {}
        else:
            fallback_trending_no_pay_tv_homepage_id_dict = TrendingModelUtils.get_dict_format_output(
                fallback_trending_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Fallback Trending Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return fallback_trending_pay_tv_homepage_id_dict, fallback_trending_no_pay_tv_homepage_id_dict

    @staticmethod
    @custom_exception()
    def get_default_trending_all_content():
        obj = TrendingFallback
        TrendingModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_dict = []
        Logging.info("Get Fallback Trending Content based on All Content")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating fallback trending content based on All Content for "
                + user_label
                + " users"
            )
            output_df = TrendingFallback.default_trending_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Fallback Trending Dataframe Output")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_TRENDING_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_dict.append(output_df)
        fallback_trending_pay_tv_all_content, fallback_trending_no_pay_tv_all_content = list_output_dict

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if fallback_trending_pay_tv_all_content.empty:
            fallback_trending_pay_tv_all_content_dict = {}
        else:
            fallback_trending_pay_tv_all_content_dict = TrendingModelUtils.get_dict_format_output(
                fallback_trending_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
            )
        if fallback_trending_no_pay_tv_all_content.empty:
            fallback_trending_no_pay_tv_all_content_dict = {}
        else:
            fallback_trending_no_pay_tv_all_content_dict = TrendingModelUtils.get_dict_format_output(
                fallback_trending_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Fallback Trending Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        TrendingModelUtils.clear_data(obj)
        return fallback_trending_pay_tv_all_content_dict, fallback_trending_no_pay_tv_all_content_dict
