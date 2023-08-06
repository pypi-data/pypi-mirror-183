from ast import literal_eval
from datetime import datetime
import pandas as pd
from pandas import DataFrame, merge, concat
from sklearn.preprocessing import MinMaxScaler
import time
from offline_results.common.config import CONFIG_HOMEPAGE_PAYTV, CONFIG_HOMEPAGE_NO_PAYTV
from offline_results.common.constants import HOMEPAGE_ID, CONTENT_ID, REC_TYPE, SCORE, CREATED_ON, \
    RECORDS, PAY_TV, MODEL_NAME, IS_PAY_TV, VIEW_HISTORY, DURATION, VIEW_COUNT, POPULAR_MODULE_NAME, RATING_COUNT, \
    RATING_AVERAGE, UBD_CREATED_ON, INNER, IMPLICIT_RATING, CUSTOMER_ID, RATING_SUM, RECOMMENDATION_SCORE, \
    SCALED_DURATION, SCALED_WEIGHTED_RATING, RANK_SCORE, WEIGHTED_RATING, NO_PAY_TV
from offline_results.recommendation.homepage_recommendation.special_model_utils_function.special_model_utils import \
    SpecialModelUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class PopularModelUtils:
    @staticmethod
    @custom_exception()
    def get_data(obj):
        if len(obj.viewed_relation_history_df) != 0:
            return
        starttime = time.time()
        obj.viewed_relation_history_df = RecommendationUtils.user_viewed_data_from_s3()
        obj.implicit_rating_df = RecommendationUtils.implicit_rating_data_from_s3()
        obj.live_tv_channel_paytv = SpecialModelUtils.get_tv_channels(is_pay_tv=True)
        obj.live_tv_channel_nopaytv = SpecialModelUtils.get_tv_channels(is_pay_tv=False)
        obj.content_homepage_paytv_homepage = SpecialModelUtils.get_content_homepage_id_mapping(PAY_TV, True)
        obj.content_homepage_nopaytv_homepage = SpecialModelUtils.get_content_homepage_id_mapping(NO_PAY_TV, True)
        obj.content_homepage_paytv_allcontent = SpecialModelUtils.get_content_homepage_id_mapping(PAY_TV, False)
        obj.content_homepage_nopaytv_allcontent = SpecialModelUtils.get_content_homepage_id_mapping(NO_PAY_TV, False)
        endtime = time.time()
        Logging.info(
            "Duration for fetching all required data is "
            + str(endtime - starttime)
            + " seconds"
        )

    @staticmethod
    @custom_exception()
    def clear_data(obj):
        obj.viewed_relation_history_df = DataFrame()
        obj.implicit_rating_df = DataFrame()
        obj.live_tv_channel_paytv = []
        obj.live_tv_channel_nopaytv = []
        obj.content_homepage_paytv_homepage = []
        obj.content_homepage_nopaytv_homepage = []
        obj.content_homepage_paytv_allcontent  = []
        obj.content_homepage_nopaytv_allcontent = []

    @staticmethod
    @custom_exception()
    def get_dict_format_output(df, key_prefix, homepage_id_wise):
        if homepage_id_wise:
            output_dict = {}
            unique_homepage_id = df[HOMEPAGE_ID].unique()
            for homepage_id in unique_homepage_id:
                key_prefix_cls_hid = key_prefix + ":" + str(homepage_id)
                homepage_wise_df = df.loc[df[HOMEPAGE_ID] == homepage_id]
                homepage_wise_df = homepage_wise_df[
                    [CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
                ]
                output_dict[key_prefix_cls_hid] = homepage_wise_df.to_dict(RECORDS)
        else:
            df = df[[CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]]
            output_dict = {key_prefix: df.to_dict(RECORDS)}
        return output_dict

    @staticmethod
    @custom_exception()
    def filter_by_dedicated_homepage_id(df, user_label):
        config_dictionary = (
            CONFIG_HOMEPAGE_PAYTV if user_label == PAY_TV else CONFIG_HOMEPAGE_NO_PAYTV
        )
        config_df = DataFrame(config_dictionary.items())
        config_df.columns = [HOMEPAGE_ID, MODEL_NAME]
        config_df = config_df[config_df[MODEL_NAME] == POPULAR_MODULE_NAME.lower()]
        list_dedicated_homepage_id = config_df[HOMEPAGE_ID].tolist()
        df = df[df[HOMEPAGE_ID].isin(list_dedicated_homepage_id)].reset_index(drop=True)
        return df

    @staticmethod
    @custom_exception()
    def fetch_historical_data(obj, user_label, homepage_id_wise):
        Logging.info("Fetch content-homepage_id mapping")
        if homepage_id_wise:
            content_homepage_df = obj.content_homepage_paytv_homepage if user_label == PAY_TV else obj.content_homepage_nopaytv_homepage
        else:
            content_homepage_df = obj.content_homepage_paytv_allcontent if user_label == PAY_TV else obj.content_homepage_nopaytv_allcontent
        if not homepage_id_wise:
            content_homepage_df = content_homepage_df[
                ~content_homepage_df[CONTENT_ID].isin(
                    obj.live_tv_channel_paytv if user_label == PAY_TV else obj.live_tv_channel_nopaytv
                )
            ].reset_index(drop=True)
        Logging.info("Filter by dedicated homepage_id for Trending Model")
        content_homepage_df = PopularModelUtils.filter_by_dedicated_homepage_id(
            content_homepage_df, user_label
        )
        Logging.info("Load User-Behaviour-Data from S3")
        viewed_relation_history_df = obj.viewed_relation_history_df
        is_pay_tv_status = True if user_label == PAY_TV else False
        viewed_relation_history_df = viewed_relation_history_df[
            viewed_relation_history_df[IS_PAY_TV] == is_pay_tv_status
            ].reset_index(drop=True)
        viewed_relation_history_df = merge(
            viewed_relation_history_df, content_homepage_df, on=CONTENT_ID, how="inner"
        )
        if content_homepage_df.empty:
            Logging.info(f'No active trending {user_label} homepage ID/Content ID found !!')
            return content_homepage_df, viewed_relation_history_df
        viewed_relation_history_df[VIEW_HISTORY] = viewed_relation_history_df[VIEW_HISTORY].apply(
            lambda x: literal_eval(str(x)))
        viewed_relation_history_df = viewed_relation_history_df.explode(VIEW_HISTORY)
        viewed_relation_history_df[DURATION] = viewed_relation_history_df[VIEW_HISTORY].apply(lambda x: x[DURATION])
        viewed_relation_history_df = viewed_relation_history_df[
            [CONTENT_ID, HOMEPAGE_ID, VIEW_COUNT, DURATION, VIEW_HISTORY]]
        return content_homepage_df, viewed_relation_history_df

    @staticmethod
    @custom_exception()
    def prepare_rating_data(obj, history_content_df, user_label):
        Logging.info("Load Implicit Rating Network from S3")
        history_content_df[UBD_CREATED_ON] = history_content_df[VIEW_HISTORY].apply(lambda x: x[CREATED_ON])
        is_pay_tv_status = True if user_label == PAY_TV else False
        implicit_rating_df = obj.implicit_rating_df

        implicit_rating_df = implicit_rating_df[
            implicit_rating_df[IS_PAY_TV] == is_pay_tv_status
            ]
        recent_date_df = (
            history_content_df.groupby(CONTENT_ID)
            .agg({UBD_CREATED_ON: "max", DURATION: "sum"})
            .rename_axis(CONTENT_ID)
            .reset_index()
        )
        user_content_network_df = pd.merge(
            recent_date_df, implicit_rating_df, on=[CONTENT_ID], how=INNER
        )
        user_content_network_df = user_content_network_df[
            ~user_content_network_df[IMPLICIT_RATING].isnull()
        ].reset_index(drop=True)
        user_content_network_df = user_content_network_df.drop_duplicates(
            [CONTENT_ID, CUSTOMER_ID, UBD_CREATED_ON]
        )[[CONTENT_ID, DURATION, IMPLICIT_RATING]].reset_index(drop=True)
        user_content_network_df["content_id2"] = user_content_network_df[CONTENT_ID]
        prepared_df = user_content_network_df.groupby([CONTENT_ID]).agg(
            {"content_id2": "count", DURATION: "sum", IMPLICIT_RATING: "sum"}
        ).rename(
            columns={IMPLICIT_RATING: RATING_SUM, "content_id2": RATING_COUNT}).reset_index()
        prepared_df[RATING_AVERAGE] = (
                prepared_df[RATING_SUM] / prepared_df[RATING_COUNT]
        )
        return prepared_df

    @staticmethod
    @custom_exception()
    def weighted_rating_formula(prepared_data, m, C):
        v = prepared_data[RATING_COUNT]
        R = prepared_data[RATING_AVERAGE]

        return (v / (v + m) * R) + (m / (m + v) * C)

    @staticmethod
    @custom_exception()
    def final_result_df(rec_type, history_content_df, homepage_id_wise):
        history_content_df = history_content_df.drop_duplicates(subset=[CONTENT_ID], keep="first").reset_index(drop=True)
        if homepage_id_wise:
            popular_df_tmp = history_content_df.set_index([CONTENT_ID, HOMEPAGE_ID])
        else:
            popular_df_tmp = history_content_df.set_index(CONTENT_ID)
        selected_df = popular_df_tmp[[DURATION, WEIGHTED_RATING]]
        scaled_features_df = MinMaxScaler(feature_range=(0.1, 1)).fit_transform(
            selected_df.values
        )
        scaled_features_df = pd.DataFrame(
            scaled_features_df, index=selected_df.index, columns=selected_df.columns
        ).rename(
            columns={DURATION: SCALED_DURATION, WEIGHTED_RATING: SCALED_WEIGHTED_RATING}
        )
        scaled_features_df[RECOMMENDATION_SCORE] = round(
            (scaled_features_df[SCALED_DURATION] * 0.5)
            + (scaled_features_df[SCALED_WEIGHTED_RATING] * 0.5),
            3,
        )
        scaled_features_df = scaled_features_df.sort_values(
            by=RECOMMENDATION_SCORE, ascending=False
        )
        scaled_features_df = scaled_features_df.assign(
            rank_score=[i for i in range(len(scaled_features_df), 0, -1)]
        )
        scaled_features_df[SCORE] = (
                scaled_features_df[RECOMMENDATION_SCORE] + scaled_features_df[RANK_SCORE]
        )
        scaled_features_df[[SCORE]] = MinMaxScaler(feature_range=(0.1, 1)).fit_transform(
            scaled_features_df[[SCORE]]
        )
        scaled_features_df[SCORE] = scaled_features_df[SCORE].apply(lambda x: round(x, 3))
        Logging.info("Preparing Popular Model Dataframe Output")
        scaled_features_df[CREATED_ON] = datetime.utcnow().isoformat()
        scaled_features_df[REC_TYPE] = rec_type.upper()
        if homepage_id_wise:
            popular_content_df = (
                scaled_features_df[[SCORE, CREATED_ON, REC_TYPE]]
                .rename_axis([CONTENT_ID, HOMEPAGE_ID])
                .reset_index()
            )
            popular_content_df = popular_content_df.sort_values(
                by=[HOMEPAGE_ID, SCORE], ascending=[True, False]
            )
        else:
            popular_content_df = (
                scaled_features_df[[SCORE, CREATED_ON, REC_TYPE]]
                .rename_axis(CONTENT_ID)
                .reset_index()
            )
            popular_content_df = popular_content_df.sort_values(
                by=SCORE, ascending=False
            )
        return popular_content_df

    @staticmethod
    @custom_exception()
    def homepage_id_wise_scaling(rec_type, history_content_df):
        homepage_popular_content_df = DataFrame()
        homepage_ids = history_content_df[HOMEPAGE_ID].unique()
        for idx in homepage_ids:
            df = history_content_df[history_content_df[HOMEPAGE_ID] == idx]
            popular_content_df = PopularModelUtils.final_result_df(rec_type, history_content_df=df,
                                                                   homepage_id_wise=True)
            homepage_popular_content_df = concat(
                [homepage_popular_content_df, popular_content_df], ignore_index=True
            )
        return homepage_popular_content_df
