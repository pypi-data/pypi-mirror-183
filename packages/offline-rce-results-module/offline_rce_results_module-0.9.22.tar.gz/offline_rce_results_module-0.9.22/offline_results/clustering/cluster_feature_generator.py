import logging
from datetime import datetime

from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.clustering.centroids_generator import CentroidGenerator
from offline_results.clustering.cluster_generator import ClusterGenerator
from offline_results.clustering.mean_user_from_cluster import MeanUserFromCluster
from offline_results.common.constants import CUSTOMER_ID, CSV_EXTENSION, \
    PAYTVPROVIDER_ID, S3_PAYTV_PREFIX, S3_NONPAYTV_PREFIX, MINIBATCH_KMEANS, \
    IS_PAY_TV, CREATED_ON, UPDATED_ON, NO_PAY_TV, PAY_TV

logging.basicConfig(level=logging.INFO)


class ClusterFeaturesGenerator:

    @staticmethod
    def create_cluster_features(
            resource,
            s3_bucket_name,
            s3_object_name,
            user_profile,
            paytv: bool,
            k_value: int,
            connection_object=None
    ):
        user_profile[PAYTVPROVIDER_ID] = \
            user_profile[PAYTVPROVIDER_ID].fillna("").apply(list)
        for index in range(len(user_profile)):
            if len(user_profile.loc[index, PAYTVPROVIDER_ID]) == 0:
                user_profile.loc[index, PAYTVPROVIDER_ID] = -1
                continue
            paytvprovider_id = user_profile.loc[index, PAYTVPROVIDER_ID]
            user_profile.loc[index, PAYTVPROVIDER_ID] = \
                (paytvprovider_id[0])[PAYTVPROVIDER_ID]

        cluster_generator = ClusterGenerator(
            data=user_profile
        )
        cluster_generator.controller(paytv=paytv, k_value=k_value)

        cg = CentroidGenerator(
            user_features=user_profile,
            user_clusters=cluster_generator.clusters,
            connection_object=connection_object
        )
        cg.compute_centroids(
            s3_bucket_name=s3_bucket_name,
            s3_object_name=s3_object_name,
            resource=resource,
            paytv=paytv
        )
        print("Successfully dumped all the centroids data into S3...")
        rel = cluster_generator.clusters[[CUSTOMER_ID, MINIBATCH_KMEANS]]
        rel[IS_PAY_TV] = paytv
        rel[CREATED_ON] = datetime.utcnow().isoformat()
        rel[UPDATED_ON] = datetime.utcnow().isoformat()
        ClusterFeaturesGenerator.write_user_cluster_mapping_to_s3(
            resource=resource,
            s3_bucket_name=s3_bucket_name,
            s3_object_name=s3_object_name,
            df_to_upload=rel,
            paytv=paytv,
        )
        ctl = MeanUserFromCluster(pay_tv_label=NO_PAY_TV)
        ctl.update_mean_users()
        ctl = MeanUserFromCluster(pay_tv_label=PAY_TV)
        ctl.update_mean_users()
        return rel

    @staticmethod
    def write_user_cluster_mapping_to_s3(s3_bucket_name,
                                         s3_object_name,
                                         df_to_upload,
                                         resource,
                                         paytv):
        feature = S3_PAYTV_PREFIX + MINIBATCH_KMEANS if paytv \
            else S3_NONPAYTV_PREFIX + MINIBATCH_KMEANS

        ConnectS3().write_csv_to_s3(
            bucket_name=s3_bucket_name,
            object_name=s3_object_name + feature + CSV_EXTENSION,
            df_to_upload=df_to_upload,
            resource=resource
        )
        return True


