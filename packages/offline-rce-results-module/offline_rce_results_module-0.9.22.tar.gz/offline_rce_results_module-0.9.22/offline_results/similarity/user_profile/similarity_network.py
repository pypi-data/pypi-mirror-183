from offline_results.common.config import (
    TO_READ_FROM_S3_PREFERENCES,
    TO_READ_FROM_S3_CLUSTERING_LABELS,
)
from offline_results.similarity.user_profile.all_users_generator import (
    SimilarityGenerator,
)
from offline_results.similarity.user_profile.config import SIMILARITY_THRESHOLD
from offline_results.utils import custom_exception, Logging


class SimilarityNetwork:
    @staticmethod
    @custom_exception()
    def dump_similarity_relations(connection_object, cluster_label: None):
        """
        Calculate similarity relationships among the users
        in the same cluster and dump these relationships
        into graphDB
        :param connection_object: graphDB connection object
        :param cluster_label: cluster label to be searched
        :return: None, simply dumps the computed
        relationships into graphDB
        """
        usg_paytv = SimilarityGenerator(
            db_graph=connection_object, sim_cutoff=SIMILARITY_THRESHOLD
        )
        preferences = TO_READ_FROM_S3_PREFERENCES
        clusters = TO_READ_FROM_S3_CLUSTERING_LABELS
        preferences.update(clusters)

        Logging.info("For PayTV users profile clusters....")
        paytv_similarity_score = usg_paytv.controller(
            use_features=preferences, is_paytv=True, cluster_label=cluster_label
        )

        usg_nopaytv = SimilarityGenerator(
            db_graph=connection_object, sim_cutoff=SIMILARITY_THRESHOLD
        )

        Logging.info("For NON-PayTV users profile clusters....")
        nopaytv_similarity_score = usg_nopaytv.controller(
            use_features=preferences, is_paytv=False, cluster_label=cluster_label
        )

        return paytv_similarity_score, nopaytv_similarity_score
