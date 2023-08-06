from offline_results.clustering.cluster_feature_generator import ClusterFeaturesGenerator
from offline_results.clustering.reclustering import ReCluster

import logging

from offline_results.common.config import S3_RESOURCE, VISIONPLUS_DEV, USER_MAPPING_KEY_CLUSTERING
from offline_results.repository.graph_db_connection import ANGraphDb


class ClusteringMain:

    @staticmethod
    def find_user_clusters():
        """
        Computes cluster labels once for
        paytv users and once for non-paytv users
        """
        try:
            users, paytv_k, no_paytv_k = ReCluster.find_k()
        except TypeError:
            logging.info(f"Too few data points in ubd to perform Re-Clustering, Aborting!!")
            return
        logging.info("Computing Clusters for PayTV Users......")
        connection_object = ANGraphDb.new_connection_config().graph

        ClusterFeaturesGenerator.create_cluster_features(
            resource=S3_RESOURCE,
            s3_bucket_name=VISIONPLUS_DEV,
            s3_object_name=USER_MAPPING_KEY_CLUSTERING,
            user_profile=users[0],
            paytv=True,
            k_value=paytv_k,
            connection_object=connection_object
        )

        logging.info("Computing clusters for Non-PayTV Users.....")

        ClusterFeaturesGenerator.create_cluster_features(
            resource=S3_RESOURCE,
            s3_bucket_name=VISIONPLUS_DEV,
            s3_object_name=USER_MAPPING_KEY_CLUSTERING,
            user_profile=users[1],
            paytv=False,
            k_value=no_paytv_k,
            connection_object=connection_object
        )
        logging.info(f"Retraining of Minibatch K-Means Clustering Model is Finished!!")
