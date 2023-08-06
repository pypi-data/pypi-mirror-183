from pandas import DataFrame, merge

from offline_results.common.config import DURATION_BINS, TOD_MAPPING
from offline_results.common.constants import (
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    CUSTOMER_ID,
    VIDEO_ID1,
    CONTENT_ID,
    DURATION,
    CONTENT_DURATION,
    TOD,
    CREATED_ON,
)
from offline_results.preferences.generate_preferences import PreferenceGenerator
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception


class UserViewTimePreferences:
    @staticmethod
    @custom_exception()
    def get_content_durations() -> DataFrame:
        """
        For all the contents dumped into graphDB, identify their
        respective content durations and return the response
        as a dataframe object
        :param graph: graphDB object
        :return: Dataframe object pandas
        """
        graph = ANGraphDb.new_connection_config().graph
        response = []
        for content_type in [PAY_TV_CONTENT, NO_PAY_TV_CONTENT]:
            try:
                subresponse = graph.custom_query(
                    query=f"""g.V().hasLabel('{content_type}').match(
                            __.as("c").values("content_id").as("content_id"),
                            __.as("c").values("duration_minute").as("content_duration")
                            ).select("content_id", "content_duration")""",
                    payload={
                        content_type: content_type,
                    },
                )
                # flattening the response obtained
                response.extend(
                    [item for temp_response in subresponse for item in temp_response]
                )
            except Exception as e:
                print("Unable to fetch response from graphdb")
        graph.connection.close()

        return DataFrame(response)

    @staticmethod
    @custom_exception()
    def get_closest_bin(value: int, bins: list):
        """
        Identify the closest bin to which a value belongs
        :param value: value to be assigned to a bin
        :param bins: list of different bin values
        :return: bin value to which the input should be assigned
        """
        result = [abs(bin_val - value) for bin_val in bins]
        return bins[result.index(min(result))]

    @staticmethod
    @custom_exception()
    def perform_duration_binning(duration_df: DataFrame):
        """
        For each value in the content-duration mapping,
        substitute the corresponding bin value
        :param duration_df: Dataframe object pandas
        :return: Dataframe object pandas
        """
        duration_bins = DURATION_BINS
        duration_df[CONTENT_DURATION] = [
            UserViewTimePreferences.get_closest_bin(value=duration, bins=duration_bins)
            for duration in duration_df[CONTENT_DURATION]
        ]
        return duration_df

    @staticmethod
    @custom_exception()
    def fetch_time_of_day(content_viewed_tod: DataFrame, ubd: DataFrame) -> DataFrame:
        """
        Fetch TOD from created on
        :param content_viewed_tod: Dataframe object pandas
        :param ubd: Dataframe object pandas
        :return: Dataframe object pandas
        """
        content_viewed_tod[TOD] = (ubd[CREATED_ON].dt.hour % 24 + 6) // 6
        return content_viewed_tod

    @staticmethod
    @custom_exception()
    def get_content_view_tod(ubd: DataFrame) -> DataFrame:
        """
        Identify the time of day as per the input
        timestamps in the ubd data
        :param ubd: Dataframe object pandas
        :return: Dataframe object pandas
        """
        content_viewed_tod = DataFrame()
        content_viewed_tod[CUSTOMER_ID] = ubd[CUSTOMER_ID]
        content_viewed_tod[DURATION] = ubd[DURATION]
        content_viewed_tod = UserViewTimePreferences.fetch_time_of_day(
            content_viewed_tod, ubd
        )
        content_viewed_tod[TOD].replace(TOD_MAPPING, inplace=True)
        return content_viewed_tod

    @staticmethod
    @custom_exception()
    def get_viewtime_preferences(ubd: DataFrame):
        """
        Obtain user-wise time of day and content duration preferences
        based on the log from the UBD Data. This function internally
        utilises the same preference methods as used to generate the
        category, subcategory, actor preferences etc.
        :param ubd: Dataframe object pandas
        :param graph: graphDB connection object
        :return: Dataframe objects pandas
        """
        # preparing content duration input data for preference generation
        content_durations = UserViewTimePreferences.get_content_durations()

        binned_content_durations = UserViewTimePreferences.perform_duration_binning(
            content_durations.copy()
        )

        merged_ubd_content_duration = merge(
            ubd[[CUSTOMER_ID, VIDEO_ID1, DURATION]],
            binned_content_durations,
            left_on=VIDEO_ID1,
            right_on=CONTENT_ID,
            how="inner",
        )
        merged_ubd_content_duration.drop(columns=[CONTENT_ID], inplace=True)

        # preparing content view tod input data for preference generation
        content_view_tod = UserViewTimePreferences.get_content_view_tod(ubd=ubd)

        # generating preferences
        preference = PreferenceGenerator(feature=TOD, feature_cutoff=2, user_cutoff=2)
        tod_preferences = preference.controller(data=content_view_tod)
        preference = PreferenceGenerator(
            feature=CONTENT_DURATION, feature_cutoff=2, user_cutoff=2
        )
        content_duration_preferences = preference.controller(
            data=merged_ubd_content_duration
        )

        return tod_preferences, content_duration_preferences
