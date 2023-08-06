import logging

from pandas import DataFrame
from offline_results.common.constants import CONTENT_ID, VIEW_COUNT, SCORE, PAY_TV
from offline_results.utils import class_custom_exception


class CFItemtoItem:
    @class_custom_exception()
    def most_viwed_content(self, df: DataFrame, pay_tv_label, live_tv_channel_paytv, live_tv_channel_nopaytv,
                           homepage_id_wise):
        try:
            if not homepage_id_wise:
                df = df[~df[CONTENT_ID].isin(live_tv_channel_paytv if pay_tv_label == PAY_TV else live_tv_channel_nopaytv)]
            df = df.groupby([CONTENT_ID])[VIEW_COUNT].sum().reset_index()
            df = df[df[VIEW_COUNT] == df[VIEW_COUNT].max()].reset_index(drop=True)
            most_viewed_content = df.iloc[0][CONTENT_ID]
            return most_viewed_content
        except Exception as e:
            logging.error(f"error while calling most_vied_content, Error {e}")

    @class_custom_exception()
    def similar_contents(self, content_id, content_similarity):
        data = content_similarity.get(content_id, {})
        if len(data) == 0:
            return DataFrame(columns=[CONTENT_ID, SCORE])
        data = DataFrame(
            {CONTENT_ID: data.keys(), SCORE: data.values()}, columns=[CONTENT_ID, SCORE]
        )
        return data

    @class_custom_exception()
    def generate_rec(
        self, ubd, content_similarity, content_list, default_wise,
            pay_tv_label, live_tv_channel_paytv, live_tv_channel_nopaytv, homepage_id_wise
    ):
        if len(ubd) == 0 or len(content_list) == 0:
            return DataFrame(columns=[CONTENT_ID, SCORE])
        most_viewed_content_id = self.most_viwed_content(ubd, pay_tv_label,
                                                         live_tv_channel_paytv, live_tv_channel_nopaytv,
                                                         homepage_id_wise)
        result = self.similar_contents(most_viewed_content_id, content_similarity)
        result = result[result[CONTENT_ID].isin(content_list)]
        if not default_wise:
            mean_threshold = result[SCORE].mean()
            result = result[result[SCORE] >= mean_threshold]
        return DataFrame(columns=[CONTENT_ID, SCORE]) if len(result) == 0 else result
