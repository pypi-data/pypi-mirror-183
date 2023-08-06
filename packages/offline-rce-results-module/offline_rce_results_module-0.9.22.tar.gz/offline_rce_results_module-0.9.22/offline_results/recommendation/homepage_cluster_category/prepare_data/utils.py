from collections import Counter

from graphdb.graph import GraphDb
from numpy import array, zeros, mean, concatenate
from pandas import DataFrame, merge
from tqdm import tqdm

from offline_results.common.config import (
    DISCARD_ATTRIBUTES,
    OUTLIERS_HOMEPAGE_ID,
    OUTLIERS_CUSTOMER,
    DUPLICATE_VIEWS_CAP,
    DEFAULT_HOMEPAGE_ID,
    LOWER_FREQ_HOMEPAGE_ID_CUTOFF,
    ZERO_VECTOR_DIMENSION,
)
from offline_results.common.constants import (
    CSV_EXTENSION,
    CUSTOMER_ID,
    VIDEO_ID1,
    CONTENT_ID,
    HOMEPAGE_ID,
    COUNT,
    HOMEPAGE_TITLE_EN,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception, Logging


class PrepareDataUtils:
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
        self.graph = GraphDb.from_connection(connection_object)
        self.resource = resource
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.keep_rating = keep_rating
        self.keep_category = keep_category
        self.keep_subcategory = keep_subcategory
        self.keep_tags = keep_tags

    @class_custom_exception()
    def fetch_data(self, attribute: str):
        """
        To retrieve preference information for a specified attribute.
        This information can either be retrieved from S3 or
        alternatively, directly from the graphDB
        @param attribute: the preference attribute for which the
        information needs to be retrieved.
        @return: Attribute preference dataframe object pandas
        """

        return ConnectS3().read_csv_from_s3(
            bucket_name=self.bucket_name,
            object_name=self.object_name + attribute + CSV_EXTENSION,
            resource=self.resource,
        )

    @class_custom_exception()
    def format_ubd(self, ubd):
        """
        Basic formatting of attributes in UBD
        @param ubd: Dataframe object pandas
        @return: dataframe object pandas
        """
        ubd = ubd[[CUSTOMER_ID, VIDEO_ID1]]
        ubd[CUSTOMER_ID] = ubd[CUSTOMER_ID].astype(str)
        ubd = ubd.rename(columns={VIDEO_ID1: CONTENT_ID})
        return ubd

    @class_custom_exception()
    def filter_outliers(self, ubd_df: DataFrame, homepage_title_map: dict) -> DataFrame:
        """
        Filter out the records with users from the outlier
        set and homepage id from the outlier set
        @param ubd_df: Dataframe object pandas
        @param homepage_title_map: dictionary mapping
        @return: Filtered dataframe object pandas
        """
        outliers = list(
            set([homepage_title_map[outlier] for outlier in OUTLIERS_HOMEPAGE_ID])
        )

        ubd_df = ubd_df.loc[
            (~ubd_df[HOMEPAGE_ID].isin(outliers))
            & (~(ubd_df[CUSTOMER_ID].isin(OUTLIERS_CUSTOMER)))
        ]

        return ubd_df.reset_index(drop=True)

    @class_custom_exception()
    def get_filtered_duplicate_views_df(
        self, duplicate_views_df: DataFrame, ubd_df: DataFrame
    ) -> DataFrame:
        """
        Prepare filtered df with removed duplicate
        views up to the specified upper cap
        @param duplicate_views_df: Dataframe object pandas
        @param ubd_df: Dataframe object pandas
        @return: Dataframe object pandas
        """
        filtered_df = merge(duplicate_views_df, ubd_df, on=[CUSTOMER_ID, CONTENT_ID])

        filtered_df = filtered_df[
            filtered_df.groupby([CUSTOMER_ID, CONTENT_ID]).customer_id.transform(COUNT)
            <= DUPLICATE_VIEWS_CAP
        ]

        return filtered_df

    @class_custom_exception()
    def filter_duplicate_views(self, ubd_df: DataFrame) -> DataFrame:
        """
        Apply an upper cap to duplicate user-content
        view records up to a specified limit
        @param ubd_df: Dataframe object pandas
        @return: Dataframe object pandas
        """
        duplicate_views_df = ubd_df.groupby([CUSTOMER_ID, CONTENT_ID]).size()

        duplicate_views_df = DataFrame(duplicate_views_df, columns=[COUNT])

        for idx, val in duplicate_views_df.iterrows():
            if val[COUNT] <= DUPLICATE_VIEWS_CAP:
                val[COUNT] = val[COUNT]
            else:
                val[COUNT] = DUPLICATE_VIEWS_CAP

        filtered_df = self.get_filtered_duplicate_views_df(
            duplicate_views_df=duplicate_views_df, ubd_df=ubd_df
        )

        final_df = filtered_df.drop(COUNT, axis=1)
        return final_df.reset_index(drop=True)

    @class_custom_exception()
    def lower_freq_homepage_id_cutoff(
        self, ubd_df: DataFrame, cutoff_value: int
    ) -> DataFrame:
        """
        Group lower frequency homepage records under a
        single homepage category
        @param ubd_df: Dataframe object pandas
        @param cutoff_value: integer threshold. The
        frequencies below this threshold shall be grouped together
        @return: Dataframe object pandas
        """
        homepage_id_counts = dict(Counter(ubd_df[HOMEPAGE_ID]))
        valid_id, invalid_id = [], []

        for homepage_id in homepage_id_counts:
            valid_id.append(homepage_id) if homepage_id_counts[
                homepage_id
            ] > cutoff_value else invalid_id.append(homepage_id)

        # replace low frequency homepage ids with the default label
        ubd_df[HOMEPAGE_ID] = ubd_df[HOMEPAGE_ID].replace(
            invalid_id, DEFAULT_HOMEPAGE_ID
        )

        return ubd_df.reset_index(drop=True)

    @class_custom_exception()
    def filter_ubd_views(self, ubd: DataFrame, homepage_title_map: dict) -> DataFrame:
        """
        Apply multiple filtration over UBD records
        @param ubd: Dataframe object pandas
        @param homepage_title_map: dictionary mapping
        @return: Dataframe object pandas
        """
        homepage_id_filtered_ubd = self.filter_outliers(ubd, homepage_title_map)

        ubd_after_duplicate_views_removal = self.filter_duplicate_views(
            ubd_df=homepage_id_filtered_ubd
        )
        filtered_ubd_df = self.lower_freq_homepage_id_cutoff(
            ubd_df=ubd_after_duplicate_views_removal,
            cutoff_value=LOWER_FREQ_HOMEPAGE_ID_CUTOFF,
        )
        return filtered_ubd_df

    @class_custom_exception()
    def format_preferences(
        self, data: DataFrame, data_key: str, attribute: str, solo_feature: bool = False
    ) -> DataFrame:
        """
        For the preference information related to the specified
        attribute, format the layout of the dataframe object by
        replacing 1's with corresponding preference value string.
        Since for the solo features such as rating and attribute1,
        there is no particular identifier, their values need not
        be type casted. This condition is captured using the solo_
        feature flag.
        @param data: Dataframe object pandas
        @param data_key: The key attribute in data variable. This
        attribute used to generate the final result returned
        by the function.
        @param attribute: String value for the preference attribute.
        @param solo_feature: Boolean indicator. When preparing the
        result, if solo_feature is set to True, the values are not
        type casted to corresponding integers.
        @return: Formatted dataframe object pandas with preferences
        within a single dataframe column.
        """
        formatted_preferences = DataFrame()
        formatted_preferences[data_key] = data[data_key]
        data = data.drop(columns=[data_key])

        # Since the key column has been dropped from the
        # 'data' variable, all the columns currently in this
        # dataframe are preference attributes. Thus, iterating
        # through each attribute to reformat the preferences.

        for feature in data.columns:
            Logging.info("Formatting the feature " + feature)
            feature_val = feature.split("_")[-1]

            if not solo_feature and feature_val not in DISCARD_ATTRIBUTES:
                feature_val = int(feature_val)

            data[feature] = [feature_val if val == 1 else 0 for val in data[feature]]

        # Merging all the formatted attribute preferences under a
        # single dataframe column in the result

        formatted_preferences[attribute] = data[data.columns].apply(list, axis=1)

        # Remove all the preference values that are either 0 or nan.
        # These values do not contribute to the preferences of
        # a given user

        formatted_preferences[attribute] = [
            list(filter(lambda val: val not in DISCARD_ATTRIBUTES, preferences))
            for preferences in formatted_preferences[attribute]
        ]

        return formatted_preferences

    @class_custom_exception()
    def map_static_preferences(
        self,
        data: DataFrame,
        preference_map: DataFrame,
        map_key: str,
        map_val: str,
        attribute: str,
    ):
        """
        To map preference attributes whose static nodes
        have been dumped into graphDB. The function
        queries the graphDB to retrieve all nodes of
        specified attribute node label and returns the
        key-value pair for the requested property.
        @param data: Dataframe object pandas
        @param preference_map: Dataframe object pandas
        @param map_key: The attribute to be considered
        as the key in preference_map
        @param map_val: The attribute to be considered
        as the value map to the key in the preference_map
        @param attribute: Attribute value to be considered
        @return: Dataframe object pandas mapped for the
        specified attribute
        """
        record_count = len(data)

        for index in range(record_count):
            Logging.info("Working on " + attribute + " record " + str(index))

            preferences = data.loc[index, attribute]

            preferences = preference_map[
                preference_map[map_key].isin(preferences)
            ].reset_index(drop=True)

            data.at[index, attribute] = preferences[map_val].tolist()

        return data

    @class_custom_exception()
    def map_solo_feature_preferences(
        self, data: DataFrame, preference_map: list, attribute: str
    ) -> DataFrame:
        """
        To map preference attributes whose static nodes
        have NOT been dumped into graphDB. The function
        uses the pre-defined config mappings to retrieve
        all possible values of the specified attribute
        and returns the vectorised form for the
        requested property.
        @param data: Dataframe object pandas
        @param preference_map: list of possible values
        for the specified attribute
        @param attribute: Attribute value to be considered
        @return:  Dataframe object pandas vectorized for the
        specified attribute
        """
        for index in range(len(data)):
            Logging.info("Working on " + attribute + " record " + str(index))

            feature_preference = data.loc[index, attribute]

            data.at[index, attribute] = array(
                [
                    1 if preference.upper() in feature_preference else 0
                    for preference in preference_map
                ]
            )

        return data

    @class_custom_exception()
    def get_preferences(
        self,
        attribute: str,
        label: str = None,
        map_key: str = None,
        map_val: str = None,
        solo_feature: bool = False,
    ) -> DataFrame:
        """
        Fetch and format the preferences for a given attribute.
        @param attribute: Value string for an attribute
        @param label: Node label to search for in graphDB for
        preparing the preference key-value mappings
        @param map_key: Key node property to look for in graphDB
        @param map_val: Value node property to look for in graphDB
        @param solo_feature: Boolean indicator. Used during
        the formatting of the result.
        @return: Dataframe object pandas with formatted
        preference credentials
        """
        Logging.info("Fetching preferences data for" + attribute)
        preference_data = self.fetch_data(attribute=attribute)

        Logging.info("Formatting preference attributes....")
        formatted_preferences = self.format_preferences(
            data=preference_data,
            data_key=CUSTOMER_ID,
            attribute=attribute,
            solo_feature=solo_feature,
        )

        # if the feature under consideration does not
        # have any independent static nodes in the graphDB,
        # return the result at this stage. The further
        # procedure shall be vectorization of values
        # under this feature.
        if label is None:
            return formatted_preferences

        preference_map = RecommendationUtils.get_attribute_map(
            graph=self.graph,
            node_label=label,
            key_node_property=map_key,
            value_node_property=map_val,
        )

        return self.map_static_preferences(
            data=formatted_preferences,
            preference_map=DataFrame(preference_map[0]),
            map_key=map_key,
            map_val=map_val,
            attribute=attribute,
        )

    @class_custom_exception()
    def map_embeddings_to_attributes(self, embeddings_map: dict, attributes: list):
        """
        Uses the embeddings map to obtain user preference embeddings
        @param embeddings_map: dictionary mapping
        @param attributes: list of preferences
        @return: numpy array object of embeddings
        """
        if len(attributes) == 0:
            return zeros((ZERO_VECTOR_DIMENSION,), dtype=float)

        print("Generating embeddings for attributes: ", attributes)
        embeddings_from_map = []
        for attribute in attributes:
            embeddings_from_map.append(embeddings_map[attribute])

        return mean(embeddings_from_map, axis=0)

    @class_custom_exception()
    def get_unique_preference_attributes(
        self, feature_preferences: DataFrame, preference: str
    ):
        """
        For a given attribute type, retrieve the set of
        unique values
        @param feature_preferences: Dataframe object pandas
        @param preference: string value
        @return: list of unique preferences
        """
        all_attributes = feature_preferences[preference].tolist()
        all_attributes_flatten = [
            attribute for attributes in all_attributes for attribute in attributes
        ]
        unique_attributes = list(set(all_attributes_flatten))
        return unique_attributes

    @class_custom_exception()
    def get_merged_vectorized_input(self, data: DataFrame) -> list:
        """
        Merge embeddings from all the feature preference
        vectors into a single attribute.
        @param data: Dataframe object pandas
        @return: list of merged preference embeddings
        """
        input_vectors = []

        Logging.info("Merging all features into " + "a single feature embedding")
        for index in tqdm(range(len(data))):
            feature_vector = data.loc[index, :].values.tolist()
            input_vectors.append(concatenate(feature_vector).ravel())

        return input_vectors

    @class_custom_exception()
    def process_homepage_title(self, homepage_title_map: DataFrame) -> DataFrame:
        """
        Preprocess homepage title attribute to remove
        whitespace characters and unify the case
        throughout the values
        @param homepage_title_map: Dataframe object pandas
        @return: Dataframe object pandas
        """
        homepage_title_map[HOMEPAGE_TITLE_EN] = homepage_title_map[
            HOMEPAGE_TITLE_EN
        ].str.lower()

        homepage_title_map[HOMEPAGE_TITLE_EN] = homepage_title_map[
            HOMEPAGE_TITLE_EN
        ].str.replace(" ", "")

        return homepage_title_map

    @class_custom_exception()
    def get_one_hot_encodings(self, encoder, preference_df, key: str):
        for index in range(len(preference_df)):
            Logging.info("One-hot encoding index " + str(index))
            encoding = encoder.transform(
                array(list(set(preference_df.loc[index, key]))).reshape(-1, 1)
            ).toarray()
            encoding = encoding.sum(axis=0).tolist()
            preference_df.at[index, key] = list(map(int, encoding))

        return preference_df

    @class_custom_exception()
    def map_same_title_homepages(self, homepage_title_map: DataFrame) -> dict:
        """
        Map all homepage ids with the same titles
        to a single label.
        @param homepage_title_map: Dataframe object pandas
        @return: dictionary mapping
        """
        homepage_title_map = self.process_homepage_title(homepage_title_map)

        title_indices = {
            k: v for v, k in enumerate(list(set(homepage_title_map[HOMEPAGE_TITLE_EN])))
        }

        homepage_title_map[HOMEPAGE_TITLE_EN] = [
            title_indices[homepage_title]
            for homepage_title in homepage_title_map[HOMEPAGE_TITLE_EN]
        ]

        return dict(
            zip(homepage_title_map[HOMEPAGE_ID], homepage_title_map[HOMEPAGE_TITLE_EN])
        )
