import os
import pickle

from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise.model_selection import GridSearchCV

from offline_results.common.config import MODELS_PATH, VISIONPLUS_DEV
from offline_results.common.constants import HOMEPAGE_ID
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.homepage_cluster_category.config import (
    GRID_SEARCH_PARAMETERS,
    HOMEPAGE_IDS_CONTENT_REC_MODEL,
)
from offline_results.utils import class_custom_exception, custom_exception, Logging


class RecommendationModel:
    @class_custom_exception()
    def create_data_obj(self, data=False):
        if data is not False:
            self.dataset = data
        reader = Reader(rating_scale=HOMEPAGE_IDS_CONTENT_REC_MODEL["rating_scale"])
        self.traing_dataset = Dataset.load_from_df(self.dataset, reader)
        return self.traing_dataset

    @class_custom_exception()
    def get_best_param(self):
        try:
            measures = HOMEPAGE_IDS_CONTENT_REC_MODEL["measures"]
            cv = HOMEPAGE_IDS_CONTENT_REC_MODEL["cv"]
            gs = GridSearchCV(
                SVD,
                GRID_SEARCH_PARAMETERS,
                measures=measures,
                refit=True,
                cv=cv,
                n_jobs=-1,
            )
            Logging.info("Grid-search started....")
            gs.fit(self.traing_dataset)
            training_parameters = gs.best_params["rmse"]
            Logging.info("BEST RMSE: \t" + str(gs.best_score["rmse"]))
            Logging.info("BEST params: \t" + str(gs.best_params["rmse"]))
            return training_parameters
        except Exception as e:
            Logging.error(f"Error while fitting Grid search. Exception {e}")

    @class_custom_exception()
    def model_training(self, data=False, grid_search=False):
        try:
            Logging.info("start model training")
            if data is not False:
                self.create_data_obj(data)
            if grid_search:
                best_param = self.get_best_param()
                model = SVD(
                    n_epochs=best_param["n_epochs"],
                    lr_all=best_param["lr_all"],
                    reg_all=best_param["reg_all"],
                )
            else:
                model = SVD(n_epochs=150, lr_all=0.002, reg_all=0.02)
            model.fit(self.traing_dataset.build_full_trainset())
            Logging.info("model training is done")
            return model

        except Exception as e:
            Logging.error(f"Error while model training. Error :{e}")

    @staticmethod
    @custom_exception()
    def save_model_to_s3(
        model, model_name=HOMEPAGE_IDS_CONTENT_REC_MODEL["current_model_name"]
    ):
        try:
            path = os.getcwd() + "\\" + model_name
            with open(model_name, "wb") as f:
                pickle.dump(model, f)
            ctl = ConnectS3()
            resource = ctl.create_connection()
            ctl.upload_to_s3(
                bucket_name=VISIONPLUS_DEV,
                file_with_path=path,
                key=MODELS_PATH + HOMEPAGE_ID + "/" + model_name,
                resource=resource,
            )
            os.remove(path)
            Logging.info(f"Model {model_name} saved successfully")
        except Exception as e:
            Logging.error(f"Error while uploading model {model_name} on s3, Error: {e}")


# train model on your dataset here
# if __name__ == "__main__":
#     ctl = RecommendationModel()
#     model = ctl.model_training()
#     if model is not None:
#       ctl.save_model_to_s3(model)
