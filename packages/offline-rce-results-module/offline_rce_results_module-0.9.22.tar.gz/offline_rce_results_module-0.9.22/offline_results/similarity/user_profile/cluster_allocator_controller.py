import numpy as np
from pandas import DataFrame, concat

from offline_results.common.constants import (
    CUSTOMER_ID,
    PAYTVPROVIDER_ID,
    GENDER,
    IS_PAYTV,
)
from offline_results.similarity.user_profile.common import SimilarityCommons
from offline_results.similarity.user_profile.config import (
    CLUSTER_NODE_LABEL,
    NEW_USER_CLUSTER_RELATIONSHIP_LABEL,
)
from offline_results.similarity.user_profile.plot_relations import PlotRelations
from offline_results.similarity.user_profile.utils.cluster_allocator_utils import (
    ClusterAllocatorUtils,
)
from offline_results.utils import class_custom_exception


class ClusterAllocatorController(ClusterAllocatorUtils):
    def __init__(self, connection_object):
        """
        Constructor to create graph object using
        the input connection details
        :param connection_object: graph
        connection object
        """

        ClusterAllocatorUtils.__init__(self, connection_object=connection_object)

    @class_custom_exception()
    def get_centroids(self):
        """
        Retrieve all the centroids for a
        particular cluster type from GraphDB
        :return: list of centroids and
        their properties
        """
        return self.graph.custom_query(
            query="g.V().hasLabel('centroid').has('"
            + CLUSTER_NODE_LABEL
            + "').path().by(elementMap())",
            payload={CLUSTER_NODE_LABEL: CLUSTER_NODE_LABEL},
        )[0]

    @class_custom_exception()
    def filter_centroids(self, is_paytv: bool, centroids: list) -> list:
        """
        Filter out the centroids that do not belong
        to the same paytv type as that of the user
        :param is_paytv: paytv indicator boolean
        :param centroids: list of centroids
        :return: list of centroids that are to be
        proceeded with
        """
        centroids_to_keep = []

        for centroid in centroids:
            if (
                IS_PAYTV in centroid[0].keys()
                and str(is_paytv) == centroid[0][IS_PAYTV]
            ):
                centroids_to_keep.append(centroid[0])

        return centroids_to_keep

    @class_custom_exception()
    def get_paytv_filtered_centroids(self):
        """
        Retrieve all centroids and filter them
        as per their respective paytv types
        into a dictionary. Dictionary key True
        holds centroids with is_paytv flag set
        to True and False for the rest
        :return: dictionary object
        """
        centroid_nodes = self.get_centroids()
        centroids = {
            "True": self.filter_centroids(is_paytv=True, centroids=centroid_nodes),
            "False": self.filter_centroids(is_paytv=False, centroids=centroid_nodes),
        }

        paytv_centroids = DataFrame.from_dict(centroids["True"])
        nopaytv_centroids = DataFrame.from_dict(centroids["False"])

        return paytv_centroids, nopaytv_centroids

    @class_custom_exception()
    def compute_user_centroid_scores(self, centroids: DataFrame, user: list) -> list:
        """
        Calculate Euclidean Distance scores between
        the considered user and all the centroids
        of the same paytv type.
        :param centroids: Dataframe object pandas
        :param user: list of features for the user
        :return: list of centroid scores
        """
        scores = []
        for index in range(len(centroids)):
            centroid = centroids.loc[index, :].values.tolist()
            scores.append(
                SimilarityCommons.get_distance(vector_a=user, vector_b=centroid)
            )
        return scores

    @class_custom_exception()
    def find_centroid_for_user(self, user: DataFrame, centroids: DataFrame) -> int:
        """
        Find the index of the most suitable
        centroid to be assigned for the user
        :param user: dataframe object pandas
        :param centroids: dataframe object pandas
        :return: integer value for the
        centroid index
        """
        centroids, user = self.process_user_centroid_records(
            centroids=centroids, user=user
        )
        scores = self.compute_user_centroid_scores(centroids=centroids, user=user)
        min_value = min(scores)
        return scores.index(min_value)

    @class_custom_exception()
    def check_features_available(self, users: DataFrame, index: int) -> bool:
        """
        Check if any feature values are available for the user
        :param users: dataframe object pandas
        :param index: user record index
        :return: Boolean indicator
        """
        if users.loc[index, GENDER] == -1 and (
            users.loc[index, PAYTVPROVIDER_ID] == -1
        ):
            return False
        return True

    @class_custom_exception()
    def dump_relations(self, is_paytv: bool, data=DataFrame):
        """
        Dump user-centroid relations
        :param is_paytv: boolean indicator
        :param data: dataframe object pandas
        :return: None, updates the relationships
         in graphDB
        """
        if len(data) == 0:
            return

        data[CLUSTER_NODE_LABEL] = data[CLUSTER_NODE_LABEL].astype(int)

        pr = PlotRelations(
            data=data,
            label=NEW_USER_CLUSTER_RELATIONSHIP_LABEL,
            connection_uri=self.connection_object,
        )

        pr.controller(destination_prop_label=CLUSTER_NODE_LABEL, is_paytv=is_paytv)

    @class_custom_exception()
    def find_cluster_label(self, users=DataFrame, centroids=DataFrame) -> DataFrame:
        """
        Find centroid for the users based on the
        dataframe supplied.
        :param users: paytv or nopaytv user dataframe
        :param centroids: paytv or no paytv centroids
        :return: dataframe with cluster label
        """
        if CLUSTER_NODE_LABEL not in users.columns:
            users[CLUSTER_NODE_LABEL] = np.nan

        users_na = users[users[CLUSTER_NODE_LABEL].isna()]
        users_int = users[~users[CLUSTER_NODE_LABEL].isna()]
        if len(users_na) > 0:
            users_na[CLUSTER_NODE_LABEL] = users_na[CLUSTER_NODE_LABEL].fillna(-1)
            users_na[CLUSTER_NODE_LABEL][users_na[CLUSTER_NODE_LABEL] == -1] = list(
                users_na[users_na[CLUSTER_NODE_LABEL] == -1].index
            )
            users_na[CLUSTER_NODE_LABEL] = users_na[CLUSTER_NODE_LABEL].apply(
                lambda x: self.find_centroid_for_user(
                    user=DataFrame(users.loc[x, :]).T, centroids=centroids
                )
            )

            users = concat([users_na, users_int], axis=0)

        return users.reset_index(drop=True)

    @class_custom_exception()
    def controller(
        self, users=DataFrame, path_pickle=None, streaming_chunked_index=int
    ):
        """
        Driver function for finding cluster labels
        for new users
        :param users: dataframe object pandas
        :param path_pickle: path where files will be saved
        :return: None, updates the relationships in graphDB
        """
        users = self.preprocess_user_attributes(users)

        paytv_centroids, nonpaytv_centroids = self.get_paytv_filtered_centroids()

        nonpaytv_users, paytv_users = self.get_paytv_wise_users(users)

        paytv_users = self.find_cluster_label(paytv_users, paytv_centroids)
        nonpaytv_users = self.find_cluster_label(nonpaytv_users, nonpaytv_centroids)

        paytv_users = paytv_users[[CUSTOMER_ID, CLUSTER_NODE_LABEL]]
        nonpaytv_users = nonpaytv_users[[CUSTOMER_ID, CLUSTER_NODE_LABEL]]

        # Uncomment below part if running from historical_data_utility repo
        # paytv_users.to_pickle(os.path.join(
        #     path_pickle,
        #     "paytv_streaming_user_clusters_chunk_{}.pkl".format(streaming_chunked_index)
        # )
        # )
        # nonpaytv_users.to_pickle(os.path.join(
        #     path_pickle,
        #     "nopaytv_streaming_user_clusters_chunk_{}.pkl".format(streaming_chunked_index)
        # )
        # )
        return paytv_users, nonpaytv_users
