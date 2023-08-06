import logging
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation.main import \
    HomepageCatRecommendation
from offline_results.common.config import BUCKET_NAME, cluster_pkl_path_file
from offline_results.updater.preference_updater import PreferenceUpdater
from offline_results.updater.prepare_ubd import UserMap
from offline_results.updater.user_cluster_updater import ClusterUpdater
from offline_results.updater.user_node_updater import NodeUpdater
from offline_results.utils import custom_exception


class UpdaterMain:
    @staticmethod
    @custom_exception()
    def vdb_updater(redis_uri):
        """
        Driver function to call vdb updater network
        :param redis_uri: redis connection uri
        """
        NodeUpdater.vdb_updater(
            bucket_name=BUCKET_NAME,
            object_name=cluster_pkl_path_file,
            redis_uri=redis_uri,
        )

    @staticmethod
    @custom_exception()
    def ubd_updater(redis_uri):
        """
        Driver function to call ubd updater network
        :param redis_uri: redis connection uri
        """
        preference = PreferenceUpdater()
        ubd = UserMap.mapping_ubd(update=True)
        if ubd.empty:
            logging.error(f"No UBD data found in S3, Aborting")
            return
        merged_preferences = preference.controller(ubd=ubd, update=True)
        cluster_updater = ClusterUpdater()
        cluster_updater.controller(
            data=merged_preferences,
            bucket_name=BUCKET_NAME,
            object_name=cluster_pkl_path_file,
            redis_uri=redis_uri,
        )
        try:
            logging.info(f"MLC Model training started!!")
            cls = HomepageCatRecommendation(is_paytv=True)
            cls.model_training()
            cls = HomepageCatRecommendation(is_paytv=False)
            cls.model_training()
        except Exception as e:
            logging.error(f"Error in MLC Model training, {e}")
