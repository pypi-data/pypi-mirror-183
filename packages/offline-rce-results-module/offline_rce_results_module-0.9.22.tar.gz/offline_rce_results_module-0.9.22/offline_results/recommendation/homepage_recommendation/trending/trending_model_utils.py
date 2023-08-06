import datetime
import time
from datetime import datetime
import dateutil.relativedelta
import pandas as pd
from gast import literal_eval
from pandas import DataFrame, merge, concat
from sklearn.preprocessing import MinMaxScaler
from offline_results.common.config import CONFIG_HOMEPAGE_PAYTV, CONFIG_HOMEPAGE_NO_PAYTV
from offline_results.common.constants import HOMEPAGE_ID, CONTENT_ID, SCORE, CREATED_ON, REC_TYPE, RECORDS, PAY_TV, \
    IS_PAY_TV, VIEW_HISTORY, DURATION, UBD_CREATED_ON, MODEL_NAME, VIEW_COUNT, \
    SCALED_DURATION, RECOMMENDATION_SCORE, SCALED_VIEW_COUNT, TRENDING_MODULE_NAME, RANK_SCORE, NO_PAY_TV
from offline_results.recommendation.homepage_recommendation.special_model_utils_function.special_model_utils import \
    SpecialModelUtils
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class TrendingModelUtils:
    @staticmethod
    @custom_exception()
    def get_data(obj):
        if len(obj.viewed_relation_history_df) != 0:
            return
        starttime = time.time()
        obj.viewed_relation_history_df = RecommendationUtils.user_viewed_data_from_s3()
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
        config_df = config_df[config_df[MODEL_NAME] == TRENDING_MODULE_NAME.lower()].reset_index(drop=True)
        config_df[HOMEPAGE_ID] = config_df[HOMEPAGE_ID].astype(int)
        df[HOMEPAGE_ID] = df[HOMEPAGE_ID].astype(int)
        df = df[df[HOMEPAGE_ID].isin(config_df[HOMEPAGE_ID])].reset_index(drop=True)
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
        content_homepage_df = TrendingModelUtils.filter_by_dedicated_homepage_id(
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
    def get_latest_week_df(history_content_df):
        Logging.info("Get last week UBD Dataframe data")
        history_content_df[UBD_CREATED_ON] = history_content_df[VIEW_HISTORY].apply(
            lambda x: x[CREATED_ON]
        )
        history_content_df[UBD_CREATED_ON] = pd.to_datetime(
            history_content_df[UBD_CREATED_ON], dayfirst=True
        )
        history_content_df = history_content_df.sort_values(
            by=UBD_CREATED_ON, ascending=False
        ).reset_index(drop=True)
        past_month_date = str(datetime.now() + dateutil.relativedelta.relativedelta(months=-1))
        past_month_date = pd.Timestamp(past_month_date, tz="Asia/Jakarta").tz_convert(tz="UTC").isoformat()
        past_month_ubd = history_content_df[history_content_df[UBD_CREATED_ON] > past_month_date]
        return past_month_ubd

    @staticmethod
    @custom_exception()
    def final_result_df(rec_type, history_content_df, homepage_id_wise):
        if homepage_id_wise:
            season_df_tmp = history_content_df.groupby(
                [CONTENT_ID, HOMEPAGE_ID])[[VIEW_COUNT, DURATION]].sum().reset_index()
            season_df_tmp = season_df_tmp.set_index([CONTENT_ID, HOMEPAGE_ID])
        else:
            season_df_tmp = history_content_df.groupby(
                [CONTENT_ID])[[VIEW_COUNT, DURATION]].sum().reset_index()
            season_df_tmp = season_df_tmp.set_index(CONTENT_ID)
        scaled_features_df = MinMaxScaler(feature_range=(0.1, 1)).fit_transform(
            season_df_tmp.values
        )
        scaled_features_df = DataFrame(
            scaled_features_df,
            index=season_df_tmp.index,
            columns=season_df_tmp.columns,
        ).rename(columns={DURATION: SCALED_DURATION, VIEW_COUNT: SCALED_VIEW_COUNT})
        scaled_features_df[RECOMMENDATION_SCORE] = round(
            (scaled_features_df[SCALED_DURATION] * 0.7)
            + (scaled_features_df[SCALED_VIEW_COUNT] * 0.3),
            3,
        )
        Logging.info("Preparing Final Dataframe Output")
        scaled_features_df = scaled_features_df.sort_values(
            by=RECOMMENDATION_SCORE, ascending=False
        )
        scaled_features_df = scaled_features_df.assign(
            rank_score=[i for i in range(len(scaled_features_df), 0, -1)]
        )
        scaled_features_df[SCORE] = (
                scaled_features_df[RECOMMENDATION_SCORE]
                + scaled_features_df[RANK_SCORE]
        )
        scaled_features_df[[SCORE]] = MinMaxScaler(
            feature_range=(0.1, 1)
        ).fit_transform(scaled_features_df[[SCORE]])
        scaled_features_df[SCORE] = scaled_features_df[SCORE].apply(
            lambda x: round(x, 3)
        )
        scaled_features_df[CREATED_ON] = datetime.utcnow().isoformat()
        if homepage_id_wise:
            seasonal_content_df = (
                scaled_features_df[[SCORE, CREATED_ON]]
                .rename_axis([CONTENT_ID, HOMEPAGE_ID])
                .reset_index()
            )
            seasonal_content_df = seasonal_content_df.sort_values(
                by=[HOMEPAGE_ID, SCORE], ascending=[True, False]
            )
        else:
            seasonal_content_df = (
                scaled_features_df[[SCORE, CREATED_ON]]
                .rename_axis(CONTENT_ID)
                .reset_index()
            )
            seasonal_content_df = seasonal_content_df.sort_values(
                by=SCORE, ascending=False
            )
        seasonal_content_df[REC_TYPE] = rec_type.upper()
        return seasonal_content_df

    @staticmethod
    @custom_exception()
    def homepage_id_wise_scaling(rec_type, history_content_df):
        homepage_seasonal_content_df = DataFrame()
        homepage_ids = history_content_df[HOMEPAGE_ID].unique()
        for idx in homepage_ids:
            df = history_content_df[history_content_df[HOMEPAGE_ID] == idx]
            seasonal_content_df = TrendingModelUtils.final_result_df(rec_type, history_content_df=df,
                                                                     homepage_id_wise=True)
            homepage_seasonal_content_df = concat(
                [homepage_seasonal_content_df, seasonal_content_df], ignore_index=True
            )
        return homepage_seasonal_content_df
