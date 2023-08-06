import logging
import os
import pickle

from pandas import DataFrame, Series, concat

from offline_results.common.config import (
    MODELS_PATH,
    VISIONPLUS_DEV,
)
from offline_results.common.constants import (
    CUSTOMER_ID,
    HOMEPAGE_ID,
    SCORE,
    CURRENT_MODEL_NAME,
    TAGS,
    HAS_TAG_PREFERENCE,
    CONTENT_DURATION,
    CATEGORY,
    HAS_CATEGORY_PREFERENCE,
    HAS_SUBCATEGORY_PREFERENCE,
    HAS_DURATION_PREFERENCE,
    SUBCATEGORY,
    TOD,
    HAS_TOD_PREFERENCE,
    TAGS_ID,
    VALUE,
    CATEGORY_ID,
    SUBCATEGORY_ID,
    DURATION,
    HOMEPAGE,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.homepage_cluster_category.config import (
    HOMEPAGE_ID_CLF_MODEL,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception, custom_exception, Logging


class HomepageIdRecommendation(RecommendationUtils):
    @staticmethod
    @custom_exception()
    def load_model_from_s3(
        is_paytv, model_name=HOMEPAGE_ID_CLF_MODEL[CURRENT_MODEL_NAME]
    ):
        try:
            path = (
                os.getcwd()
                + "\\"
                + str("paytv" if is_paytv else "no_paytv")
                + "_"
                + model_name
            )
            ctl = ConnectS3()
            resource = ctl.create_connection()
            ctl.download_from_s3(
                bucket_name=VISIONPLUS_DEV,
                filename_with_path=path,
                key=MODELS_PATH
                + HOMEPAGE_ID
                + "/"
                + str("paytv" if is_paytv else "no_paytv")
                + "_"
                + model_name,
                resource=resource,
            )
            model = pickle.load(open(path, "rb"))
            return model
        except Exception as e:
            Logging.error(f"Error while uploading model {model_name} on s3, Error: {e}")

    @staticmethod
    @custom_exception()
    def get_user_preferences(customer_id, encoding_model):

        ctl = RecommendationUtils()
        user_tags_pref = ctl.single_user_pref(
            customer_id, TAGS, HAS_TAG_PREFERENCE, TAGS_ID
        )
        user_duration_pref = ctl.single_user_pref(
            customer_id, CONTENT_DURATION, HAS_DURATION_PREFERENCE, VALUE
        )
        user_category_pref = ctl.single_user_pref(
            customer_id, CATEGORY, HAS_CATEGORY_PREFERENCE, CATEGORY_ID
        )
        user_sub_category_pref = ctl.single_user_pref(
            customer_id, SUBCATEGORY, HAS_SUBCATEGORY_PREFERENCE, SUBCATEGORY_ID
        )
        user_tod_pref = ctl.single_user_pref(
            customer_id, TOD, HAS_TOD_PREFERENCE, VALUE
        )
        user_df = DataFrame(
            {
                CUSTOMER_ID: customer_id,
                TAGS_ID: [user_tags_pref],
                DURATION: [user_duration_pref],
                CATEGORY_ID: [user_category_pref],
                SUBCATEGORY_ID: [user_sub_category_pref],
                VALUE: [user_tod_pref],
            }
        )
        col_and_model = {
            TAGS_ID: TAGS,
            DURATION: DURATION,
            CATEGORY_ID: CATEGORY,
            SUBCATEGORY_ID: SUBCATEGORY,
            VALUE: TOD,
        }
        for col in col_and_model:
            user_df = HomepageIdRecommendation.encode_df(
                user_df, col, encoding_model[col_and_model[col]]
            )
        user_df = HomepageIdRecommendation.expand_features(user_df)
        user_df = user_df.drop(columns=[CUSTOMER_ID])
        return user_df

    @class_custom_exception()
    def generate_recommendations(
        self,
        user_id,
        model=None,
        encoding_model=None,
    ):
        try:
            user_pref = self.get_user_preferences(user_id, encoding_model)
            yhat = model.predict(user_pref)[0]
            homepage_encoder = encoding_model[HOMEPAGE]
            result = DataFrame({HOMEPAGE_ID: list(homepage_encoder), SCORE: yhat})
            result = result.sort_values([SCORE], ascending=False).reset_index(drop=True)
            logging.info("success predicting recommendation")
        except Exception as e:
            Logging.error(f"Error predicting recommendation. Error: {e}")
        return result

    @staticmethod
    @custom_exception()
    def encode_df(df, col, one_hot_encoder):
        ctl = RecommendationUtils()
        df[col] = df[col].apply(lambda x: ctl.multi_label_encoding(x, one_hot_encoder))
        return df

    @staticmethod
    @custom_exception()
    def expand_features(
        df,
    ):
        for col in df.columns:
            if col == CUSTOMER_ID:
                continue
            expand_features = df[col].apply(Series)
            expand_features.columns = [
                col + "_" + str(i) for i in expand_features.columns
            ]
            df = df.drop(columns=[col])
            df = concat([df, expand_features], axis=1)
        return df


# test code here
# if __name__=="__main__":
#     ctl=HomepageIdRecommendation()
#     encoding_model = ctl.load_model_from_s3(True, ENCODING_MODEL)
#     model = ctl.load_model_from_s3(True)
#     recomm = ctl.generate_recommendations('11627385', model, encoding_model)
#     print(recomm)
