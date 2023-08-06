from functools import reduce

from pandas import DataFrame, merge

from offline_results.common.config import (
    RATING_VALUES,
    FILENAME_VIDEO_MEASURE,
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
    HOMEPAGE_ID,
    INNER,
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
    def fetch_and_format_ubd(self) -> DataFrame:
        """
        Fetches UBD video_measure.csv data from S3,
        filters out unwanted attributes and returns
        homepage id for all the content listed in
        UBD dataframe object pandas
        @return: Dataframe object pandas
        """

        ubd = self.fetch_data(attribute=FILENAME_VIDEO_MEASURE)
        ubd = self.format_ubd(ubd)

        content_homepage_mapping = DataFrame(
            RecommendationUtils.get_homepage_for_contents(graph=self.graph)
        )

        homepage_title_map = DataFrame(
            RecommendationUtils.get_homepage_id_title_map(graph=self.graph)
        )

        homepage_title_map = self.map_same_title_homepages(
            homepage_title_map=homepage_title_map
        )

        content_homepage_mapping["homepage_id"] = [
            homepage_title_map[homepage_id]
            for homepage_id in content_homepage_mapping["homepage_id"]
        ]

        ubd = merge(
            ubd, content_homepage_mapping, on=CONTENT_ID, how=INNER
        ).reset_index(drop=True)

        filtered_ubd_df = self.filter_ubd_views(ubd, homepage_title_map)

        return filtered_ubd_df

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
            preference_attributes.append(
                self.get_preferences(
                    attribute=CATEGORY,
                    solo_feature=False,
                    label=CATEGORY,
                    map_key=CATEGORY_ID,
                    map_val=CATEGORY_EN,
                )
            )

        # prepare user-wise subcategory preferences
        # if subcategory is to be included
        if self.keep_subcategory:
            preference_attributes.append(
                self.get_preferences(
                    attribute=SUBCATEGORY,
                    solo_feature=False,
                    label=SUBCATEGORY,
                    map_key=SUBCATEGORY_ID,
                    map_val=SUBCATEGORY_EN,
                )
            )

        # prepare user-wise tags preferences
        # if tags is to be included
        if self.keep_tags:
            preference_attributes.append(
                self.get_preferences(
                    attribute=TAGS,
                    solo_feature=False,
                    label=TAGS,
                    map_key=TAGS_ID,
                    map_val=TAGS_NAME,
                )
            )

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

        if CONTENT_ID in data.columns:
            data = data.drop(columns=[CONTENT_ID])

        # get the independent variable values
        vectorized_input["X"] = self.get_merged_vectorized_input(data=data)

        return vectorized_input

    @class_custom_exception()
    def controller(self):
        """
        Driver function to retrieve preference data, map the
        preferences to the corresponding values, adn generate
        vector representation using BERT pre-trained
        language model
        @return: Dataframe object pandas
        """
        preferences = self.get_mapped_feature_preferences()

        preferences[CUSTOMER_ID] = preferences[CUSTOMER_ID].astype(str)

        ubd = self.fetch_and_format_ubd()

        input_data = merge(preferences, ubd, on=CUSTOMER_ID, how=INNER)

        return self.reshape_input_vectors(data=input_data, target_attribute=HOMEPAGE_ID)
