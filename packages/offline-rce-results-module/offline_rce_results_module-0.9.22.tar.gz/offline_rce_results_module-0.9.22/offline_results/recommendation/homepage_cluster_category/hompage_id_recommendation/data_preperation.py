import functools as ft
import os
import pickle

from pandas import merge, concat, Series

from offline_results.common.config import VISIONPLUS_DEV, MODELS_PATH, ENCODING_MODEL
from offline_results.common.constants import (
    CUSTOMER_ID,
    CONTENT_ID,
    HOMEPAGE_ID,
    TAGS,
    DURATION,
    CATEGORY,
    SUBCATEGORY,
    TOD,
    TAGS_ID,
    VALUE,
    CATEGORY_ID,
    SUBCATEGORY_ID,
    VIEW_COUNT,
    HOMEPAGE,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception, Logging


class DataPreprocessing:
    @class_custom_exception()
    def save_encoding_model(self, is_paytv, model, model_name=ENCODING_MODEL):
        try:
            path = (
                os.getcwd()
                + "/"
                + str("paytv" if is_paytv else "no_paytv")
                + "_"
                + model_name
            )
            with open(
                str("paytv" if is_paytv else "no_paytv") + "_" + model_name, "wb"
            ) as f:
                pickle.dump(model, f)
            ctl = ConnectS3()
            ctl.upload_to_s3(
                bucket_name=VISIONPLUS_DEV,
                file_with_path=path,
                key=MODELS_PATH
                + HOMEPAGE_ID
                + "/"
                + str("paytv" if is_paytv else "no_paytv")
                + "_"
                + model_name,
                resource=ctl.create_connection(),
            )
            os.remove(path)
        except Exception as e:
            Logging.error(f"Error while uploading model {model_name} on s3, Error: {e}")

    @class_custom_exception()
    def create_encoding_model(
        self,
    ):
        self.encoding_model = {}
        self.encoding_model[TAGS] = set(self.tags_pref[TAGS_ID])
        self.encoding_model[DURATION] = set(self.duration_pref[DURATION])
        self.encoding_model[CATEGORY] = set(self.category_pref[CATEGORY_ID])
        self.encoding_model[SUBCATEGORY] = set(self.sub_category_pref[SUBCATEGORY_ID])
        self.encoding_model[TOD] = set(self.tod_pref[VALUE])
        self.encoding_model[HOMEPAGE] = set(self.homepage_having_content[HOMEPAGE_ID])
        self.save_encoding_model(self.is_paytv, self.encoding_model)

    @class_custom_exception()
    def encode_df(self, df, col, one_hot_encoder):
        ctl = RecommendationUtils()
        df[col] = df[col].apply(lambda x: ctl.multi_label_encoding(x, one_hot_encoder))
        return df

    @class_custom_exception()
    def expand_df_features(
        self,
        df,
    ):
        for col in df.columns:
            if col != CUSTOMER_ID:
                expand_features = df[col].apply(Series)
                expand_features.columns = [
                    col + "_" + str(i) for i in expand_features.columns
                ]
                df = df.drop(columns=[col])
                df = concat([df, expand_features], axis=1)
        return df

    @class_custom_exception()
    def data_filtration(self):

        self.ubd = self.ubd[[CUSTOMER_ID, CONTENT_ID, VIEW_COUNT]]
        ubd = merge(self.ubd, self.homepage_having_content, on=CONTENT_ID, how="left")
        ubd = ubd.dropna()
        ubd[HOMEPAGE_ID] = ubd[HOMEPAGE_ID].astype(int)
        ubd_temp = (
            ubd.groupby([CUSTOMER_ID, HOMEPAGE_ID])[VIEW_COUNT].sum().reset_index()
        )
        ubd_valid_hid = (
            ubd_temp.groupby(HOMEPAGE_ID)[VIEW_COUNT].apply(sum).reset_index()
        )
        valid_hid = list(ubd_valid_hid[ubd_valid_hid[VIEW_COUNT] >= 100][HOMEPAGE_ID])
        ubd_temp = ubd_temp[ubd_temp[HOMEPAGE_ID].isin(valid_hid)]
        ubd_temp = (
            ubd_temp.groupby(CUSTOMER_ID)[HOMEPAGE_ID]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )
        self.preferences[CUSTOMER_ID] = self.preferences[CUSTOMER_ID].astype(str)
        self.ubd[CUSTOMER_ID] = self.ubd[CUSTOMER_ID].astype(str)
        ubd = merge(ubd_temp, self.preferences, on=CUSTOMER_ID)
        ubd = self.encode_df(ubd, HOMEPAGE_ID, self.encoding_model[HOMEPAGE])
        self.ubd = ubd.drop(columns=[CUSTOMER_ID])
        return self.ubd

    @class_custom_exception()
    def data_encoding(self):
        self.create_encoding_model()

        self.tags_pref = (
            self.tags_pref.groupby(CUSTOMER_ID)[TAGS_ID]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )
        self.duration_pref = (
            self.duration_pref.groupby(CUSTOMER_ID)[DURATION]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )
        self.category_pref = (
            self.category_pref.groupby(CUSTOMER_ID)[CATEGORY_ID]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )
        self.sub_category_pref = (
            self.sub_category_pref.groupby(CUSTOMER_ID)[SUBCATEGORY_ID]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )
        self.tod_pref = (
            self.tod_pref.groupby(CUSTOMER_ID)[VALUE]
            .apply(lambda x: list(set(x)))
            .reset_index()
        )

        self.tags_pref = self.encode_df(
            self.tags_pref, TAGS_ID, self.encoding_model[TAGS]
        )
        self.duration_pref = self.encode_df(
            self.duration_pref, DURATION, self.encoding_model[DURATION]
        )
        self.category_pref = self.encode_df(
            self.category_pref, CATEGORY_ID, self.encoding_model[CATEGORY]
        )
        self.sub_category_pref = self.encode_df(
            self.sub_category_pref, SUBCATEGORY_ID, self.encoding_model[SUBCATEGORY]
        )
        self.tod_pref = self.encode_df(self.tod_pref, VALUE, self.encoding_model[TOD])
        preferences = [
            self.category_pref,
            self.sub_category_pref,
            self.tags_pref,
            self.tod_pref,
            self.duration_pref,
        ]

        self.preferences = ft.reduce(
            lambda left, right: merge(left, right, on=CUSTOMER_ID), preferences
        )
        self.preferences = self.expand_df_features(self.preferences)

    @class_custom_exception()
    def data_preprocessing(
        self,
    ):
        self.data_encoding()
        self.data_filtration()
