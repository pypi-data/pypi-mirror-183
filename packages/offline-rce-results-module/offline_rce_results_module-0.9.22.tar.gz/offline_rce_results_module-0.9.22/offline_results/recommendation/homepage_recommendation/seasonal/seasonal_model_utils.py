from ast import literal_eval
from datetime import datetime

from pandas import DataFrame, concat, merge
from sklearn.preprocessing import MinMaxScaler

from offline_results.common.config import CONFIG_HOMEPAGE_PAYTV, CONFIG_HOMEPAGE_NO_PAYTV
from offline_results.common.constants import HOMEPAGE_ID, CONTENT_ID, SEASONAL_MODULE_NAME, REC_TYPE, SCORE, CREATED_ON, \
    RECOMMENDATION_SCORE, RANK_SCORE, SCALED_DURATION, SCALED_VIEW_COUNT, DURATION, RECORDS, PAY_TV, MODEL_NAME, \
    IS_PAY_TV, VIEW_HISTORY, VIEW_COUNT
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class SeasonalModelUtils:
    @staticmethod
    @custom_exception()
    def get_data(obj):
        if len(obj.viewed_relation_history_df) != 0:
            return
        obj.viewed_relation_history_df = RecommendationUtils.user_viewed_data_from_s3()
        obj.live_tv_channel_paytv = RecommendationUtils.get_tv_channels(is_pay_tv=True)
        obj.live_tv_channel_nopaytv = RecommendationUtils.get_tv_channels(is_pay_tv=False)

    @staticmethod
    @custom_exception()
    def clear_data(obj):
        obj.viewed_relation_history_df = DataFrame()
        obj.live_tv_channel_paytv = []
        obj.live_tv_channel_nopaytv = []

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
        config_df = config_df[config_df[MODEL_NAME] == SEASONAL_MODULE_NAME.lower()]
        list_dedicated_homepage_id = config_df[HOMEPAGE_ID].tolist()
        df = df[df[HOMEPAGE_ID].isin(list_dedicated_homepage_id)].reset_index(drop=True)
        return df

    @staticmethod
    @custom_exception()
    def fetch_historical_data(obj, graph, user_label, homepage_id_wise):
        Logging.info("Fetch content-homepage_id mapping")
        content_homepage_id_mapping, content_homepage_df = RecommendationUtils.get_content_homepage_id_mapping(
            graph, user_label, homepage_id_wise)
        if not homepage_id_wise:
            content_homepage_df = content_homepage_df[
                ~content_homepage_df[CONTENT_ID].isin(
                    obj.live_tv_channel_paytv if user_label == PAY_TV else obj.live_tv_channel_nopaytv
                )
            ].reset_index(drop=True)
        Logging.info("Filter by dedicated homepage_id for Seasonal Model")
        content_homepage_df = SeasonalModelUtils.filter_by_dedicated_homepage_id(
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
            Logging.info(f'No active seasonal {user_label} homepage ID/Content ID found !!')
            return content_homepage_df, viewed_relation_history_df
        viewed_relation_history_df[VIEW_HISTORY] = viewed_relation_history_df[VIEW_HISTORY].apply(
            lambda x: literal_eval(str(x)))
        viewed_relation_history_df = viewed_relation_history_df.explode(VIEW_HISTORY)
        viewed_relation_history_df[DURATION] = viewed_relation_history_df[VIEW_HISTORY].apply(lambda x: x[DURATION])
        viewed_relation_history_df = viewed_relation_history_df[[CONTENT_ID, HOMEPAGE_ID, VIEW_COUNT, DURATION]]
        return content_homepage_df, viewed_relation_history_df

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
            seasonal_content_df = SeasonalModelUtils.final_result_df(rec_type, history_content_df=df,
                                                                     homepage_id_wise=True)
            homepage_seasonal_content_df = concat(
                [homepage_seasonal_content_df, seasonal_content_df], ignore_index=True
            )
        return homepage_seasonal_content_df
