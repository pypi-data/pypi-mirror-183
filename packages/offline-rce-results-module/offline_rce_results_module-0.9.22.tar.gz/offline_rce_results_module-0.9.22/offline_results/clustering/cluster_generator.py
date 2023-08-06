from offline_results.common.read_write_from_s3 import ConnectS3
from pandas import DataFrame, Series, get_dummies
from sklearn.cluster import MiniBatchKMeans, KMeans

from offline_results.clustering.clustering_utils import ClusteringUtils
from offline_results.clustering.config import K_PAYTV, K_NO_PAYTV, MINIBATCH_SIZE
from offline_results.common.constants import CUSTOMER_ID, MINIBATCH_KMEANS, BIRTHDAY, \
    CUSTOMER_CREATED_ON, CUSTOMER_MODIFIED_ON, PAYTVPROVIDER_ID, GENDER, UD_KEY, \
    IS_PAY_TV, GENDER_NAN, STATUS, PAY_TV, NO_PAY_TV
from offline_results.common.config import VISIONPLUS_DEV, CLUSTER_MODEL_PATH


class ClusterGenerator(ClusteringUtils):

    def __init__(
            self,
            data=DataFrame
    ):
        data[CUSTOMER_ID] = data[CUSTOMER_ID].astype(str)
        ClusteringUtils.__init__(self, data=data)
        self.clusters = DataFrame()

    def get_kmeans(
            self,
            features: DataFrame,
            paytv: bool
    ) -> Series:
        """
        Generate KMeans Clusters
        :param features: user features
        :return: list of assigned cluster values
        """
        if paytv:
            k = K_PAYTV
        else:
            k = K_NO_PAYTV
        model = KMeans(n_clusters=k, random_state=0)
        return model.fit_predict(features)

    def get_minibatch_kmeans(
            self,
            features: DataFrame,
            paytv: bool,
            k_value: int
    ) -> Series:
        """
        Generate MiniBatch-KMeans clusters
        :param features: user features
        :return: list of assigned cluster values
        """
        model = MiniBatchKMeans(n_clusters=k_value, init='k-means++', random_state=None,
                                batch_size=MINIBATCH_SIZE)
        model.fit(features)
        result = model.predict(features)
        ctl = ConnectS3()
        resource = ctl.create_connection()
        filename = MINIBATCH_KMEANS + "_reclustering_" + (PAY_TV if paytv else NO_PAY_TV) + ".pkl"
        print("Write model to S3...")
        ctl.write_pkl_to_s3(bucket_name=VISIONPLUS_DEV,
                            object_name=CLUSTER_MODEL_PATH + filename,
                            data=model,
                            resource=resource)
        return result

    def controller(
            self,
            paytv: bool,
            k_value: int
    ):
        """
        Driver function for Cluster based feature
        processing and results generation
        :return: None
        """
        features = self.drop_sparse_features()

        self.clusters[CUSTOMER_ID] = features[CUSTOMER_ID]

        features = get_dummies(
            features,
            columns=[GENDER, PAYTVPROVIDER_ID]
        )

        # since we do not want to pass an identifier as a clustering feature
        if paytv:
            features = self.remove_attributes(attributes=features,
                                              to_drop=[CUSTOMER_ID,
                                                       BIRTHDAY,
                                                       CUSTOMER_CREATED_ON,
                                                       CUSTOMER_MODIFIED_ON,
                                                       UD_KEY,
                                                       GENDER_NAN,
                                                       STATUS])
        else:
            features = self.remove_attributes(attributes=features,
                                              to_drop=[CUSTOMER_ID,
                                                       BIRTHDAY,
                                                       CUSTOMER_CREATED_ON,
                                                       CUSTOMER_MODIFIED_ON,
                                                       UD_KEY,
                                                       GENDER_NAN,
                                                       STATUS])

        self.clusters[MINIBATCH_KMEANS] = self.get_minibatch_kmeans(features=features, paytv=paytv, k_value=k_value)
