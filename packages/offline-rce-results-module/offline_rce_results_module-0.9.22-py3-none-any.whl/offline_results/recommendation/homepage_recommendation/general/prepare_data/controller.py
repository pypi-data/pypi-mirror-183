from functools import reduce

from numpy import array
from pandas import DataFrame, merge
from sklearn.preprocessing import OneHotEncoder

from offline_results.common.config import (
    RATING_VALUES,
    FILENAME_VIDEO_MEASURE,
    CONTENT_VIEW_LOWER_THRESHOLD,
    CONTENT_VIEW_UPPER_THRESHOLD,
)
from offline_results.common.constants import (
    RATING,
    CATEGORY,
    CUSTOMER_ID,
    SUBCATEGORY,
    TAGS,
    CATEGORY_ID,
    CATEGORY_EN,
    SUBCATEGORY_ID,
    SUBCATEGORY_EN,
    TAGS_ID,
    TAGS_NAME,
    CONTENT_ID,
    INNER,
    COUNT,
)
from offline_results.recommendation.homepage_cluster_category.prepare_data.utils import (
    PrepareDataUtils,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception


class PrepareDataController(PrepareDataUtils):
    def __init__(
        self,
        connection_object,
        resource: object,
        bucket_name: str,
        object_name: str,
        keep_rating: bool = False,
        keep_category: bool = False,
        keep_subcategory: bool = False,
        keep_tags: bool = False,
    ):
        """
        Constructor to create instance member properties
        for s3 communication. The instance member properties
        also include boolean indicators of the features that
        shall be used subsequently by the recommendation model.
        @param connection_object: graphDB connection object
        @param resource: S3 resource object
        @param bucket_name: S3 bucket name
        @param object_name: S3 object name
        @param keep_rating: Boolean indicator for using rating
        @param keep_category: Boolean indicator for using category
        @param keep_subcategory: Boolean indicator for using subcategory
        @param keep_tags: Boolean indicator for using tags
        """
        PrepareDataUtils.__init__(
            self,
            connection_object=connection_object,
            resource=resource,
            bucket_name=bucket_name,
            object_name=object_name,
            keep_rating=keep_rating,
            keep_category=keep_category,
            keep_subcategory=keep_subcategory,
            keep_tags=keep_tags,
        )

    @class_custom_exception()
    def remove_upper_lower_threshold_contents(
        self, ubd_df: DataFrame, upper_threshold: int, lower_threshold: int
    ) -> DataFrame:
        """
        Filter out UBD data for content ids with very
        large or very few viewership records
        @param ubd_df: Dataframe object pandas
        @param upper_threshold: contents with total
        view-count beyond this limit are discarded
        @param lower_threshold: contents with total
        view-count below this limit are discarded
        @return:
        """

        # grouping contents to find their frequencies
        content_grouped_df = ubd_df.groupby(CONTENT_ID).size().reset_index()

        content_grouped_df.rename(columns={0: COUNT}, inplace=True)

        # computing contents that need to be removed from
        # further consideration

        # lower threshold
        contents_to_remove = content_grouped_df[
            content_grouped_df[COUNT] < lower_threshold
        ][CONTENT_ID].tolist()

        # upper threshold
        contents_to_remove.extend(
            content_grouped_df[content_grouped_df[COUNT] > upper_threshold][
                CONTENT_ID
            ].tolist()
        )

        # return filtered ubd records
        return ubd_df[~ubd_df[CONTENT_ID].isin(contents_to_remove)].reset_index(
            drop=True
        )

    @class_custom_exception()
    def fetch_and_format_ubd(self) -> DataFrame:
        """
        Fetches UBD video_measure.csv data from S3,
        filters out unwanted records after filtering
        @return: Dataframe object pandas
        """

        ubd = self.fetch_data(attribute=FILENAME_VIDEO_MEASURE)
        ubd = self.format_ubd(ubd)
        ubd = self.filter_duplicate_views(ubd_df=ubd)
        return self.remove_upper_lower_threshold_contents(
            ubd_df=ubd,
            lower_threshold=CONTENT_VIEW_LOWER_THRESHOLD,
            upper_threshold=CONTENT_VIEW_UPPER_THRESHOLD,
        )

    @class_custom_exception()
    def get_mapped_feature_preferences(self):
        """
        Driver function for generating Homepage Cluster
        Category recommendation model input data.
        Solo features are the features which do not have a separate
        collection in the V+ DB. These features include
        rating, attribute1 etc.
        @return: Dataframe object pandas
        """
        preference_attributes = []

        # prepare user-wise rating preferences
        # if rating is to be included
        if self.keep_rating:
            rating_preferences = self.get_preferences(
                attribute=RATING, solo_feature=True
            )
            preference_attributes.append(
                self.map_solo_feature_preferences(
                    data=rating_preferences,
                    preference_map=RATING_VALUES,
                    attribute=RATING,
                )
            )

        # prepare user-wise category preferences
        # if category is to be included
        if self.keep_category:
            category_names = RecommendationUtils.get_node_property_label_values(
                graph=self.graph, label=CATEGORY, property=CATEGORY_EN
            )
            enc = OneHotEncoder(handle_unknown="ignore")
            enc.fit(array(category_names).reshape(-1, 1))

            category_preferences = self.get_preferences(
                attribute=CATEGORY,
                solo_feature=False,
                label=CATEGORY,
                map_key=CATEGORY_ID,
                map_val=CATEGORY_EN,
            )

            category_preferences = self.get_one_hot_encodings(
                encoder=enc, preference_df=category_preferences, key=CATEGORY
            )

            preference_attributes.append(category_preferences)

        # prepare user-wise subcategory preferences
        # if subcategory is to be included
        if self.keep_subcategory:
            subcategory_names = RecommendationUtils.get_node_property_label_values(
                graph=self.graph, label=SUBCATEGORY, property=SUBCATEGORY_EN
            )
            enc = OneHotEncoder(handle_unknown="ignore")
            enc.fit(array(subcategory_names).reshape(-1, 1))

            subcategory_preferences = self.get_preferences(
                attribute=SUBCATEGORY,
                solo_feature=False,
                label=SUBCATEGORY,
                map_key=SUBCATEGORY_ID,
                map_val=SUBCATEGORY_EN,
            )

            subcategory_preferences = self.get_one_hot_encodings(
                encoder=enc, preference_df=subcategory_preferences, key=SUBCATEGORY
            )

            preference_attributes.append(subcategory_preferences)

        # prepare user-wise tags preferences
        # if tags is to be included
        if self.keep_tags:
            tag_names = RecommendationUtils.get_node_property_label_values(
                graph=self.graph, label=TAGS, property=TAGS_NAME
            )
            enc = OneHotEncoder(handle_unknown="ignore")
            enc.fit(array(tag_names).reshape(-1, 1))
            tag_preferences = self.get_preferences(
                attribute=TAGS,
                solo_feature=False,
                label=TAGS,
                map_key=TAGS_ID,
                map_val=TAGS_NAME,
            )

            tag_preferences = self.get_one_hot_encodings(
                encoder=enc, preference_df=tag_preferences, key=TAGS
            )

            preference_attributes.append(tag_preferences)

        # Merge results from the above preferences
        # set to True and return merged result
        return reduce(
            lambda l, r: merge(l, r, on=CUSTOMER_ID, how=INNER), preference_attributes
        )

    @class_custom_exception()
    def reshape_input_vectors(self, data: DataFrame, target_attribute: str):
        """
        Reshape input data by removing identifier
        attributes, redundant attributes.
        @param data: Dataframe object pandas
        @param target_attribute: Target attribute name
         in the dataframe feature set
        @return: DataFrame object pandas
        """
        vectorized_input = DataFrame()

        # get the dependant variable values
        vectorized_input["Y"] = data[target_attribute]

        if CUSTOMER_ID in data.columns:
            data = data.drop(columns=[CUSTOMER_ID])

        if target_attribute in data.columns:
            data = data.drop(columns=[target_attribute])

        # get the independent variable values
        vectorized_input["X"] = self.get_merged_vectorized_input(data=data)

        return vectorized_input

    @class_custom_exception()
    def controller(self):
        """
        Driver function to retrieve preference data, map the
        preferences to the corresponding values, and generate
        one-hot preference encoding
        @return: Dataframe object pandas
        """
        preferences = self.get_mapped_feature_preferences()

        preferences[CUSTOMER_ID] = preferences[CUSTOMER_ID].astype(str)

        ubd = self.fetch_and_format_ubd()

        input_data = merge(preferences, ubd, on=CUSTOMER_ID, how=INNER)

        return self.reshape_input_vectors(data=input_data, target_attribute=CONTENT_ID)
