import ast
from pandas import merge
import pandas as pd
from pandas import concat, DataFrame
from sklearn.preprocessing import MinMaxScaler
from offline_results.common.constants import CONTENT_ID, VIEW_COUNT, CUSTOMER_ID, SCORE, VIEW_HISTORY, DURATION
from offline_results.recommendation.homepage_recommendation.core.with_cf_user_to_user.utils import (
    UserViewershipUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception


class UserViewershipController(UserViewershipUtils):

    @class_custom_exception()
    def calculate_total_duration(self, viewership):
        view_history = viewership[VIEW_HISTORY].tolist()
        view_history2 = [ast.literal_eval(str(i)) for i in view_history]
        temp_df = pd.DataFrame({
            CONTENT_ID: viewership[CONTENT_ID].tolist(),
            VIEW_HISTORY: view_history2
        })
        temp_df = temp_df.explode(column=VIEW_HISTORY)
        temp_df[DURATION] = temp_df[VIEW_HISTORY].apply(lambda x: x[DURATION])
        content_duration_counts = temp_df.groupby(CONTENT_ID)[DURATION].sum().reset_index()

        return content_duration_counts

    @class_custom_exception()
    def controller(self, content_list, similar_users, is_paytv=True, viewed_data=None):
        # viewership = self.content_viewership(content_list=content_list, is_pay_tv=is_paytv)
        viewership = viewed_data[viewed_data[CONTENT_ID].isin(content_list)]
        viewership = viewership[viewership[CUSTOMER_ID].isin(similar_users)]
        content_duration_counts = self.calculate_total_duration(viewership)
        if viewership is None:
            viewership = self.content_viewership(
                content_list=content_list, is_pay_tv=is_paytv
            )
        if viewership is None or len(viewership) == 0:
            return DataFrame({CONTENT_ID: [], SCORE: []})

        viewership[VIEW_COUNT] = viewership[VIEW_COUNT].fillna(0)
        max_view_count = viewership[VIEW_COUNT].max()
        filtered_viewership = viewership[
            viewership[CUSTOMER_ID].isin(similar_users)
        ].copy()
        filtered_viewership[VIEW_COUNT] = filtered_viewership[VIEW_COUNT] + max_view_count
        viewership = viewership.drop(index=filtered_viewership.index)
        viewership = concat([filtered_viewership, viewership], axis=0).reset_index(
            drop=True
        )
        content_score_counts = viewership.groupby(CONTENT_ID)[VIEW_COUNT].sum().reset_index()
        content_score_counts = merge(
            content_score_counts, content_duration_counts, on=CONTENT_ID, how="left"
        ).reset_index(drop=True)
        content_score_counts[SCORE] = (content_score_counts[VIEW_COUNT] * 0.5) + (content_score_counts[DURATION] * 0.5)
        content_score_counts = RecommendationUtils.round_score(content_score_counts)
        content_score_counts[SCORE] = (
            1 if content_score_counts[SCORE].max() == 0.001 else content_score_counts[SCORE]
        )

        return content_score_counts[[CONTENT_ID, SCORE, DURATION]]
