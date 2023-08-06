from pandas import DataFrame, Series
from numpy import array, where, unique, average, asarray, linalg
from offline_results.common.constants import NON_FEATURES
from collections import Counter


class EvaluationUtils:

    def __init__(
            self,
            data=DataFrame
    ):
        """
        Using the combined dataset of
        features and clustering results,
        prepare the desired data members
        :param data: combined dataset
        """
        self.data = data
        self.features = self.data.drop(
            columns=NON_FEATURES
        )
        self.ensemble_results = DataFrame()

    def calculate_centroid(
            self,
            features
    ) -> array:
        """
        Calculate centroid using cluster
        feature vectors
        :param features: feature vectors for
        cluster members
        :return: average vector for input
        """
        return average(features, axis=0)

    def get_unique_cluster_labels(
            self,
            labels
    ) -> array:
        """
        From the cluster labels vector,
        identify the unique values in the input
        :param labels: cluster labels vector
        :return: unique values as a vector
        """
        return unique(labels)

    def get_indices(
            self,
            result_labels,
            label
    ) -> array:
        """
        Identify the feature vectors that
        belong to the same label
        :param result_labels: labels vector
        :param label: label value
        :return: vector indices with same label
        """
        return asarray(where(
            result_labels == label)[0])

    def get_distance(
            self,
            point1: array,
            point2: array
    ) -> float:
        """
        Calculates euclidean distance
        :param point1: first vector
        :param point2: second vector
        :return: euclidean distance between
        the two input vectors
        """
        return linalg.norm(point1 - point2)

    def compute_label_weights(
            self,
            labels: Series
    ) -> dict:
        """
        For each cluster label, calculate the
        frequency of occurrence of each label
        in the input vector
        :param labels: label vector
        :return: {label: frequency} mapping
        """
        return dict(Counter(labels))

    def get_global_centroid(
            self,
            centroids: dict
    ) -> array:
        """
        Calculate and return the global centroid
        :param centroids: vector of centroids
        :return: global centroid
        """
        return self.calculate_centroid(
            array(list(centroids.values())))

    def get_feature_label_df(
            self,
            input_set: DataFrame,
            label: str,
            method: str
    ) -> DataFrame:
        """
        Return a merged df only of features
        and corresponding cluster label to
        which they belong
        :param input_set: feature
        :param label: cluster label vector
        :param method: cluster label
        :return: [feature, label] combined df
        """
        return input_set[input_set[method]
                         == label]
