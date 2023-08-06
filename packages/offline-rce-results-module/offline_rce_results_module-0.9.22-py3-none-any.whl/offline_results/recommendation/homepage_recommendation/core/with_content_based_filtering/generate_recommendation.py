import os
import pickle

from pandas import DataFrame, Series
from sklearn.preprocessing import MinMaxScaler

from offline_results.common.config import MODELS_PATH, VISIONPLUS_DEV, SCORE_WEIGHT, IMPLICIT_RATING_WEIGHT
from offline_results.common.constants import (
    HOMEPAGE_ID,
    CURRENT_MODEL_NAME,
    CONTENT_ID,
    SCORE, CUSTOMER_ID, IMPLICIT_RATING,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.homepage_cluster_category.config import (
    HOMEPAGE_IDS_CONTENT_REC_MODEL,
)
from offline_results.utils import class_custom_exception, custom_exception, Logging


class HomepageIdContentScorePred:
    @staticmethod
    @custom_exception()
    def load_model_from_s3(
        model_name=HOMEPAGE_IDS_CONTENT_REC_MODEL[CURRENT_MODEL_NAME],
    ):
        try:
            path = os.getcwd() + "\\" + model_name
            ctl = ConnectS3()
            resource = ctl.create_connection()
            ctl.download_from_s3(
                bucket_name=VISIONPLUS_DEV,
                filename_with_path=path,
                key=MODELS_PATH + HOMEPAGE_ID + "/" + model_name,
                resource=resource,
            )
            model = pickle.load(open(path, "rb"))
            return model
        except Exception as e:
            Logging.error(f"Error while uploading model {model_name} on s3, Error: {e}")

    @class_custom_exception()
    def scale_and_sort(self, df):
        scaler = MinMaxScaler(feature_range=(0, 1))
        df[SCORE] = scaler.fit_transform(df[[SCORE]].to_numpy()).flatten().tolist()
        df[SCORE] = 1 if df[SCORE].max() == 0 else df[SCORE]
        #df[SCORE] = df[SCORE].replace({0: -1})
        df = df.sort_values([SCORE], ascending=False, ignore_index=True)
        return df[[CONTENT_ID, SCORE]]

    @class_custom_exception()
    def get_score(self, users, contents,implicit_rating, model=None):
        try:
            rec = {CONTENT_ID: [], SCORE: [], "rating":[]}
            loaded_model = self.load_model_from_s3() if model is None else model
            for content in contents:
                score = []
                for user in users[CUSTOMER_ID]:
                    prediction = loaded_model.predict(
                        uid=str(user), iid=str(content), verbose=False
                    )
                    score.append(prediction.est)
                rec[CONTENT_ID].append(content)
                rating = implicit_rating[implicit_rating[CONTENT_ID]==content][IMPLICIT_RATING]
                rating = rating.mean() if len(rating) > 0 else 0
                rec["rating"].append(rating)
                rec[SCORE].append(Series(score).mean())
            rec_df = DataFrame(rec)
            rec_df[SCORE] = (rec_df[SCORE] * SCORE_WEIGHT) + (rec_df["rating"] * IMPLICIT_RATING_WEIGHT)
            rec_df.drop(columns=["rating"], inplace=True)
            rec_df = rec_df if len(rec_df) == 0 else self.scale_and_sort(rec_df)
            return rec_df

        except Exception as e:
            Logging.error(f"Error while getting score. Error :{e}")


# #test code here
# if __name__ == "__main__":
#     ctl=HomepageIdContentRecommendation()
#     model = ctl.load_model_from_s3()
#     recomm = ctl.get_score(user=4120, contents=[15, 50, 11, 17173, 34410], model=model)
#     print(recomm)
