import logging

from pandas import DataFrame, Series

from offline_results.common.constants import HOMEPAGE_ID
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation.data_gathering import (
    DataGathering,
)
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation.data_preperation import (
    DataPreprocessing,
)
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation.model_training import (
    ClassificationModel,
)
from offline_results.utils import class_custom_exception


class HomepageCatRecommendation(DataGathering, DataPreprocessing):
    def __init__(self, is_paytv=True):
        super(HomepageCatRecommendation, self).__init__()
        self.data = {}
        self.dataset = DataFrame
        self.is_paytv = is_paytv

    @class_custom_exception()
    def get_data(self, is_paytv):
        logging.info(f"MLC Rank model: get-data started")
        self.data_gathering(is_paytv)

    @class_custom_exception()
    def preprocess_data(self):
        logging.info(f"MLC Rank model: preprocessing started")
        self.data_preprocessing()

    @class_custom_exception()
    def model_training(self):
        self.get_data(self.is_paytv)
        self.preprocess_data()
        target = self.ubd[HOMEPAGE_ID].apply(Series).to_numpy()
        features = self.ubd.drop(columns=HOMEPAGE_ID).to_numpy()
        ctl = ClassificationModel(features, target)
        model = ctl.evaluate_model()
        ctl.save_model_to_s3(model, self.is_paytv)


# #test code here
# if __name__ == "__main__":
#     ctl=HomepageCatRecommendation()
#     ctl.model_training()
