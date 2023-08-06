import ast
from collections import Counter
from datetime import datetime, timedelta

import numpy as np
from graphdb.graph import GraphDb
from pandas import DataFrame, to_datetime, qcut, cut

from offline_results.common.constants import (
    VIEW_COUNT,
    VIEW_HISTORY,
    CUSTOMER_ID,
    CONTENT_ID,
    CREATED_ON,
    RECENCY,
    LAST_VIEWED,
    USER_RECENCY,
    UNIQUE_USERS_COUNT,
    DURATION,
    bin_features,
    LABEL,
    R_SCORE,
    D_SCORE,
    V_SCORE,
    RATINGS,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception

connection_uri_local = "ws://localhost:8182/gremlin"

DURATION_WEIGHT = 5
VIEW_WEIGHT = 2
UNIQUE_WEIGHT = 1
RECENCY_WEIGHT = 1


class PersonalisedRanker:
    def __init__(self, connection_object):
        """
        Constructor to create graph object using
        the input connection details
        :param connection_object: graph
        connection object
        """
        self.graph = GraphDb.from_connection(connection_object)
        self.data = self.extract_feature()

    @class_custom_exception()
    def extract_feature(self) -> DataFrame:
        """
        Extract viewed features from the response dataframe.
        """
        viewed_content = RecommendationUtils.get_viewed_features(self.graph)
        viewed_content[VIEW_HISTORY] = viewed_content[VIEW_HISTORY].apply(
            ast.literal_eval
        )
        result = []
        for idx, row in viewed_content.iterrows():
            for dct in row[VIEW_HISTORY]:
                dct[CUSTOMER_ID] = row[CUSTOMER_ID]
                dct[CONTENT_ID] = row[CONTENT_ID]
                dct[VIEW_COUNT] = row[VIEW_COUNT]
                result.append(dct)

        result = DataFrame(result)
        return result

    @class_custom_exception()
    def calculate_overall_recency(
        self,
    ) -> DataFrame:
        """
        Find content last viewed date.
        """

        data = self.data

        data[CREATED_ON] = to_datetime(data[CREATED_ON], format="%Y/%m/%d")
        data = data[[CONTENT_ID, CREATED_ON]]
        idx = data.groupby(CONTENT_ID)[CREATED_ON].idxmax()
        data = data.loc[idx]
        data[RECENCY] = data[CREATED_ON] + timedelta(days=1)
        data[RECENCY] = (datetime.utcnow() - data[RECENCY]).dt.days
        data = data[[CONTENT_ID, RECENCY]]

        return data.reset_index(drop=True)

    @class_custom_exception()
    def calculate_user_wise_recency(self):
        """
        Calculates the user-wise recency of each content
        """

        data = self.data
        data[CREATED_ON] = to_datetime(data[CREATED_ON], format="%Y/%m/%d")
        df_recency = data.groupby(by=CUSTOMER_ID, as_index=False)[
            CONTENT_ID, CREATED_ON
        ].max()
        df_recency.columns = [CUSTOMER_ID, CONTENT_ID, LAST_VIEWED]

        recent_date = df_recency[LAST_VIEWED].max()
        df_recency[USER_RECENCY] = df_recency[LAST_VIEWED].apply(
            lambda x: (recent_date - x).days
        )

        return df_recency.drop(columns=[CUSTOMER_ID, LAST_VIEWED])

    @class_custom_exception()
    def prepare_features(self) -> DataFrame:
        """
        Prepare required features by summing
        """

        data = self.data
        data = data.drop(columns=[CREATED_ON, CUSTOMER_ID])
        data = data.groupby([CONTENT_ID]).sum().reset_index()

        return data

    @class_custom_exception()
    def get_unique_users_count(self) -> DataFrame:
        """
        Get count of unique users for each content.
        """

        unique_users = self.data
        unique_users = unique_users.drop_duplicates(
            subset=[CUSTOMER_ID, CONTENT_ID]
        ).reset_index(drop=True)
        users_counter = dict(Counter(unique_users[CONTENT_ID]))
        users_count = DataFrame()
        users_count[CONTENT_ID] = users_counter.keys()
        users_count[UNIQUE_USERS_COUNT] = users_counter.values()

        return users_count

    @class_custom_exception()
    def merge_features(self) -> DataFrame:
        """
        Merge all the required features in single dataframe
        """

        features = self.prepare_features()
        recency = self.calculate_overall_recency()
        unique = self.get_unique_users_count()

        data = features.merge(recency, on=CONTENT_ID)
        data = data.merge(unique, on=CONTENT_ID)

        return data

    @class_custom_exception()
    def content_lifetime(self) -> DataFrame:
        """
        Calculate content lifetime which is date of
        content last viewed with duration greater
        than zero minus first viewed with duration
        greater than zero.
        """
        data = self.data
        data = data.loc[:, [CONTENT_ID, DURATION, CREATED_ON]]
        data[CREATED_ON] = to_datetime(data[CREATED_ON], format="%Y/%m/%d")
        data = data[data[DURATION] != 0]
        df = data.groupby(CONTENT_ID, as_index=False)[DURATION, CREATED_ON].min()
        df = df.rename(
            {CREATED_ON: "first_view_with_duration", DURATION: "duration_first"}, axis=1
        )
        # df = df.drop(columns='duration')
        df1 = data.groupby(CONTENT_ID, as_index=False)[DURATION, CREATED_ON].max()
        df1 = df1.rename(
            {CREATED_ON: "last_view_with_duration", DURATION: "duration_last"}, axis=1
        )
        # df1 = df1.drop(columns='duration')
        new_df = df.merge(df1, on=CONTENT_ID, how="outer", indicator=True)
        new_df["content_lifetime"] = (
            new_df["last_view_with_duration"] - new_df["first_view_with_duration"]
        ).dt.days
        new_df = new_df[[CONTENT_ID, "content_lifetime"]]

        return new_df

    @class_custom_exception()
    def calculate_bins(self, data) -> DataFrame:
        """
        Calculate bins for features required
        """

        for feature, score in bin_features.items():

            if feature == RECENCY:
                label = [4, 3, 2, 1]
            else:
                label = [1, 2, 3, 4]

            data[score] = cut(
                data[feature],
                bins=[
                    -1,
                    np.percentile(data[feature], 25),
                    np.percentile(data[feature], 50),
                    np.percentile(data[feature], 75),
                    data[feature].max(),
                ],
                labels=label,
            ).astype("int")
        return data

    @class_custom_exception()
    def generate_ratings(self) -> DataFrame:
        """
        Generate final ratings for each viewed content
        """
        data = self.merge_features()
        data = self.calculate_bins(data)
        data[LABEL] = 0.15 * data[R_SCORE] + 0.25 * data[D_SCORE] + 0.15 * data[V_SCORE]

        data[RATINGS] = qcut(data[LABEL], 5, labels=[1, 2, 3, 4, 5])

        return data

    @class_custom_exception()
    def ranking_controller(
        self,
    ) -> DataFrame:
        """
        Driver function for Class PersonalisedRanker
        """

        data = self.generate_ratings()

        return data
