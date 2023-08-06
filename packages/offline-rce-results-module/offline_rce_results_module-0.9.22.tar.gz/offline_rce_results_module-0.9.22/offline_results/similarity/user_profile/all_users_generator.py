from typing import List

from graphdb.graph import GraphDb
from pandas import DataFrame

from offline_results.similarity.user_profile.common import SimilarityCommons
from offline_results.similarity.user_profile.config import (
    USER1,
    USER2,
    SCORE,
    SIMILARITY_WEIGHTS,
    DEFAULT_CLUSTER_LABEL,
)
from offline_results.similarity.user_profile.utils.utils import SimilarityUtils
from offline_results.utils import class_custom_exception, Logging


class SimilarityGenerator(SimilarityUtils):
    def __init__(self, db_graph, sim_cutoff: int):
        """
        Accepts the graphDB connection object
        and similarity cutoff as inputs
        :param db_graph: graphDB connection object
        :param sim_cutoff: similarity threshold
        """
        self.connection_object = db_graph
        self.db_graph = GraphDb.from_connection(self.connection_object)
        SimilarityUtils.__init__(self, db_graph=self.db_graph, sim_cutoff=sim_cutoff)

    @class_custom_exception()
    def compute_similarity(self, network, source_nodes: List, feature_weight=1):
        """
        Calculates and returns user-user similarity
        :param network: networkx instance
        :param source_nodes: user nodes
        :param feature_weight: fraction of contribution
        to overall similarity scores
        :return: None, updates the instance
        member of the class
        """
        relation_similarity_scores = DataFrame(columns=self.similarity_score.columns)
        for index1, user1 in enumerate(source_nodes):
            for index2, user2 in enumerate(source_nodes):
                if index2 <= index1:
                    continue
                neighbors_customer1 = network.neighbors(user1)
                neighbors_customer2 = network.neighbors(user2)
                (
                    neighbors_customer1_count,
                    neighbors_customer2_count,
                ) = self.get_neighbors_count(
                    neighbors_customer1=neighbors_customer1,
                    neighbors_customer2=neighbors_customer2,
                )
                overlap = self.get_neighborhood_overlap(
                    neighbors_customer1_count=neighbors_customer1_count,
                    neighbors_customer2_count=neighbors_customer2_count,
                    network=network,
                    user1=user1,
                    user2=user2,
                )
                self.validate_overlap(
                    overlap=overlap,
                    relation_similarity_scores=relation_similarity_scores,
                    user1=user1,
                    user2=user2,
                )
        self.update_similarity_table(
            relation_similarity_scores, feature_weight=feature_weight
        )

    @class_custom_exception()
    def compute_final_similarity_scores(self):
        """
        Group and add up the weighted similarity
        scores obtained from all te features considered
        :return: None, updates the instance Dataframe
        """
        self.similarity_score = (
            self.similarity_score.groupby([USER1, USER2])[SCORE].sum().reset_index()
        )

        if len(self.similarity_score[SCORE].unique()) > 1:
            self.similarity_score[SCORE] = SimilarityCommons.normalize(
                self.similarity_score[SCORE].tolist()
            )
        else:
            self.similarity_score[SCORE] = 1

        return self.similarity_score

    @class_custom_exception()
    def controller(self, use_features: dict, is_paytv: bool, cluster_label=None):
        """
        Driver function of the class
        :param use_features: list of features
        to be used for computing similarity
        :param is_paytv: boolean indicator
        :return: Updates the graphDB
        """

        # get all cluster labels for paytv type
        cluster_labels = self.get_cluster_labels(is_paytv=is_paytv)

        if cluster_label is None or cluster_label not in cluster_labels:
            Logging.info("Invalid cluster label input")
            return None

        cluster_labels = [cluster_label]

        for cluster in cluster_labels:

            if cluster == DEFAULT_CLUSTER_LABEL:
                Logging.info("Skipping default cluster label")
                continue

            Logging.info("Working on CLUSTER ID: " + str(cluster))

            # retrieve all 2-hop edges from cluster label node
            edges = self.get_graphdb_network(cluster_id=cluster, is_paytv=is_paytv)
            for feature in list(use_features.keys()):
                Logging.info("SIMILARITY for feature set: " + feature)

                # generate NetworkX object from the edges
                G = self.get_networkx_structure(
                    edges=edges,
                    dest_node_label=feature,
                    dest_node_property=(use_features[feature])[1],
                    relationship=(use_features[feature])[0],
                )

                # get all source (i.e. user) nodes
                source_nodes = self.get_source_nodes_from_networkx(network=G)

                if len(source_nodes) == 0:
                    Logging.info(
                        "No users with " + feature + " relationships in this cluster"
                    )
                    continue

                # convert network to undirected form
                X = self.get_undirected_network(network=G)

                # compute similarity using neighborhood overlap
                self.compute_similarity(
                    network=X,
                    source_nodes=source_nodes,
                    feature_weight=SIMILARITY_WEIGHTS[feature],
                )

        # group on users and add scores obtained from all the features
        final_similarity_score = self.compute_final_similarity_scores()
        # dump into GraphDB
        return final_similarity_score
