import time
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from offline_results.common.constants import (
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    DEFAULT_POPULAR_MODULE_NAME,
    PAY_TV,
    HOMEPAGE_ID_BASED,
    NO_PAY_TV, RATING_AVERAGE, RATING_COUNT, WEIGHTED_RATING, CONTENT_ID, INNER, HOMEPAGE_ID, CREATED_ON, SCORE,
    REC_TYPE,
)
from offline_results.recommendation.homepage_recommendation.popular.popular_model_utils import PopularModelUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class PopularModelFallback:
    viewed_relation_history_df = DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []
    content_homepage_paytv_homepage = []
    content_homepage_nopaytv_homepage = []
    content_homepage_paytv_allcontent = []
    content_homepage_nopaytv_allcontent = []

    @staticmethod
    @custom_exception()
    def default_popular_algorithm(obj, user_label, homepage_id_wise):
        homepage_wise_df = pd.DataFrame()
        rec_type = DEFAULT_POPULAR_MODULE_NAME
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

        Logging.info("Finding popular contents for " + user_label + " in UBD Data - DEFAULT MODE ")
        if homepage_id_wise:
            popular_content_df = PopularModelUtils.homepage_id_wise_scaling(rec_type, listed_content_df)
        else:
            popular_content_df = PopularModelUtils.final_result_df(
                rec_type, history_content_df=listed_content_df, homepage_id_wise=False
            )
        Logging.info("Finding popular contents for " + user_label + " in NON-UBD Data - DEFAULT MODE ")
        content_in_popular_content_df = popular_content_df[CONTENT_ID].unique()
        additional_df = content_homepage_id_mapping[
            ~content_homepage_id_mapping[CONTENT_ID].isin(content_in_popular_content_df)
        ]
        if homepage_id_wise:
            additional_df = additional_df.sort_values(
                by=[HOMEPAGE_ID, CREATED_ON], ascending=[True, False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID, HOMEPAGE_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            popular_content_df = pd.concat(
                [popular_content_df, additional_df], ignore_index=True)
            unique_homepage = popular_content_df[HOMEPAGE_ID].unique()
            for i in unique_homepage:
                popular_content_df_tmp = popular_content_df[popular_content_df[HOMEPAGE_ID] == i]
                popular_content_df_tmp = RecommendationUtils().get_recommendation_scores(popular_content_df_tmp)
                homepage_wise_df = pd.concat([homepage_wise_df, popular_content_df_tmp], ignore_index=True)
        else:
            additional_df = additional_df.sort_values(
                by=[CREATED_ON], ascending=[False]
            ).reset_index(drop=True)
            additional_df = additional_df[[CONTENT_ID]]
            additional_df[SCORE] = 0
            additional_df[CREATED_ON] = datetime.utcnow().isoformat()
            additional_df[REC_TYPE] = rec_type.upper()
            popular_content_df = pd.concat(
                [popular_content_df, additional_df], axis=0).reset_index(drop=True)
            popular_content_df = popular_content_df.drop_duplicates(subset=[CONTENT_ID], keep="first"). \
                reset_index(drop=True)
            popular_content_df = RecommendationUtils().get_recommendation_scores(popular_content_df)
        return homepage_wise_df if homepage_id_wise else popular_content_df

    @staticmethod
    @custom_exception()
    def get_default_popular_homepage_id():
        obj = PopularModelFallback
        PopularModelUtils.clear_data(obj)
        PopularModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Popular Fallback Content based on Homepage_id - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating fallback popular content based on Homepage_id for "
                + user_label
                + " users - DEFAULT MODE"
            )
            output_df = PopularModelFallback.default_popular_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Fallback Trending Dataframe Output - DEFAULT MODE")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_POPULAR_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        (
            fallback_popular_pay_tv_homepage_id,
            fallback_popular_no_pay_tv_homepage_id,
        ) = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if fallback_popular_pay_tv_homepage_id.empty:
            fallback_popular_pay_tv_homepage_id_dict = {}
        else:
            fallback_popular_pay_tv_homepage_id_dict = (
                PopularModelUtils.get_dict_format_output(
                    fallback_popular_pay_tv_homepage_id,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )
        if fallback_popular_no_pay_tv_homepage_id.empty:
            fallback_popular_no_pay_tv_homepage_id_dict = {}
        else:
            fallback_popular_no_pay_tv_homepage_id_dict = (
                PopularModelUtils.get_dict_format_output(
                    fallback_popular_no_pay_tv_homepage_id,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Fallback Popular Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return fallback_popular_pay_tv_homepage_id_dict, fallback_popular_no_pay_tv_homepage_id_dict

    @staticmethod
    @custom_exception()
    def get_default_popular_all_content():
        obj = PopularModelFallback
        PopularModelUtils.get_data(obj)
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        Logging.info("Get Fallback Popular Content based on All Content - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating fallback popular content based on All Content for "
                + user_label
                + " users - DEFAULT MODE"
            )
            output_df = PopularModelFallback.default_popular_algorithm(
                obj, user_label, homepage_id_wise
            )
            Logging.info("Success Preparing Fallback Popular Dataframe Output - DEFAULT MODE")
            key_prefix = (
                    SERVICE_NAME
                    + ":"
                    + DEFAULT_POPULAR_MODULE_NAME.lower()
                    + ":"
                    + user_label
                    + ":"
                    + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        fallback_popular_pay_tv_all_content, fallback_popular_no_pay_tv_all_content = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        if fallback_popular_pay_tv_all_content.empty:
            fallback_popular_pay_tv_all_content_dict = {}
        else:
            fallback_popular_pay_tv_all_content_dict = (
                PopularModelUtils.get_dict_format_output(
                    fallback_popular_pay_tv_all_content,
                    list_of_key_prefix[0],
                    homepage_id_wise,
                )
            )
        if fallback_popular_no_pay_tv_all_content.empty:
            fallback_popular_no_pay_tv_all_content_dict = {}
        else:
            fallback_popular_no_pay_tv_all_content_dict = (
                PopularModelUtils.get_dict_format_output(
                    fallback_popular_no_pay_tv_all_content,
                    list_of_key_prefix[1],
                    homepage_id_wise,
                )
            )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Fallback Popular Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        PopularModelUtils.clear_data(obj)
        return fallback_popular_pay_tv_all_content_dict, fallback_popular_no_pay_tv_all_content_dict

