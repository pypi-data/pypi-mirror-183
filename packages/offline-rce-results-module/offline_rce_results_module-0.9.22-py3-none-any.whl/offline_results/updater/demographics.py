from datetime import datetime, date

from pandas import DataFrame

from offline_results.common.constants import (
    CUSTOMER_ID,
    BIRTHDAY,
    GENDER,
    CUSTOMER_CREATED_ON,
    CUSTOMER_MODIFIED_ON,
    DEFAULT_NAN,
    DEFAULT_DATE,
    GENDER_VALUES,
    AGE,
    MEDIAN_AGE,
    AGE_UPPER_BOUND,
)
from offline_results.common.convert_time_zone import ConvertTimeZone
from offline_results.utils import class_custom_exception


class PreprocessDemography:
    @class_custom_exception()
    def preprocess_customer_id(self, df: DataFrame) -> DataFrame:
        """
        This function type casts customer_id to string.
        :param df: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        df[CUSTOMER_ID] = df[CUSTOMER_ID].astype(str)

        return df

    @class_custom_exception()
    def preprocess_gender(self, df: DataFrame) -> DataFrame:
        """
        This function maps occurrences of male and female to m and f.
        And fills nan values with na

        :param df: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        df[GENDER] = df[GENDER].fillna(DEFAULT_NAN)
        df[GENDER] = df[GENDER].str.lower()
        df[GENDER] = df[GENDER].replace(GENDER_VALUES)

        return df

    @class_custom_exception()
    def preprocess_birthday(self, df: DataFrame) -> DataFrame:
        """
        This function typecasts birthday column into date object

        :param df: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        df[BIRTHDAY] = df[BIRTHDAY].fillna(value=DEFAULT_DATE)
        df[BIRTHDAY] = df[BIRTHDAY].astype("datetime64[s]")
        df[BIRTHDAY] = df[BIRTHDAY].dt.date

        return df

    @class_custom_exception()
    def calculate_age(self, df: DataFrame) -> DataFrame:
        """
        This function calculates age of the customer from birthday

        :param df: dataframe object pandas
        :return: preprocessed dataframe object pandas
        """
        df[AGE] = [int(birthday.year) for birthday in df[BIRTHDAY]]
        df[AGE] = (df[AGE] - int(datetime.utcnow().strftime("%Y"))) * (-1)
        df.loc[df[AGE] > AGE_UPPER_BOUND, AGE] = MEDIAN_AGE
        df[AGE] = df[AGE].astype(int)
        df[BIRTHDAY] = df[BIRTHDAY].astype(str)

        return df

    @class_custom_exception()
    def preprocess_created_modified_on(self, df: DataFrame, update: bool) -> DataFrame:
        """
        This function typecasts customer_created_on and customer_modified_on into datetime object

        :param df: dataframe object pandas
        :param update: If run from vdb_updater
        :return: preprocessed dataframe object pandas
        """
        df[CUSTOMER_CREATED_ON] = df[CUSTOMER_CREATED_ON].fillna(value=DEFAULT_DATE)
        df[CUSTOMER_MODIFIED_ON] = df[CUSTOMER_MODIFIED_ON].fillna(
            df[CUSTOMER_CREATED_ON]
        )
        df[CUSTOMER_CREATED_ON] = ConvertTimeZone(df[CUSTOMER_CREATED_ON])
        df[CUSTOMER_MODIFIED_ON] = ConvertTimeZone(df[CUSTOMER_MODIFIED_ON])
        if update:
            df = df[df[CUSTOMER_MODIFIED_ON] >= str(date.today())]
        df[CUSTOMER_CREATED_ON] = df[CUSTOMER_CREATED_ON].astype(str)
        df[CUSTOMER_MODIFIED_ON] = df[CUSTOMER_MODIFIED_ON].astype(str)

        return df

    @class_custom_exception()
    def controller(
        self,
        df: DataFrame,
        update: bool
    ) -> DataFrame:
        """
        This is the driver function for user demographics preprocessing

        :param df: dataframe object pandas
        :param update: True if run from vdb_updater
        :return: preprocessed dataframe object pandas
        """
        print("Preprocessing Customer_id...")
        data = self.preprocess_customer_id(df)

        print("Preprocessing Gender...")
        data = self.preprocess_gender(data)

        print("Preprocessing Birthday...")
        data = self.preprocess_birthday(data)

        print("Calculating Customer Age...")
        data = self.calculate_age(data)

        print("Preprocessing Customer_created_on and Customer_modified_on...")
        data = self.preprocess_created_modified_on(df=data, update=update)

        print("Finished Preprocessing User Demographics Data...")

        return data
