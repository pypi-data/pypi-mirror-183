import os
import pickle
import tensorflow as tf
from keras import Sequential, Model
from keras.layers import Dense
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedKFold
from tensorflow.python.keras.layers import deserialize, serialize
from tensorflow.python.keras.saving import saving_utils

from offline_results.common.config import S3_RESOURCE, MODELS_PATH, VISIONPLUS_DEV
from offline_results.common.constants import HOMEPAGE_ID
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.homepage_cluster_category.config import (
    HOMEPAGE_ID_CLF_MODEL,
)
from offline_results.utils import class_custom_exception, custom_exception, Logging
from keras.callbacks import EarlyStopping

@custom_exception()
def unpack(model, weights):
    restored_model = deserialize(model)
    restored_model.set_weights(weights)
    return restored_model


@custom_exception()
def make_keras_picklable():
    def __reduce__(self):
        model = serialize(self)
        weights = self.get_weights()
        return (unpack, (model, weights))

    cls = Model
    cls.__reduce__ = __reduce__


class ClassificationModel:
    def __init__(self, features, target):
        self.X = features
        self.y = target

    @class_custom_exception()
    def model_config(self, n_inputs, n_outputs):
        make_keras_picklable()
        model = Sequential()
        model.add(
            Dense(
                30,
                input_dim=n_inputs,
                kernel_initializer="he_uniform",
                activation="relu",
            )
        )
        model.add(Dense(n_outputs, activation="sigmoid"))
        model.compile(loss="binary_crossentropy", optimizer=tf.keras.optimizers.Adam())
        return model

    @staticmethod
    @custom_exception()
    def save_model_to_s3(
        model, is_paytv, model_name=HOMEPAGE_ID_CLF_MODEL["current_model_name"]
    ):
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
                resource=S3_RESOURCE,
            )
            os.remove(path)
            Logging.info(f"MLC Rank model {model_name} saved successfully")
        except Exception as e:
            Logging.error(f"Error while uploading model {model_name} on s3, Error: {e}")

    @class_custom_exception()
    def evaluate_model(self, config=HOMEPAGE_ID_CLF_MODEL):
        try:
            Logging.info(f"MLC Rank model: model training started")
            epochs = config.get("epochs", HOMEPAGE_ID_CLF_MODEL["epochs"])
            n_splits = config.get("n_splits", HOMEPAGE_ID_CLF_MODEL["n_splits"])
            n_repeats = config.get("n_repeats", HOMEPAGE_ID_CLF_MODEL["n_repeats"])
            random_state = config.get(
                "random_state", HOMEPAGE_ID_CLF_MODEL["random_state"]
            )
            verbose = config.get("verbose", HOMEPAGE_ID_CLF_MODEL["verbose"])
            results = list()
            n_inputs, n_outputs = self.X.shape[1], self.y.shape[1]
            cv = RepeatedKFold(
                n_splits=n_splits, n_repeats=n_repeats, random_state=random_state
            )
            Logging.info("model training has been started....")
            model = self.model_config(n_inputs, n_outputs)
            early_stop = EarlyStopping(monitor='loss', patience=0, restore_best_weights=True)
            for train_ix, test_ix in cv.split(self.X):
                Logging.info("================= next iteration is started ")
                X_train, X_test = self.X[train_ix], self.X[test_ix]
                y_train, y_test = self.y[train_ix], self.y[test_ix]
                model.fit(X_train, y_train, verbose=verbose, epochs=epochs, callbacks=[early_stop])
                yhat = model.predict(X_test)
                yhat = yhat.round()
                acc = accuracy_score(y_test, yhat)
                Logging.info("=================>" + str(">%.3f" % acc))
                results.append(acc)
            return model

        except Exception as e:
            Logging.error(f"Error while model training. Exception: {e}")


# train model on your dataset here
# if __name__ == "__main__":
#     import pandas as pd
#     X = pd.read_pickle("X.pkl").to_numpy() #pass any other data,
#     y = pd.read_pickle("y.pkl").to_numpy() #pass any other data
#     ctl = ClassificationModel(X, y)# X and y should be numpy array
#     model = ctl.evaluate_model()
#     ctl.save_model_to_s3(model)
