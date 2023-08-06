from itertools import chain

import numpy as np
from graphdb import Node, Relationship
from pandas import DataFrame, concat

from offline_results.common.config import HAS_PAYTV_PROVIDER, S3_RESOURCE
from offline_results.common.constants import (
    CUSTOMER_ID,
    USER_LABEL,
    LABEL,
    PROPERTIES,
    RELATIONSHIP,
    PAYTVPROVIDER_ID,
    IS_PAYTV,
    RATING,
    ATTRIBUTE1,
    SUBCATEGORY,
    ACTORS,
    AGE,
    RELATIONSHIP_NAME,
    DIRECTORS,
    DURATION,
    TOD,
    TAGS,
    CATEGORY,
    IS_PAY_TV,
    GENDER,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.similarity.user_profile.config import CLUSTER_NODE_LABEL
from offline_results.utils import custom_exception, Logging


class UpdaterUtils:
    @staticmethod
    @custom_exception()
    def fetch_existing_cluster(bucket_name=None, object_name=None) -> DataFrame:
        """
        Query the graph for cluster labels of the
        considered users and save them in DataFrame
        :return: Dataframe of customer_id and
        current assigned cluster label
        """
        existing_user_clusters = ConnectS3().read_compress_pickles_from_S3(
            bucket_name=bucket_name, object_name=object_name, resource=S3_RESOURCE
        )
        if "internal_table" in existing_user_clusters.columns:
            existing_user_clusters = existing_user_clusters.drop(
                columns=["internal_table", "internal_id"]
            )
        return existing_user_clusters

    @staticmethod
    @custom_exception()
    def drop_existing_rel(data, relation_label):
        """
        Function to drop edge from user node
        :param data: dataframe object pandas
        :param relation_label: name of edge
        """
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dropping {}".format(relation_label).center(100, "*"))
        customer_ids = data[CUSTOMER_ID].unique().tolist()
        for ids in customer_ids:
            try:
                node = Node.parse_obj(
                    {LABEL: USER_LABEL, PROPERTIES: {CUSTOMER_ID: str(ids)}}
                )
                relationship = Relationship.parse_obj(
                    {RELATIONSHIP_NAME: relation_label}
                )
                graph.delete_relationship_custom_query(node=node, rel=relationship)
            except Exception as e:
                Logging.error(
                    f"Error while dropping relation {relation_label} on graph, Error: {e}"
                )
        print("Successfully dropped all the {}...".format(relation_label))
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def dump_relations(
        dump_data: DataFrame,
        destination_label: str,
        relation_label: str,
        destination_property: str,
        df_attribute: str,
    ):
        """
        Function to dump user preferences in graphdb
        using custom query.
        :param dump_data: preference dataframe to be dumped
        :param destination_label: label of destination node
        :param relation_label: name of edge
        :param destination_property: property of destination node
        :param df_attribute: dataframe attribute
        """
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dumping {}".format(relation_label).center(100, "*"))
        for index in range(len(dump_data)):
            try:
                node_from = Node.parse_obj(
                    {
                        LABEL: USER_LABEL,
                        PROPERTIES: {
                            CUSTOMER_ID: str(dump_data.loc[index, CUSTOMER_ID])
                        },
                    }
                )
                node_to = Node.parse_obj(
                    {
                        LABEL: destination_label,
                        PROPERTIES: {
                            destination_property: int(
                                dump_data.loc[index, df_attribute]
                            )
                        },
                    }
                )
                graph.create_multi_relationship_without_upsert(
                    node_from,
                    node_to,
                    rel=Relationship(**{RELATIONSHIP: relation_label}),
                )
            except Exception as e:
                Logging.error(
                    f"Error while creating relation {relation_label} between "
                    f"customer_id:{dump_data.loc[index, CUSTOMER_ID]} & "
                    f"{destination_property}:{dump_data.loc[index, df_attribute]}, Error: {e}"
                )
                continue
        print("Successfully dumped all {}...".format(relation_label))
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def dump_str_relations(
        dump_data: DataFrame,
        destination_label: str,
        relation_label: str,
        destination_property: str,
        df_attribute: str,
    ):
        """
        Function to dump user preferences in graphdb
        using custom query.
        :param dump_data: preference dataframe to be dumped
        :param destination_label: label of destination node
        :param relation_label: name of edge
        :param destination_property: property of destination node
        :param df_attribute: dataframe attribute
        """
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dumping {}".format(relation_label).center(100, "*"))
        for index in range(len(dump_data)):
            try:
                node_from = Node.parse_obj(
                    {
                        LABEL: USER_LABEL,
                        PROPERTIES: {
                            CUSTOMER_ID: str(dump_data.loc[index, CUSTOMER_ID])
                        },
                    }
                )
                node_to = Node.parse_obj(
                    {
                        LABEL: destination_label,
                        PROPERTIES: {
                            destination_property: str(
                                dump_data.loc[index, df_attribute]
                            )
                        },
                    }
                )
                graph.create_multi_relationship_without_upsert(
                    node_from,
                    node_to,
                    rel=Relationship(**{RELATIONSHIP: relation_label}),
                )
            except Exception as e:
                Logging.error(
                    f"Error while creating relation {relation_label} between "
                    f"customer_id:{dump_data.loc[index, CUSTOMER_ID]} & "
                    f"{destination_property}:{dump_data.loc[index, df_attribute]}, Error: {e}"
                )
                continue
        print("Successfully dumped all {}...".format(relation_label))
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def dump_cluster_relations(
        dump_data: DataFrame,
        destination_label: str,
        relation_label: str,
        df_attribute: str,
    ):
        """
        Function to dump user preferences in graphdb
        using custom query.
        :param dump_data: preference dataframe to be dumped
        :param destination_label: label of destination node
        :param relation_label: name of edge
        :param df_attribute: dataframe attribute
        """
        dump_data = dump_data.reset_index(drop=True)
        graph = ANGraphDb.new_connection_config().graph
        print("Starting dumping {}".format(relation_label).center(100, "*"))
        for index in range(len(dump_data)):
            try:
                node_from = Node.parse_obj(
                    {
                        LABEL: USER_LABEL,
                        PROPERTIES: {
                            CUSTOMER_ID: str(dump_data.loc[index, CUSTOMER_ID])
                        },
                    }
                )
                node_to = Node.parse_obj(
                    {
                        LABEL: destination_label,
                        PROPERTIES: {
                            CLUSTER_NODE_LABEL: int(dump_data.loc[index, df_attribute]),
                            IS_PAY_TV: str(dump_data.loc[index, IS_PAYTV]),
                        },
                    }
                )
                if int(dump_data.loc[index, df_attribute]) == -999:
                    node_to = Node.parse_obj(
                        {
                            LABEL: destination_label,
                            PROPERTIES: {
                                CLUSTER_NODE_LABEL: int(
                                    dump_data.loc[index, df_attribute]
                                )
                            },
                        }
                    )
                graph.create_multi_relationship_without_upsert(
                    node_from,
                    node_to,
                    rel=Relationship(**{RELATIONSHIP: relation_label}),
                )
            except Exception as e:
                Logging.error(
                    f"Error while creating relation {relation_label} on graph, Error: {e}"
                )
                continue
        print("Successfully dumped all {}...".format(relation_label))
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def find_paytv_users(data: DataFrame):
        """
        Fetch paytv users from graph
        :param data: list of customer_ids
        """
        user_list = data[CUSTOMER_ID].tolist()
        users = DataFrame()
        graph = ANGraphDb.new_connection_config().graph
        print("Fetching paytv users from graph".center(100, "*"))
        for user in user_list:
            try:
                response = graph.custom_query(
                    query=f"""g.V().has('{USER_LABEL}','{CUSTOMER_ID}', '{user}').
                    outE('{HAS_PAYTV_PROVIDER}').project('{CUSTOMER_ID}','{IS_PAY_TV}','{PAYTVPROVIDER_ID}').
                    by(outV().values('{CUSTOMER_ID}')).
                    by(outV().values('{IS_PAY_TV}')).
                    by(inV().values('{PAYTVPROVIDER_ID}'))""",
                    payload={
                        USER_LABEL: USER_LABEL,
                        CUSTOMER_ID: CUSTOMER_ID,
                        IS_PAY_TV: IS_PAY_TV,
                        HAS_PAYTV_PROVIDER: HAS_PAYTV_PROVIDER,
                        PAYTVPROVIDER_ID: PAYTVPROVIDER_ID,
                    },
                )
                if len(response) > 0:
                    row_to_add = response[0][0]
                    users = concat([users, DataFrame([row_to_add])], ignore_index=True)
            except Exception as e:
                Logging.error(
                    f"Error while fetching paytv users from graph, Error: {e}"
                )

        # there is a possibility that input dataframe doesn't contain any user_id having paytv status
        # in that case else condition will assign PAYTVPROVIDER_ID column as nan
        if not users.empty:
            data = data.merge(users, on=CUSTOMER_ID, how="left")
            data[IS_PAY_TV] = data[IS_PAY_TV].fillna(False)
        else:
            data[PAYTVPROVIDER_ID] = np.nan
            data[IS_PAY_TV] = False
        graph.connection.close()

        return data

    @staticmethod
    @custom_exception()
    def fetch_user_in_graph(user_ids: list):
        """
        Fetch user nodes available in graph
        :param user_ids: List of user ids to be searched
        """
        id_found = []
        graph = ANGraphDb.new_connection_config().graph
        print("Fetching user data from graph".center(100, "*"))
        for _id in user_ids:
            query = f"""g.V().has('{USER_LABEL}', '{CUSTOMER_ID}', '{_id}').match(
                    __.as("c").values('{CUSTOMER_ID}').as('{CUSTOMER_ID}'),
                    __.as("c").values('{GENDER}').as('{GENDER}'),
                    __.as("c").values('{AGE}').as('{AGE}')
                    ).select('{CUSTOMER_ID}', '{GENDER}', '{AGE}')"""
            try:
                response = graph.custom_query(
                    query=query,
                    payload={
                        USER_LABEL: USER_LABEL,
                        CUSTOMER_ID: CUSTOMER_ID,
                        GENDER: GENDER,
                        AGE: AGE,
                    },
                )
                if len(response) > 0:
                    id_found.append(response[0][0])
            except Exception as e:
                Logging.error(f"Error while fetching users from graph, Error: {e}")
        graph.connection.close()
        return DataFrame(id_found)

    @staticmethod
    @custom_exception()
    def fetch_centroids():
        """
        Fetch kmeans centroid from the graph
        """
        graph = ANGraphDb.new_connection_config().graph
        response = graph.custom_query(
            query=f"""g.V().hasLabel('centroid').has('{CLUSTER_NODE_LABEL}').
            path().by(elementMap())""",
            payload={CLUSTER_NODE_LABEL: CLUSTER_NODE_LABEL},
        )
        graph.connection.close()
        tmp = {}
        centroids = DataFrame()
        for index, value in enumerate(response):
            for i, j in enumerate(value):
                tmp[CLUSTER_NODE_LABEL] = j[0][CLUSTER_NODE_LABEL]
                tmp[IS_PAYTV] = j[0][IS_PAYTV]
                tmp[RATING] = j[0][RATING]
                tmp[ATTRIBUTE1] = j[0][ATTRIBUTE1]
                tmp[CATEGORY] = j[0][CATEGORY]
                tmp[SUBCATEGORY] = j[0][SUBCATEGORY]
                tmp[ACTORS] = j[0][ACTORS]
                tmp[DIRECTORS] = j[0][DIRECTORS]
                tmp[TAGS] = j[0][TAGS]
                tmp[DURATION] = j[0][DURATION]
                tmp[TOD] = j[0][TOD]
                centroids = concat([centroids, DataFrame([tmp])])
        return centroids.reset_index(drop=True)

    @staticmethod
    @custom_exception()
    def fetch_user_preference(
        data: DataFrame, rel_label: str, destination_property: str
    ):
        pref_list = []
        print("Fetching {} from graph".format(rel_label).center(100, "*"))
        graph = ANGraphDb.new_connection_config().graph
        for _ids in data[CUSTOMER_ID].tolist():
            query = f"""g.V().has('{USER_LABEL}', '{CUSTOMER_ID}', '{_ids}').
                    outE('{rel_label}').project('{CUSTOMER_ID}', '{destination_property}').
                    by(outV().values('{CUSTOMER_ID}')).
                    by(inV().values('{destination_property}'))"""
            try:
                response = graph.custom_query(
                    query=query,
                    payload={
                        USER_LABEL: USER_LABEL,
                        CUSTOMER_ID: CUSTOMER_ID,
                        rel_label: rel_label,
                        destination_property: destination_property,
                    },
                )
                if len(response) > 0:
                    pref_list.append(response[0])
            except Exception as e:
                Logging.error(
                    f"Error while fetching {rel_label} from graph, Error: {e}"
                )
        graph.connection.close()
        return DataFrame(list(chain.from_iterable(pref_list)))
