import logging

import numpy as np
from graphdb import GraphDbConnection
from pandas import DataFrame, concat

from offline_results.common.constants import (
    CUSTOMER_ID,
    GENDER,
    AGE,
    STATUS,
    PAYTVPROVIDER_ID,
    NAN,
    IS_PAYTV,
)
from offline_results.repository.graph_db_connection import (
    config_connection_uri_reader,
    config_connection_uri_writer,
)
from offline_results.similarity.user_profile.cluster_allocator_controller import (
    ClusterAllocatorController,
)
from offline_results.similarity.user_profile.config import (
    CLUSTER_NODE_LABEL,
    NEW_USER_CLUSTER_RELATIONSHIP_LABEL,
)
from offline_results.updater.user_cluster_updater import ClusterUpdater
from offline_results.updater.utils import UpdaterUtils
from offline_results.utils import custom_exception


class NoPreferenceUsers:
    conn: GraphDbConnection

    def __init__(self):
        NoPreferenceUsers.conn = GraphDbConnection.from_uri(
            connection_uri_reader=config_connection_uri_reader,
            connection_uri_writer=config_connection_uri_writer,
        )

    @staticmethod
    @custom_exception()
    def cluster_assigner(
        user_profile: DataFrame,
        no_pref_users: DataFrame,
    ):
        """
        Assign clusters to no preferences users
        using streaming user clustering method
        :param user_profile: DataFrame object pandas
        :param no_pref_users: DataFrame object pandas
        :return Dataframe: DataFrame object pandas
        """
        user_profile = user_profile[
            user_profile[CUSTOMER_ID].isin(no_pref_users[CUSTOMER_ID])
        ]
        user_profile = user_profile[
            [CUSTOMER_ID, GENDER, AGE, STATUS, PAYTVPROVIDER_ID]
        ].reset_index(drop=True)
        user_profile[PAYTVPROVIDER_ID] = user_profile[PAYTVPROVIDER_ID].apply(
            lambda x: [{PAYTVPROVIDER_ID: int(float(x))}] if x != NAN else np.nan
        )
        cac = ClusterAllocatorController(connection_object=NoPreferenceUsers.conn)
        paytv_cluster_user, no_paytv_cluster_user = cac.controller(user_profile)
        return paytv_cluster_user, no_paytv_cluster_user

    @staticmethod
    @custom_exception()
    def prepare_cluster_data(
        paytv_cluster_user: DataFrame, no_paytv_cluster_user: DataFrame
    ):
        """
        Add fields to update cluster data on S3 and redis
        :param paytv_cluster_user: DataFrame object pandas
        :param no_paytv_cluster_user: DataFrame object pandas
        """
        if not paytv_cluster_user.empty:
            paytv_cluster_user[CLUSTER_NODE_LABEL] = paytv_cluster_user[
                CLUSTER_NODE_LABEL
            ].astype(int)
            paytv_cluster_user[IS_PAYTV] = "True"
        if not no_paytv_cluster_user.empty:
            no_paytv_cluster_user[CLUSTER_NODE_LABEL] = no_paytv_cluster_user[
                CLUSTER_NODE_LABEL
            ].astype(int)
            no_paytv_cluster_user[IS_PAYTV] = np.where(
                (no_paytv_cluster_user[CLUSTER_NODE_LABEL] != -999), "False", np.nan
            )
        cluster_data = concat([paytv_cluster_user, no_paytv_cluster_user], axis=0)
        return cluster_data.reset_index(drop=True)

    @staticmethod
    @custom_exception()
    def db_updater(
        cluster_data: DataFrame, bucket_name=None, object_name=None, redis_uri=None
    ):
        """
        Filter raw merged_df for users with no preferences
        are found in the graph
        :param cluster_data: Dataframe object pandas
        :param bucket_name: S3 bucket name
        :param object_name: S3 key path
        :param redis_uri: Redis uri
        """
        existing_clusters = UpdaterUtils.fetch_existing_cluster(
            bucket_name=bucket_name, object_name=object_name
        )
        existing_clusters[CUSTOMER_ID] = existing_clusters[CUSTOMER_ID].astype(str)
        logging.info(f"""Updating user-cluster relations on S3""")
        updated_cluster_data = ClusterUpdater.save_cluster_relation_s3(
            new_cluster_data=cluster_data,
            existing_cluster_data=existing_clusters,
            bucket_name=bucket_name,
            object_name=object_name,
        )
        logging.info(f"""Updating user-cluster relations on Redis""")
        ClusterUpdater.update_redis_cache(updated_cluster_data, redis_uri)

    @staticmethod
    @custom_exception()
    def controller(
        no_pref_users: DataFrame,
        user_profile: DataFrame,
        bucket_name=None,
        object_name=None,
        redis_uri=None,
    ):
        """
        Filter raw merged_df for users with no preferences
        are found in the graph
        :param no_pref_users: Dataframe object pandas
        :param user_profile: Dataframe object pandas
        :param bucket_name: S3 bucket name
        :param object_name: S3 key path
        :param redis_uri: Redis uri
        """

        paytv_cluster_user, no_paytv_cluster_user = NoPreferenceUsers.cluster_assigner(
            user_profile=user_profile, no_pref_users=no_pref_users
        )
        cluster_data = NoPreferenceUsers.prepare_cluster_data(
            paytv_cluster_user, no_paytv_cluster_user
        )
        NoPreferenceUsers.db_updater(
            cluster_data=cluster_data,
            bucket_name=bucket_name,
            object_name=object_name,
            redis_uri=redis_uri,
        )
        UpdaterUtils.drop_existing_rel(
            data=cluster_data, relation_label=NEW_USER_CLUSTER_RELATIONSHIP_LABEL
        )
        UpdaterUtils.dump_cluster_relations(
            dump_data=cluster_data,
            destination_label=CLUSTER_NODE_LABEL,
            relation_label=NEW_USER_CLUSTER_RELATIONSHIP_LABEL,
            df_attribute=CLUSTER_NODE_LABEL,
        )
