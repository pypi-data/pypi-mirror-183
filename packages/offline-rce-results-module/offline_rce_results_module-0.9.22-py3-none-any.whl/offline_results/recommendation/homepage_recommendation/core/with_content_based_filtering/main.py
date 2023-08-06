from offline_results.recommendation.homepage_recommendation.core.with_content_based_filtering.data_gathering import (
    DataGathering,
)
from offline_results.recommendation.homepage_recommendation.core.with_content_based_filtering.data_preperation import (
    DataPreprocessing,
)
from offline_results.recommendation.homepage_recommendation.core.with_content_based_filtering.generate_recommendation import (
    HomepageIdContentScorePred,
)
from offline_results.recommendation.homepage_recommendation.core.with_content_based_filtering.model_training import (
    RecommendationModel,
)
from offline_results.utils import class_custom_exception, Logging


class HomepageIdContentsRecommendation(
    DataGathering, DataPreprocessing, RecommendationModel, HomepageIdContentScorePred
):
    @class_custom_exception()
    def get_data(self):
        self.data_gathering()

    @class_custom_exception()
    def data_preparation(self):
        self.preprocessing(self.raw_data)

    @class_custom_exception()
    def train_model(self):
        try:
            self.get_data()
            self.data_preparation()
            self.create_data_obj()
            model = self.model_training()
            if model is not None:
                self.save_model_to_s3(model)

        except Exception as e:
            Logging.error(f"Error while training model. Error :{e}")


# test code here for model training
# if __name__ == "__main__":
#     ctl = HomepageIdContentsRecommendation(data_source=S3) #data_source options are , s3, graph_db
#     ctl.train_model()

##test code here for getting score for content ids
# if __name__ == "__main__":
#     ctl=HomepageIdContentsRecommendation()
#     model = ctl.load_model_from_s3()
#     recomm = ctl.get_score(user=4120, contents=[15, 50, 11, 17173, 34410], model=model)
#     print(recomm)
