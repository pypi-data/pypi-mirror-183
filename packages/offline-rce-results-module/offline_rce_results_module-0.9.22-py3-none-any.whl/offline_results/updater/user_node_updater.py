import time
from datetime import datetime

import numpy as np
import pandas as pd
from graphdb.schema import Node
from pandas import DataFrame, get_dummies

from offline_results.common.config import (
    S3_RESOURCE,
    BUCKET_NAME,
    HAS_RATING_PREFERENCE,
    MAPPING_KEY,
    HAS_PAYTV_PROVIDER,
    HAS_ACTOR_PREFERENCE,
    HAS_DIRECTOR_PREFERENCE,
    HAS_ATTRIBUTE1_PREFERENCE,
    HAS_CATEGORY_PREFERENCE,
    HAS_SUBCATEGORY_PREFERENCE,
    HAS_DURATION_PREFERENCE,
    HAS_TOD_PREFERENCE,
)
from offline_results.common.constants import (
    LABEL,
    PROPERTIES,
    USER_LABEL,
    CUSTOMER_ID,
    UD_KEY,
    STATUS,
    PAYTVPROVIDER_ID,
    PAYTV_PROVIDER,
    TAGS,
    HAS_TAG_PREFERENCE,
    TAGS_ID,
    ACTOR_ID,
    RATING,
    ATTRIBUTE1,
    CATEGORY_ID,
    SUBCATEGORY_ID,
    VALUE,
    TOD,
    SUBCATEGORY,
    CATEGORY,
    DIRECTORS,
    ACTORS,
    NEW,
    MATCHED,
    UNMATCHED,
    PREF_FEATURES,
    DURATION,
    USER_PAYTV_FILENAME,
    NEW_PAYTV,
    NAN,
    INNER,
    IS_PAY_TV_NEW,
    IS_PAY_TV,
    ACTIVE_LOWER,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.updater.demographics import PreprocessDemography
from offline_results.updater.no_preference_users import NoPreferenceUsers
from offline_results.updater.user_cluster_updater import ClusterUpdater
from offline_results.updater.utils import UpdaterUtils
from offline_results.utils import custom_exception, Logging


class NodeUpdater:
    @staticmethod
    @custom_exception()
    def process_s3_data(
        bucket_name=None,
    ) -> DataFrame:
        """
        Function to read current month file from s3
        """
        user_profile = DataFrame()
        now = datetime.now()
        path_file = "vdb/{year}/{month_name}/customer.pkl".format(
            year=now.year,
            month_name=now.strftime("%B"),
        )
        try:
            user_profile = ConnectS3().read_compress_pickles_from_S3(
                bucket_name=bucket_name, object_name=path_file, resource=S3_RESOURCE
            )
            if user_profile.empty:
                return user_profile
            user_profile = user_profile.drop(columns=user_profile.columns[0:2].tolist())
            user_profile = user_profile.replace(to_replace=NAN, value=np.nan)
            user_paytv = ConnectS3().read_compress_pickles_from_S3(
                bucket_name=bucket_name,
                object_name=MAPPING_KEY + USER_PAYTV_FILENAME,
                resource=S3_RESOURCE,
            )
            if "internal_table" in user_paytv.columns:
                user_paytv = user_paytv.drop(columns=["internal_table", "internal_id"])
            user_paytv[STATUS] = user_paytv[STATUS].str.lower()
            user_profile = user_profile.merge(user_paytv, on=UD_KEY, how="left")
            user_profile[STATUS] = user_profile[STATUS].fillna(NAN)
            user_profile = user_profile.rename(columns={PAYTVPROVIDER_ID: NEW_PAYTV})
            user_profile = PreprocessDemography().controller(df=user_profile, update=True)
        except Exception as e:
            Logging.error(f"Error while reading file from S3, Error: {e}")
        return user_profile

    @staticmethod
    @custom_exception()
    def find_paytv_status(user_profile: DataFrame):
        """
        Find unmatched paytv ids from new and existing ones
        in the graph
        :param user_profile: Dataframe object pandas
        """
        paytv_df = UpdaterUtils.find_paytv_users(user_profile)
        paytv_df[NEW_PAYTV] = paytv_df[NEW_PAYTV].fillna(NAN)
        paytv_df[PAYTVPROVIDER_ID] = paytv_df[PAYTVPROVIDER_ID].fillna(NAN)
        paytv_df[PAYTVPROVIDER_ID] = paytv_df[PAYTVPROVIDER_ID].apply(
            lambda x: int(float(x)) if x != NAN else NAN
        )
        paytv_df[NEW] = np.where(
            (paytv_df[NEW_PAYTV] == paytv_df[PAYTVPROVIDER_ID]), MATCHED, UNMATCHED
        )
        condition = [
            (paytv_df[NEW] == UNMATCHED) & (paytv_df[STATUS] == ACTIVE_LOWER),
            (paytv_df[NEW_PAYTV] != NAN) & (paytv_df[STATUS] == ACTIVE_LOWER),
            (paytv_df[STATUS] != ACTIVE_LOWER) & (paytv_df[IS_PAY_TV] == True),
            (paytv_df[NEW_PAYTV] == NAN) & (paytv_df[IS_PAY_TV] == True),
        ]
        value = [True, True, False, False]
        paytv_df[IS_PAY_TV_NEW] = np.select(condition, value, False)
        user_profile = paytv_df.copy()
        user_profile = user_profile.drop(columns=[NEW, PAYTVPROVIDER_ID, IS_PAY_TV])
        user_profile = user_profile.rename(
            {IS_PAY_TV_NEW: IS_PAY_TV, NEW_PAYTV: PAYTVPROVIDER_ID}, axis=1
        )
        paytv_df = paytv_df[
            ((paytv_df[NEW] == UNMATCHED) & (paytv_df[STATUS] == ACTIVE_LOWER))
            | (paytv_df[IS_PAY_TV] != paytv_df[IS_PAY_TV_NEW])
        ]
        paytv_df = paytv_df.drop(columns=[PAYTVPROVIDER_ID, NEW])
        paytv_df = paytv_df.rename({NEW_PAYTV: PAYTVPROVIDER_ID}, axis=1)
        paytv_df[PAYTVPROVIDER_ID] = paytv_df[PAYTVPROVIDER_ID].apply(str)
        paytv_df[PAYTVPROVIDER_ID] = paytv_df[PAYTVPROVIDER_ID].apply(
            lambda x: int(float(x)) if x != NAN else NAN
        )
        paytv_df = paytv_df.reset_index(drop=True)
        return paytv_df, user_profile

    @staticmethod
    @custom_exception()
    def get_preference(data: DataFrame):
        """
        Function to fetch user preference from
        graph
        :param data: Dataframe object pandas
        """
        pref_list = []
        actor_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_ACTOR_PREFERENCE, destination_property=ACTOR_ID
        )
        actor_preference = actor_preference.rename({ACTOR_ID: ACTORS}, axis=1)
        pref_list.append(actor_preference)
        time.sleep(5)
        director_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_DIRECTOR_PREFERENCE, destination_property=ACTOR_ID
        )
        director_preference = director_preference.rename({ACTOR_ID: DIRECTORS}, axis=1)
        pref_list.append(director_preference)
        time.sleep(5)
        tags_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_TAG_PREFERENCE, destination_property=TAGS_ID
        )
        tags_preference = tags_preference.rename({TAGS_ID: TAGS}, axis=1)
        pref_list.append(tags_preference)
        time.sleep(5)
        rating_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_RATING_PREFERENCE, destination_property=RATING
        )
        pref_list.append(rating_preference)
        time.sleep(5)
        attribute1_preference = UpdaterUtils.fetch_user_preference(
            data=data,
            rel_label=HAS_ATTRIBUTE1_PREFERENCE,
            destination_property=ATTRIBUTE1,
        )
        pref_list.append(attribute1_preference)
        time.sleep(5)
        category_preference = UpdaterUtils.fetch_user_preference(
            data=data,
            rel_label=HAS_CATEGORY_PREFERENCE,
            destination_property=CATEGORY_ID,
        )
        category_preference = category_preference.rename(
            {CATEGORY_ID: CATEGORY}, axis=1
        )
        pref_list.append(category_preference)
        time.sleep(5)
        subcategory_preference = UpdaterUtils.fetch_user_preference(
            data=data,
            rel_label=HAS_SUBCATEGORY_PREFERENCE,
            destination_property=SUBCATEGORY_ID,
        )
        subcategory_preference = subcategory_preference.rename(
            {SUBCATEGORY_ID: SUBCATEGORY}, axis=1
        )
        pref_list.append(subcategory_preference)
        time.sleep(5)
        tod_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_TOD_PREFERENCE, destination_property=VALUE
        )
        tod_preference = tod_preference.rename({VALUE: TOD}, axis=1)
        pref_list.append(tod_preference)
        time.sleep(5)
        duration_preference = UpdaterUtils.fetch_user_preference(
            data=data, rel_label=HAS_DURATION_PREFERENCE, destination_property=VALUE
        )
        duration_preference = duration_preference.rename({VALUE: DURATION}, axis=1)
        pref_list.append(duration_preference)

        return pref_list

    @staticmethod
    @custom_exception()
    def prepare_merged_df(pref_list: list, paytv_df: DataFrame):
        """
        Function to prepare merged preference df from
        list of dataframe
        :param pref_list: List of dataframe
        :param paytv_df: Dataframe object pandas
        """
        merged_df = DataFrame()
        merged_df[CUSTOMER_ID] = paytv_df[CUSTOMER_ID]
        for df in pref_list:
            column = df.columns[df.columns != CUSTOMER_ID]
            tmp_df = df.groupby(CUSTOMER_ID)[column[0]].apply(list).reset_index()
            merged_df = pd.merge(merged_df, tmp_df, on=CUSTOMER_ID, how="outer")
        return merged_df

    @staticmethod
    @custom_exception()
    def get_dummy_features(merged_df: DataFrame):
        """
        Function to get dummy features from dataframe
        :param merged_df: Dataframe object pandas
        """
        raw_merged_df = DataFrame()
        raw_merged_df[CUSTOMER_ID] = merged_df[CUSTOMER_ID]
        for i in PREF_FEATURES:
            tmp_df = merged_df[i].apply(pd.Series).stack().reset_index(1, drop=True)
            tmp_df = pd.Series(tmp_df, name="tmp")
            tmp_df = merged_df.join(tmp_df).drop(i, axis=1).rename(columns={"tmp": i})
            tmp_df = get_dummies(tmp_df, columns=[i])
            dummies_df = tmp_df.groupby(CUSTOMER_ID, as_index=False).sum()
            raw_merged_df = raw_merged_df.merge(dummies_df, on=CUSTOMER_ID, how=INNER)
        tmp_cols = raw_merged_df.columns.tolist()
        tmp_cols = [
            "_".join(i.split("_")[:-1]) + "_" + str(int(float(i.split("_")[-1])))
            if "." in i.split("_")[-1]
            else i
            for i in tmp_cols
        ]
        raw_merged_df.columns = tmp_cols
        return raw_merged_df

    @staticmethod
    @custom_exception()
    def update_user_node(node, properties: dict, graph):
        """
        Function to update user node in graph
        :param node: User Node object
        :param properties: properties to be updated
        :param graph: graph connection
        """
        try:
            graph.update_node_property(node, update_query=properties)
        except Exception as e:
            Logging.error(f"Error while updating user node on graph, Error: {e}")

    @staticmethod
    @custom_exception()
    def update_node_properties(user_profile: DataFrame):
        """
        Function to convert dataframe to dict
        and pass to node updater function
        : param user_profile: dataframe object pandas
        """
        user_profile = user_profile.drop(columns=[PAYTVPROVIDER_ID])
        print("Updating user node properties...")
        graph = ANGraphDb.new_connection_config().graph
        for index in user_profile.to_dict("records"):
            node = Node.parse_obj(
                {LABEL: USER_LABEL, PROPERTIES: {CUSTOMER_ID: str(index[CUSTOMER_ID])}}
            )
            index.pop(CUSTOMER_ID, None)
            index.pop(PAYTVPROVIDER_ID, None)
            NodeUpdater.update_user_node(node, index, graph)
        graph.connection.close()

    @staticmethod
    @custom_exception()
    def filter_preference_user(
        raw_merged_df: DataFrame,
    ):
        """
        Filter raw merged_df for users with no preferences
        are found in the graph
        :param raw_merged_df: Dataframe object pandas
        """
        raw_merged_df = raw_merged_df.set_index(CUSTOMER_ID)
        no_pref_users = raw_merged_df.loc[~(raw_merged_df != 0).any(axis=1)]
        no_pref_users = no_pref_users.reset_index().rename(
            columns={"index": CUSTOMER_ID}
        )
        raw_merged_df = raw_merged_df.loc[(raw_merged_df != 0).any(axis=1)]
        raw_merged_df = raw_merged_df.reset_index().rename(
            columns={"index": CUSTOMER_ID}
        )
        return raw_merged_df, no_pref_users

    @staticmethod
    @custom_exception()
    def vdb_updater(bucket_name=None, object_name=None, redis_uri=None):
        """
        Controller function for the class NodeUpdater
        :param bucket_name: s3 bucket name
        :param object_name: S3 key path
        :param redis_uri: redis uri
        """
        user_profile = NodeUpdater.process_s3_data(bucket_name)
        if user_profile.empty:
            Logging.error(f"""No user find to be updated. Aborting""")
            return
        paytv_df, user_profile = NodeUpdater.find_paytv_status(user_profile)
        if len(paytv_df) == 0:
            NodeUpdater.update_node_properties(user_profile)
            Logging.info(f"""No user found to update paytv status""")
            return
        UpdaterUtils.drop_existing_rel(
            data=user_profile, relation_label=HAS_PAYTV_PROVIDER
        )
        to_dump = paytv_df[paytv_df[STATUS] == ACTIVE_LOWER].reset_index(drop=True)
        UpdaterUtils.dump_relations(
            dump_data=to_dump,
            destination_property=PAYTVPROVIDER_ID,
            relation_label=HAS_PAYTV_PROVIDER,
            destination_label=PAYTV_PROVIDER,
            df_attribute=PAYTVPROVIDER_ID,
        )
        NodeUpdater.update_node_properties(user_profile)
        pref_list = NodeUpdater.get_preference(user_profile)
        tmp = []
        for i in pref_list:
            if i.empty:
                tmp.append(i)
        if len(tmp) == len(pref_list):
            paytv_df = user_profile.copy()
            NoPreferenceUsers.controller(
                no_pref_users=paytv_df,
                user_profile=user_profile,
                bucket_name=bucket_name,
                object_name=object_name,
                redis_uri=redis_uri,
            )
            return
        else:
            merged_df = NodeUpdater.prepare_merged_df(
                pref_list, paytv_df[[CUSTOMER_ID]]
            )
            raw_merged_df = NodeUpdater.get_dummy_features(merged_df)
            raw_merged_df, no_pref_users = NodeUpdater.filter_preference_user(
                raw_merged_df
            )
            if not raw_merged_df.empty:
                ClusterUpdater.controller(
                    data=raw_merged_df,
                    bucket_name=BUCKET_NAME,
                    object_name=object_name,
                    redis_uri=redis_uri,
                )
            if not no_pref_users.empty:
                NoPreferenceUsers.controller(
                    no_pref_users=no_pref_users,
                    user_profile=user_profile,
                    bucket_name=bucket_name,
                    object_name=object_name,
                    redis_uri=redis_uri,
                )
