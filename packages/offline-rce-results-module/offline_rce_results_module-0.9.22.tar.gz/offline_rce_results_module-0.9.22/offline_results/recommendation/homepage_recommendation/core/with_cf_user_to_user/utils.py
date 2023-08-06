from functools import reduce

from cachetools import cached, TTLCache
from graphdb.graph import GraphDb
from pandas import DataFrame, concat, merge

from offline_results.common.config import TO_READ_FROM_S3_PREFERENCES
from offline_results.common.constants import (
    CUSTOMER_ID,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    USER_LABEL,
    VIEWED,
    IS_PAYTV,
    VIEW_COUNT,
    CONTENT_ID,
    VIEW_HISTORY,
    HOMEPAGE_ID,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.similarity.user_profile.all_users_generator import (
    SimilarityGenerator,
)
from offline_results.similarity.user_profile.config import (
    CLUSTER_NODE_LABEL,
    DEFAULT_CLUSTER_LABEL,
    USER1,
    USER2,
    SIMILARITY_THRESHOLD,
)
from offline_results.utils import class_custom_exception, Logging


class UserViewershipUtils:
    def __init__(
        self, connection_object, s3_resource, s3_bucket_name: str, s3_object_name: str
    ):
        """
        In addition to the expected parameters, this constructor performs
        the following initial computations:
        1) Retrieve content homepage mapping, so that each new function call
        to the controller does not repeat this step.
        2) All homepage nodes and their required properties, so that each new
        function call to the controller does not repeat this step.
        3) Prepare paytv-wise list of users in each user-profile cluster. The
        intermediate variables created during this process and released
        within the constructor itself.
        @param connection_object: GraphDB connection object
        @param s3_resource: S3 connection resource
        @param s3_bucket_name: S3 connection bucket name string value
        @param s3_object_name: S3 connection object name string value
        """
        self.connection_object = connection_object
        self.graph = GraphDb.from_connection(connection_object)
        self.resource = s3_resource
        self.bucket_name = s3_bucket_name
        self.object_name = s3_object_name
        self.paytv_user_cluster_mapping = {}
        self.nonpaytv_user_cluster_mapping = {}
        self.paytv_cluster_wise_users = DataFrame()
        self.nonpaytv_cluster_wise_users = DataFrame()

        # retrieving content-homepage mapping from graphDB
        self.content_homepage_mapping = DataFrame(
            RecommendationUtils.get_homepage_for_contents(graph=self.graph)
        )

        # retrieving homepage related attributes from graphDB
        self.homepage_meta = DataFrame(
            RecommendationUtils.get_homepage_id_title_map(
                graph=self.graph, get_status=True
            )
        )

        # creating intermediate pair of paytv-wise list of users in
        # each user-profile cluster
        paytv_user_clusters = ConnectS3().read_csv_from_s3(
            resource=self.resource,
            bucket_name=self.bucket_name,
            object_name=self.object_name
            + "mapping_paytv_"
            + CLUSTER_NODE_LABEL
            + ".csv",
        )

        nonpaytv_user_clusters = ConnectS3().read_csv_from_s3(
            resource=self.resource,
            bucket_name=self.bucket_name,
            object_name=self.object_name
            + "mapping_nonpaytv_"
            + CLUSTER_NODE_LABEL
            + ".csv",
        )

        # creating the mapping using the above intermediates
        # the first two are paytv-wise mappings of type:
        # { <customer_id> : <cluster_id> }

        self.paytv_user_cluster_mapping = dict(
            zip(
                paytv_user_clusters[CUSTOMER_ID].astype(str),
                paytv_user_clusters[CLUSTER_NODE_LABEL],
            )
        )

        self.nonpaytv_user_cluster_mapping = dict(
            zip(
                nonpaytv_user_clusters[CUSTOMER_ID].astype(str),
                nonpaytv_user_clusters[CLUSTER_NODE_LABEL],
            )
        )

        # the following two are paytv-wise mappings of type:
        # { <cluster_id> : [customer1, customer2,...., customerN] }

        self.paytv_cluster_wise_users = (
            paytv_user_clusters.groupby(CLUSTER_NODE_LABEL)[CUSTOMER_ID]
            .apply(list)
            .reset_index()
        )

        self.nonpaytv_cluster_wise_users = (
            nonpaytv_user_clusters.groupby(CLUSTER_NODE_LABEL)[CUSTOMER_ID]
            .apply(list)
            .reset_index()
        )

        # releasing the non-required intermediate variables from memory
        del paytv_user_clusters
        del nonpaytv_user_clusters

    @class_custom_exception()
    def get_cluster_id_for_user(self, customer_id: str):
        """
        Identify the cluster_id for the specified user. This process
        includes 3 conditions:
        1) Check the occurrence of this customer_id in paytv cluster
        mapping. If the user exists, return its cluster_id, else proceed
        into the except block raised due to KeyError.
        2) Check the occurrence of this customer_id in non-paytv cluster
        mapping. If the user exists, return its cluster_id, else proceed
        into the except block raised due to KeyError.
        3) If arrived at the nested except block, it can be inferred
        that user exists in the default cluster node
        @param customer_id: customer_id string value
        @return: cluster label and paytv status
        """
        try:
            return self.paytv_user_cluster_mapping[customer_id], True
        except KeyError:
            try:
                return self.nonpaytv_user_cluster_mapping[customer_id], False
            except KeyError:
                return DEFAULT_CLUSTER_LABEL, None

    @class_custom_exception()
    def get_all_users(self, cluster_id: int, is_paytv: bool) -> list:
        """
        Retrieve all users belonging to the specified cluster_id and
        paytv_status. This information is retrieved from one of the
        mapping prepared during constructor initialisation, instead of
        by interacting with graphDB, which prevents time-overhead.
        @param cluster_id: cluster_id integer value
        @param is_paytv: boolean paytv status
        @return: list of users belonging to the mentioned cluster_id
        and paytv status
        """
        cluster_wise_users = (
            self.paytv_cluster_wise_users
            if is_paytv
            else self.nonpaytv_cluster_wise_users
        )

        return (
            cluster_wise_users[cluster_wise_users[CLUSTER_NODE_LABEL] == cluster_id]
            .reset_index(drop=True)
            .loc[0, CUSTOMER_ID]
        )

    @class_custom_exception()
    def get_contents_viewed(self, customer_id: str, is_paytv: bool) -> DataFrame:
        """
        For the customer_id passed into the parameter, find out
        the contents viewed and their corresponding attributes
        from graphDB. The function also accepts an additional
        paytv status parameter so as to return that value as part
        of the generated result attribute set.
        @param customer_id: customer id string value
        @param is_paytv: boolean paytv status
        @return: Dataframe object pandas
        """
        content_paytv_type = PAY_TV_CONTENT if is_paytv else NO_PAY_TV_CONTENT

        viewed_feature_list = []

        response = self.graph.custom_query(
            query=f"""g.V().hasLabel('{USER_LABEL}').
            has('{CUSTOMER_ID}','{customer_id}')
            .outE('{VIEWED}').inV().
            hasLabel('{content_paytv_type}').
            path().by(elementMap())"""
        )

        # reformat the obtained result by fetching the necessary
        # information from the custom query results. The view_history
        # information from the relationship property is retrieved as is.

        for index, ele in enumerate(response):
            for i in range(len(response[index])):
                customer_id = response[index][i][0][CUSTOMER_ID]
                view_count = response[index][i][1][VIEW_COUNT]
                view_history = response[index][i][1][VIEW_HISTORY]
                content_id = response[index][i][2][CONTENT_ID]
                view_dict = {
                    CUSTOMER_ID: customer_id,
                    CONTENT_ID: content_id,
                    VIEW_COUNT: view_count,
                    VIEW_HISTORY: view_history,
                }
                viewed_feature_list.append(view_dict)

        result = DataFrame(viewed_feature_list).reset_index(drop=True)

        # add an additional attribute to reflect the paytv status
        result[IS_PAYTV] = is_paytv
        return result

    @class_custom_exception()
    def get_similar_users(
        self, customer_id: str, cluster_id: int, is_paytv: bool, graph
    ) -> list:
        """
        Identify the set of users similar to the customer_id passed into
        the parameter. In order to obtain these users, the cluster_id to
        which the customer_id belongs is also passed as an additional
        parameter, along with the corresponding paytv status. The entire
        procedure involves the following steps.
        1) Identify all the similar users belonging to the same cluster.
        2) Filter to keep only the similarity information specific to
        customer_id passed into the parameter.
        3) Return the unique list of users similar to customer_id.
        If None, return an empty list
        @param customer_id: customer id string value
        @param cluster_id: cluster id integer value
        @param is_paytv: boolean paytv status
        @return: list of users similar to customer_id
        """
        similarity_generator = SimilarityGenerator(
            db_graph=graph, sim_cutoff=SIMILARITY_THRESHOLD
        )

        similarity_generator.controller(
            use_features=TO_READ_FROM_S3_PREFERENCES,
            is_paytv=is_paytv,
            cluster_label=cluster_id,
        )

        # fetch all possible similarity relationships within the
        # [cluster_id, is_paytv] cluster
        similar_users = similarity_generator.similarity_score[[USER1, USER2]]

        # filter to keep information specific to the customer_id
        # passed into the parameter
        similar_users = concat(
            [
                similar_users[similar_users[USER1] == customer_id],
                similar_users[similar_users[USER2] == customer_id],
            ],
            axis=0,
        ).reset_index(drop=True)

        # if no user remains after filtration, return an empty list
        if len(similar_users) == 0:
            return []

        # format to prepare the list of unique users from the result,
        # while dropping the customer_id from the final result
        similar_users1 = similar_users[USER1].tolist()
        similar_users2 = similar_users[USER2].tolist()
        unique_users = similar_users1
        unique_users.extend(similar_users2)
        unique_users.remove(customer_id)

        return list(set(unique_users))

    @cached(cache=TTLCache(maxsize=200, ttl=60 * 20))
    @class_custom_exception()
    def content_viewership(
        self,
        content_list,
        is_pay_tv,
    ):
        try:
            Logging.info(f"start fetching the users for given content_ids .....")
            pay_tv_content_label = (
                PAY_TV_CONTENT if is_pay_tv is True else NO_PAY_TV_CONTENT
            )
            query = f"""
                    g.V()
                    .has('{pay_tv_content_label}', '{CONTENT_ID}', within({list(set(content_list))}))
                    .inE('{VIEWED}').outV()
                    .hasLabel('{USER_LABEL}')
                    .path()
                    .by(valueMap('{CUSTOMER_ID}', '{CONTENT_ID}', '{VIEW_COUNT}','{VIEW_HISTORY}'))
                    """
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={})
            graph.connection.close()
            if len(data) == 0:
                return []
            data = [rec for idx in data for rec in idx]
            data = [
                reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
                for item in data
            ]
            df = DataFrame(data)
            df[CONTENT_ID] = df[CONTENT_ID].apply(lambda x: x[0])
            df[CUSTOMER_ID] = df[CUSTOMER_ID].apply(lambda x: x[0])
            return df
        except Exception as e:
            Logging.error(
                f"Error while fetching content viewership of content len {len(content_list)}. Error: {e}"
            )

    @class_custom_exception()
    def get_similar_users_viewership(self, similar_users: list) -> DataFrame:
        """
        find out the contents viewed by each user similar to the customer_id
        under consideration. This information is retrieved from graphDB, user-wise.
        Moreover, this procedure is carried out paytv-wise so as to preserve
        the content's paytv-information to be returned as part of the final result
        @param similar_users: list of users similar to customer_id under consideration
        @return: Dataframe object pandas
        """
        viewership_result = DataFrame()
        for index, user in enumerate(similar_users):
            Logging.info(
                "Fetching viewership of similar user "
                + str(index)
                + " of "
                + str(len(similar_users))
            )

            # finding the viewership for pay_tv contents
            Logging.info("Fetching pay_tv_contents....")
            viewership_result = concat(
                [
                    viewership_result,
                    self.get_contents_viewed(customer_id=user, is_paytv=True),
                ],
                axis=0,
            ).reset_index(drop=True)

            # finding the viewership for non_pay_tv contents
            Logging.info("Fetching no_pay_tv_contents...")
            viewership_result = concat(
                [
                    viewership_result,
                    self.get_contents_viewed(customer_id=user, is_paytv=False),
                ],
                axis=0,
            ).reset_index(drop=True)
        return viewership_result

    @class_custom_exception()
    def format_final_result(
        self, content_paytv_type: DataFrame, content_view_counts: DataFrame
    ) -> DataFrame:
        """
        Consolidate all the intermediate results generated during
        constructor initialisation, similarity generation and other
        formatting procedures to prepare the final result of contents
        as part of user-user CF recommendation result, sorted in the
        order of decreasing view count among the similar users.
        @param content_paytv_type: Dataframe object pandas
        @param content_view_counts: Dataframe object pandas
        @return: Dataframe object pandas
        """

        # reformat data types for sanity
        content_view_counts[CONTENT_ID] = content_view_counts[CONTENT_ID].astype(int)

        content_paytv_type[CONTENT_ID] = content_paytv_type[CONTENT_ID].astype(int)

        # merge the two dfs passed into the parameter to get
        # content paytv type and view count into a single df object
        result = merge(content_view_counts, content_paytv_type, on=CONTENT_ID)

        # merge the above result with content homepage mapping to
        # get the homepage id into single df object
        result = merge(result, self.content_homepage_mapping, on=CONTENT_ID)

        # merge the above result with homepage metadata to get all
        # homepage related information into a single df object
        result = merge(result, self.homepage_meta, on=HOMEPAGE_ID)

        # sort the result in the order of decreasing view counts
        return result.sort_values(by=VIEW_COUNT, ascending=False).reset_index(drop=True)
