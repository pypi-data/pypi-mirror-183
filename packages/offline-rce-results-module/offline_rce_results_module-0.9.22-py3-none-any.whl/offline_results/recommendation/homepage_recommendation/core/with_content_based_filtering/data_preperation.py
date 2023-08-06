from offline_results.common.constants import CONTENT_ID, CUSTOMER_ID, RATING
from offline_results.recommendation.homepage_cluster_category.config import (
    MIN_USER_GIVEN_RATING,
    MIN_CONTENT_HAVING_RATING,
)
from offline_results.utils import class_custom_exception, Logging


class DataPreprocessing:
    @class_custom_exception()
    def data_filteration(self):
        try:
            filter_items = (
                self.dataset[CONTENT_ID].value_counts() > MIN_CONTENT_HAVING_RATING
            )
            filter_items = filter_items[filter_items].index.tolist()
            filter_users = (
                self.dataset[CUSTOMER_ID].value_counts() > MIN_USER_GIVEN_RATING
            )
            filter_users = filter_users[filter_users].index.tolist()
            self.dataset = self.dataset[
                (self.dataset[CONTENT_ID].isin(filter_items))
                & (self.dataset[CUSTOMER_ID].isin(filter_users))
            ]
        except Exception as e:
            Logging.error(f"Error while filtering data. Error :{e}")

    @class_custom_exception()
    def feature_extraction(self):
        try:
            self.dataset = self.raw_data[[CUSTOMER_ID, CONTENT_ID, RATING]]
        except Exception as e:
            Logging.error(f"Error while feature extraction. Error :{e}")

    @class_custom_exception()
    def preprocessing(self, data):
        try:
            Logging.info("start data pre processing")
            self.raw_data = data
            self.feature_extraction()
            self.data_filteration()
            Logging.info("data pre processing done")
            return self.dataset
        except Exception as e:
            Logging.error(f"Error while data pre processing. Error :{e}")
