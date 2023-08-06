from pandas import DataFrame

from offline_results.common.constants import (
    CUSTOMER_ID,
    DURATION,
    ATTRIBUTE1,
    VOD,
    CHANNEL_LIVE,
    CATCHUP,
    DEFAULT_FEATURE_VALUES,
)
from offline_results.common.constants import (
    WHITESPACE_REGEX,
    SINGLE_SPACE,
    ABSURD_VALUE,
)
from offline_results.utils import class_custom_exception, custom_exception


class PreprocessBehaviour:
    @staticmethod
    @custom_exception()
    def fillna_and_cast_lower(
        data: DataFrame, feature: str, default_val: str
    ) -> DataFrame:
        """
        This function is used to fillna with the default value specified
        on the feature specified.

        :param data: dataframe object pandas
        :param feature: feature name for preprocessing
        :param default_val: default value to be used for replacing nan
        :return:
        """
        data[feature] = data[feature].fillna(default_val)
        data[feature] = data[feature].replace(
            WHITESPACE_REGEX, SINGLE_SPACE, regex=True
        )
        data[feature] = data[feature].replace({ABSURD_VALUE: default_val})
        data[feature] = data[feature].str.strip()
        data[feature] = data[feature].str.lower()
        return data

    @class_custom_exception()
    def preprocess_customer_id(self, data: DataFrame) -> DataFrame:
        """
        This function type casts customer_id to string.
        :param data: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        data[CUSTOMER_ID] = data[CUSTOMER_ID].astype(str)
        return data

    @class_custom_exception()
    def attribute1_substitution(self, data: DataFrame) -> DataFrame:
        """
        This function substitutes the values in attribute1 with custom values

        :param data: dataframe object pandas
        :return: dataframe object pandas
        """
        data.loc[
            data[ATTRIBUTE1].str.contains(CHANNEL_LIVE, case=False), ATTRIBUTE1
        ] = CHANNEL_LIVE
        data.loc[
            data[ATTRIBUTE1].str.contains(CATCHUP, case=False), ATTRIBUTE1
        ] = CATCHUP
        data.loc[data[ATTRIBUTE1].str.contains(VOD, case=False), ATTRIBUTE1] = VOD

        return data

    @class_custom_exception()
    def preprocess_features(
        self,
        data: DataFrame,
    ) -> DataFrame:
        """
        This function takes dict of features and their default nan values
        and calls fillna_and_cast_lower function for preprocessing.

        :param data: dataframe object pandas
        :return: dataframe object pandas
        """
        for feature, value in DEFAULT_FEATURE_VALUES.items():
            data = PreprocessBehaviour.fillna_and_cast_lower(
                data, feature=feature, default_val=value
            )

        return data

    @class_custom_exception()
    def preprocess_and_explode(
        self, data: DataFrame, feature: str, key: str
    ) -> DataFrame:
        """
        This function transforms each element of a
        list-like to a row, replicating index values.

        :param data: dataframe object pandas
        :param feature: feature name
        :param key: dict key to be used
        :return: preprocessed dataframe object pandas
        """
        data = data[[CUSTOMER_ID, DURATION, feature]]
        mask = data[feature].apply(lambda d: d if isinstance(d, list) else [])
        result_list = [[x[key] for x in list_dict] for list_dict in mask]
        data = data.drop([feature], axis=1)
        data[feature] = result_list

        return data.explode(feature).fillna("nan")

    @class_custom_exception()
    def controller(
        self, data: DataFrame, to_explode: bool, feature="", key=""
    ) -> DataFrame:
        """
        The driver function for PreprocessBehaviour class.
        Returns preprocessed dataframe and also breaks the list of
        feature values specified in feature parameter in
        multiple rows, as per the value specified for 'to_explode'

        :param data: dataframe object pandas
        :param to_explode: if True, split the list of value into
        separate records, ignore otherwise
        :param feature: feature to be exploded
        :param key: dict key to be used
        :return: preprocessed dataframe object pandas
        """

        data = self.preprocess_customer_id(data)

        if to_explode:
            print("Preprocessing {}...".format(feature))
            data = self.preprocess_and_explode(data, feature, key)

        else:
            print("Substituting values in Attribute1...")
            data = self.attribute1_substitution(data)

            print("Preprocessing User Behaviour Features...")
            data = self.preprocess_features(data)

            print("Finished Preprocessing User Behaviour Data...")

        return data
