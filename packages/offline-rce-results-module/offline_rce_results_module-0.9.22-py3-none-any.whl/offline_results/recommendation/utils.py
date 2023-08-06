import datetime
from functools import reduce
from math import inf

import pandas as pd
from cachetools import cached, TTLCache
from joblib import Parallel, delayed
from numpy import array, dot, sqrt
from pandas import DataFrame, concat, Series
from sklearn.preprocessing import MinMaxScaler


from offline_results.common.config import (
    MAX_NO_OF_CHUNKS,
    UBD_DATA_PATH,
    VISIONPLUS_DEV,
    CLUSTER_DATA_PATH,
    IMPLICIT_RATING_PATH,
    CONFIG_NOT_APPLICABLE_FOR_REC_PAYTV,
    CONFIG_NOT_APPLICABLE_FOR_REC_NO_PAYTV,
    S3_FILES_TTL,
    CONFIG_HOMEPAGE_PAYTV,
    CONFIG_HOMEPAGE_NO_PAYTV,
    LIVE_TV_CHANNEL_HOMEPAGE_PAYTV, LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV,
)
from offline_results.common.constants import (
    IS_PAY_TV,
    USER_LABEL,
    HOMEPAGE_ID,
    CONTENT_ID,
    STATUS,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    MINIBATCH_KMEANS,
    VIEWED,
    MAX_USERS,
    ITERATE_CLUSTER_RANGE,
    CLUSTER_ID,
    CUSTOMER_ID,
    CREATED_ON,
    HOMEPAGE,
    HOMEPAGE_STATUS,
    ACTIVE_LABEL,
    HAS_HOMEPAGE,
    ACTOR,
    ACTOR_ID,
    IS_CONNECTED,
    SCORE,
    SCORE_ROUNDOFF,
    PAY_TV,
    VIEW_COUNT,
    RANK_SCORE,
    ACTIVE
)

from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils.logger import Logging

cache_s3_file_ttl = TTLCache(maxsize=3, ttl=S3_FILES_TTL)

from offline_results.utils import class_custom_exception, custom_exception, Logging
from graphdb import GraphDb


class FilesFromS3:
    graph: GraphDb
    viewed_pkl = DataFrame()
    kmeans_pkl = DataFrame()
    rating_pkl = DataFrame()

    def __init__(self):
        FilesFromS3.graph = ANGraphDb.new_connection_config().graph

    @staticmethod
    @custom_exception()
    def download_and_update(filename):
        global s3files_obj
        ctl = ConnectS3()
        resource = ctl.create_connection()
        df = ctl.read_compress_pickles_from_S3(VISIONPLUS_DEV, filename, resource)
        if CUSTOMER_ID in df.columns:
            df[CUSTOMER_ID] = df[CUSTOMER_ID].apply(str)
        if df is not None and len(df) > 0:
            if filename == UBD_DATA_PATH:
                s3files_obj.viewed_pkl = df
            if filename == CLUSTER_DATA_PATH:
                s3files_obj.kmeans_pkl = df
            if filename == IMPLICIT_RATING_PATH:
                s3files_obj.rating_pkl = df
            cache_s3_file_ttl.__setitem__(filename, datetime.datetime.utcnow())

    @staticmethod
    @custom_exception()
    def update_files():
        try:
            FilesFromS3.download_and_update(UBD_DATA_PATH)
            FilesFromS3.download_and_update(CLUSTER_DATA_PATH)
            FilesFromS3.download_and_update(IMPLICIT_RATING_PATH)
            Logging.info("Successfully loaded the files from S3")

        except Exception as e:
            Logging.error(f"Error while loading files from s3. Error: {e}")


s3files_obj = FilesFromS3()


class RecommendationUtils:
    @staticmethod
    @custom_exception()
    def get_attribute_map(
        graph, node_label: str, key_node_property: str, value_node_property: str
    ) -> list:

        return graph.custom_query(
            query=f"""g.V().hasLabel('{node_label}').match(
            __.as("c").values('{key_node_property}').as('{key_node_property}'),
            __.as("c").values('{value_node_property}').as('{value_node_property}')
            ).select('{key_node_property}', '{value_node_property}')""",
            payload={
                node_label: node_label,
                key_node_property: key_node_property,
                value_node_property: value_node_property,
            },
        )

    @staticmethod
    @custom_exception()
    def get_homepage_for_contents(graph) -> list:

        response = []
        for label in [PAY_TV_CONTENT, NO_PAY_TV_CONTENT]:
            content_response = graph.custom_query(
                query=f"""g.V().hasLabel('{label}').match(
                __.as("c").values("content_id").as("content_id"),
                __.as("c").out("HAS_HOMEPAGE")
                .values("homepage_id").as("homepage_id")
                ).select("content_id", "homepage_id")""",
                payload={
                    label: label,
                },
            )

            # appending the flattened custom query response
            response.extend(
                [item for subresponse in content_response for item in subresponse]
            )

        return response

    @staticmethod
    @custom_exception()
    def get_homepage_id_title_map(graph, get_status: bool = False) -> list:

        if not get_status:
            # TO DO : Add payload (with latest version of graphdb-module, it throws an error without payload)
            homepage_response = graph.custom_query(
                query=f"""g.V().hasLabel('homepage').match(
                    __.as("c").values("homepage_id").as("homepage_id"),
                    __.as("c").values("homepage_title_en").as("homepage_title_en"),
                    ).select("homepage_id", "homepage_title_en")""",
            )
        else:
            # TO DO : Add payload (with latest version of graphdb-module, it throws an error without payload)
            homepage_response = graph.custom_query(
                query=f"""g.V().hasLabel('homepage').match(
                                __.as("c").values("homepage_id").as("homepage_id"),
                                __.as("c").values("homepage_title_en").as("homepage_title_en"),
                                __.as("c").values("homepage_status").as("homepage_status"),
                                __.as("c").values("is_connected").as("is_connected")
                                ).select("homepage_id", "homepage_title_en", "homepage_status", "is_connected")""",
            )

        return [item for subresponse in homepage_response for item in subresponse]

    @staticmethod
    @custom_exception()
    def get_node_property_label_values(graph, label: str, property: str) -> list:
        # TO DO : Add payload (with latest version of graphdb-module, it throws an error without payload)
        response = graph.custom_query(
            query=f"""g.V().hasLabel('{label}').match(
                __.as("c").values('{property}').as('{property}')
                ).select('{property}')""",
        )

        return [item for subresponse in response for item in subresponse]

    @staticmethod
    @custom_exception()
    def get_viewed_features(graph) -> DataFrame:
        """
        Query graphdb for user_viewed_content relation.
        """

        viewed_feature_list = []
        # TO DO : Add payload (with latest version of graphdb-module, it throws an error without payload)
        response = graph.custom_query(
            query=f"""g.V().hasLabel('{USER_LABEL}').outE('{VIEWED}').inV().path().by(elementMap())"""
        )

        for index, ele in enumerate(response):
            for i in range(len(response[index])):
                customer_id = response[index][i][0]["customer_id"]
                view_count = response[index][i][1]["view_count"]
                view_history = response[index][i][1]["view_history"]
                content_id = response[index][i][2]["content_id"]
                view_dict = {
                    "customer_id": customer_id,
                    "content_id": content_id,
                    "view_count": view_count,
                    "view_history": view_history,
                }
                viewed_feature_list.append(view_dict)

        return DataFrame(viewed_feature_list).reset_index(drop=True)

    @staticmethod
    @custom_exception()
    def multi_label_encoding(arr, unique_ids):
        encoded_list, count = [0] * len(unique_ids), 0
        for i in unique_ids:
            if i in arr:
                encoded_list[count] = 1
            count += 1
        return encoded_list

    @class_custom_exception()
    def find_with_has_label(self, label: list, edge_label: str, features: list):
        feature_str = ""
        for feature in features:
            feature_str += "__.as('c').values('" + feature + "').as('" + feature + "'),"
        query = f"""
                g.V().hasLabel('{"','".join(label)}').outE('{edge_label}').match(
                {feature_str[:-1]}).select('{"','".join(features)}')
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = DataFrame(data)
        return data

    @class_custom_exception()
    def find_with_has_conditon(
        self, label: str, condition_on, condition_value, edge_label, features: list
    ):

        feature_str = ""
        condition_value = (
            f"{condition_value}"
            if condition_value.__class__ == str
            else condition_value
        )
        for feature in features:
            feature_str += "__.as('c').values('" + feature + "').as('" + feature + "'),"
        query = f"""
                g.V().has('{label}','{condition_on}',{condition_value}).
                outE('{edge_label}').
                match({feature_str[:-1]}).select('{"','".join(features)}')
                """
        graph = ANGraphDb.new_connection_config().graph
        Logging.info(f"start fetching data from Graph Db for label {label}")
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = DataFrame(data)
        return data

    @staticmethod
    @custom_exception()
    def homepage_data(
        pay_tv_label=NO_PAY_TV_CONTENT, features=[CONTENT_ID, HOMEPAGE_ID]
    ):
        feature_str = ""
        for feature in features:
            feature_str += "values('" + feature + "'),"
        query = f"""
            g.V().hasLabel('{pay_tv_label}','{STATUS}','Active').
            outE('HAS_HOMEPAGE').
            project('HAS_HOMEPAGE', '{CONTENT_ID}', 'homepage_id').
            by(label).
            by(outV().values('{CONTENT_ID}')).
            by(inV().union(
            {feature_str[:-1]}).fold())
            """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data)
        return df

    @staticmethod
    @custom_exception()
    def get_content_data(pay_tv_label=NO_PAY_TV_CONTENT):

        query = f"""g.V()
                .has('{pay_tv_label}', '{STATUS}', '{ACTIVE_LABEL}')
                .outE('{HAS_HOMEPAGE}')
                .inV().hasLabel('{HOMEPAGE}')
                .path().by(valueMap('{CONTENT_ID}', '{HOMEPAGE_ID}', '{CREATED_ON}'))
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = [list(idx)[::-1] for idx in data]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        df[CONTENT_ID] = df[CONTENT_ID].apply(lambda x: x[0])
        df[HOMEPAGE_ID] = df[HOMEPAGE_ID].apply(lambda x: x[0])
        df[CREATED_ON] = df[CREATED_ON].apply(lambda x: x[0])
        return df

    @class_custom_exception()
    def find_all_cluster_id(self, pay_tv_label):
        query = f"""
                g.V().has('{MINIBATCH_KMEANS}','{IS_PAY_TV}', '{pay_tv_label}' ).valueMap("minibatch_kmeans", "status").by(unfold()).toList()
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data, columns=[MINIBATCH_KMEANS])
        df = df.sort_values([MINIBATCH_KMEANS], ignore_index=True)
        graph.connection.close()
        return df

    @class_custom_exception()
    def active_homepage_ids(self, is_paytv=None):
        pay_tv_query = (
            ""
            if is_paytv is None
            else f".has('{IS_CONNECTED}', '{'yes' if is_paytv is True else 'no'}')"
        )
        query = (
            f"""
                g.V().has('{HOMEPAGE}', '{HOMEPAGE_STATUS}', '{ACTIVE_LABEL}')"""
            + pay_tv_query
            + f"""
                .filter(__.in('{HAS_HOMEPAGE}')).valueMap("{HOMEPAGE_ID}").by(unfold()).toList()
                """
        )
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = DataFrame(data)[[HOMEPAGE_ID]]
        df = data.dropna(subset=[HOMEPAGE_ID])
        df[HOMEPAGE_ID] = df[HOMEPAGE_ID].apply(int)
        df = df.drop_duplicates(subset=[HOMEPAGE_ID])
        return df[HOMEPAGE_ID]

    @staticmethod
    @custom_exception()
    def single_cluster_users(
        cluster_id,
        cluster_paytv_label=True,
        user_paytv_label=True,
        user_limit=None,
    ):
        # data pipelining
        def data_generator(graph):

            loop_limit = int(MAX_USERS / ITERATE_CLUSTER_RANGE)
            start = 0
            end = ITERATE_CLUSTER_RANGE
            for rng in range(0, loop_limit):
                Logging.info(
                    f"For cluster id {cluster_id}, iterate users of range {start} - {end}"
                )
                query = f"""
                        g.V().has('minibatch_kmeans', 'minibatch_kmeans',{cluster_id})
                        .has('is_pay_tv', '{cluster_paytv_label}')
                        .inE("HAS_MINIBATCH_KMEANS_CLUSTER").range({start},{end})
                        .outV()
                        .has('is_pay_tv',{'true' if user_paytv_label is True else 'false'}).values("customer_id")
                        """
                try:
                    data = graph.custom_query(query, payload={})
                except Exception as e:
                    Logging.error(
                        f"Error while fetching data , retrying with new connection, Error : {e}"
                    )
                    graph.connection.close()
                    graph = ANGraphDb.new_connection_config().graph
                    data = graph.custom_query(query, payload={})
                start, end = end, end + ITERATE_CLUSTER_RANGE
                if len(data) == 0:
                    return [[]]
                yield data

        users_list = []
        graph = ANGraphDb.new_connection_config().graph
        for users in data_generator(graph):
            users_list = users_list + [rec for idx in users for rec in idx]
            if user_limit is not None and len(users_list) >= user_limit:
                return users_list[:user_limit]
        graph.connection.close()
        return users_list

    @staticmethod
    @custom_exception()
    def all_cluster_users(cluster_paytv_label=True, user_paytv_label=True):
        """
        function will return the df having all cluster and their user ids ,
        Note: default cluster id is not included
        """

        # data pipelining
        def df_generator(graph):
            count_query = f"g.V().has('minibatch_kmeans').has('is_pay_tv', '{cluster_paytv_label}').count()"
            cluster_count = graph.custom_query(count_query, payload={})
            for id in range(0, cluster_count[0][0] + 1):
                Logging.info(f"processing cluster_id: {id}")
                result = RecommendationUtils.single_cluster_users(
                    cluster_id=id,
                    user_paytv_label=user_paytv_label,
                    cluster_paytv_label=cluster_paytv_label,
                )
                yield id, result

        graph = ANGraphDb.new_connection_config().graph
        users_cluster = {CLUSTER_ID: [], CUSTOMER_ID: []}
        for cluster_id, users_list in df_generator(graph):
            users_cluster[CLUSTER_ID] += [cluster_id] * len(users_list)
            users_cluster[CUSTOMER_ID] += users_list
        data = DataFrame(users_cluster)
        graph.connection.close()
        return data

    @staticmethod
    @custom_exception()
    def single_user_cluster(customer_id, is_pay_tv=True):
        query = f"""g.V().
                has('user', 'customer_id', '{customer_id}').
                has("is_pay_tv", {'true' if is_pay_tv is True else 'false'}).
                outE("HAS_MINIBATCH_KMEANS_CLUSTER").
                inV().hasLabel("minibatch_kmeans").
                limit(1).
                values("minibatch_kmeans")"""
        graph = ANGraphDb.new_connection_config().graph
        cluster_id = graph.custom_query(query, payload={})
        cluster_id = cluster_id[0][0] if len(cluster_id) > 0 else None
        graph.connection.close()
        return cluster_id

    @staticmethod
    @custom_exception()
    def homepage_specific_content(
        homepage_id,
        paytv_label=PAY_TV_CONTENT,
        content_active_status="Active",
    ):
        query = f"""
                g.V()
                .has("homepage","homepage_id",{homepage_id})
                .inE("HAS_HOMEPAGE")
                .outV()
                .has("{paytv_label}", "status", "{content_active_status}")
                .values("content_id")
                """
        graph = ANGraphDb.new_connection_config().graph
        content_ids = graph.custom_query(query, payload={})
        content_ids = (
            [rec for idx in content_ids for rec in idx] if len(content_ids) > 0 else []
        )
        graph.connection.close()
        return content_ids

    @staticmethod
    @custom_exception()
    def all_user_preferences(
        pref_node="category",
        pref_edge_label="HAS_CATEGORY_PREFERENCES",
        user_paytv_label=True,
        pref_limit=MAX_USERS,
        from_idx=0,
        features=[],
    ):
        # data pipelining
        feature_str = ""
        for feature in features:
            feature_str += "'" + feature + "',"

        def data_generator(graph):
            loop_limit = int(pref_limit / ITERATE_CLUSTER_RANGE) + 1
            start = 0 + from_idx
            end = min(start + pref_limit, start + ITERATE_CLUSTER_RANGE)
            for rng in range(0, loop_limit):
                Logging.info(f" iterate {pref_node} pref of range {start} - {end}")
                query = f"""
                        g.V()
                        .hasLabel('{pref_node}')
                        .inE('{pref_edge_label}')
                        .outV()
                        .has('user','is_pay_tv', {'true' if user_paytv_label is True else 'false'})
                        .range({start}, {end})
                        .path()
                        .by(valueMap({feature_str[:-1]}))
                        """
                try:
                    data = graph.custom_query(query, payload={})
                except Exception as e:
                    Logging.error(
                        f"Error while fetching data , retrying with new connection, Error : {e}"
                    )
                    graph.connection.close()
                    graph = ANGraphDb.new_connection_config().graph
                    data = graph.custom_query(query, payload={})

                start, end = end, end + ITERATE_CLUSTER_RANGE
                if len(data) == 0:
                    graph.connection.close()
                    return [[]]
                yield data

        data = []
        graph = ANGraphDb.new_connection_config().graph
        for user_pref in data_generator(graph):
            data = data + [rec for idx in user_pref for rec in idx]
            if pref_limit is not None and len(data) >= pref_limit:
                data = data[:pref_limit]
                break
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        graph.connection.close()
        return df

    @staticmethod
    @custom_exception()
    def user_pref(
        pref_node,
        pref_edge_label,
        user_paytv_label=True,
        features=[],
        pref_limit=MAX_USERS,
    ):
        Logging.info(f"start fetching users {pref_node} preference")
        query = f"""
                g.V()
                .hasLabel('{pref_node}')
                .inE('{pref_edge_label}')
                .outV()
                .has('user','is_pay_tv', {'true' if user_paytv_label is True else 'false'})
                .count()
                """

        graph = ANGraphDb.new_connection_config().graph
        count = graph.custom_query(query, payload={})[0][0]
        graph.connection.close()
        parll_count = min(count, inf if pref_limit is None else pref_limit)
        t = parll_count // MAX_NO_OF_CHUNKS + 1
        l = [
            (pref_node, pref_edge_label, user_paytv_label, t, i * t, features)
            for i in range(MAX_NO_OF_CHUNKS)
        ]
        results = Parallel(n_jobs=5)(
            delayed(RecommendationUtils.all_user_preferences)(i, j, k, n, m, f)
            for i, j, k, n, m, f in l
        )
        results = concat(results, axis=0, ignore_index=True)
        return results

    @staticmethod
    @custom_exception()
    def content_having_homepage(is_paytv=False):
        query = f"""
                g.V()
                .hasLabel('{PAY_TV_CONTENT if is_paytv else NO_PAY_TV_CONTENT}')
                .outE('HAS_HOMEPAGE')
                .inV()
                .has('homepage', 'is_connected', '{'yes' if is_paytv else 'no'}')
                .path().by(valueMap('content_id','homepage_id' ))
                """
        try:
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={})
        except Exception as e:
            Logging.error(
                f"Error while fetching data , retrying with new connection, Error : {e}"
            )
            graph.connection.close()
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={})
        data = [rec for idx in data for rec in idx]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        graph.connection.close()
        return df

    @staticmethod
    @custom_exception()
    def single_user_pref(customer_id, pref_node, pref_edge, feature):
        query = f"""
                g.V().has('{USER_LABEL}', '{CUSTOMER_ID}', '{customer_id}')
                .outE().hasLabel('{pref_edge}')
                .inV().hasLabel('{pref_node}')
                .values('{feature}')
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        return data

    @staticmethod
    @custom_exception()
    def content_property(
        is_paytv=True, pref_edge_label=None, node_label=None, pref_feature=None
    ):

        query = f"""
                g.V().hasLabel('{PAY_TV_CONTENT if is_paytv else NO_PAY_TV_CONTENT}').
                outE('{pref_edge_label}').inV().hasLabel('{node_label}').
                path().by(valueMap('{CONTENT_ID}','{pref_feature}'))
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        data = [rec for idx in data for rec in idx]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        graph.connection.close()
        return df

    @staticmethod
    @custom_exception()
    def calculate_euclidean_dist(data_point_1, data_point_2):
        try:
            features = list(set(data_point_1.index).intersection(set(data_point_2.index)))
            data_point_1, data_point_2 = array(data_point_1[features]), array(data_point_2[features])
            differences = data_point_1 - data_point_2
            squared_sums = dot(differences.T, differences)
            distance = sqrt(squared_sums)
            return abs(distance)
        except Exception as e:
            Logging.error(f"Error while calculating euclidean dist. Error: {e}")

    @staticmethod
    @custom_exception()
    def encode_df(df, col, one_hot_encoder):
        ctl = RecommendationUtils()
        df[col] = df[col].apply(lambda x: ctl.multi_label_encoding(x, one_hot_encoder))
        return df

    @staticmethod
    @custom_exception()
    def expand_features(df, col):
        expand_features = df[col].apply(Series)
        expand_features.columns = [col + "_" + str(i) for i in expand_features.columns]
        df = df.drop(columns=[col])
        df = concat([df, expand_features], axis=1)
        return df

    @staticmethod
    @custom_exception()
    def all_actor_ids():

        query = f"""
                g.V().hasLabel('{ACTOR}').values('{ACTOR_ID}')
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        data = [rec for idx in data for rec in idx]
        graph.connection.close()
        return data

    @staticmethod
    @custom_exception()
    def user_cluster_from_s3():
        if len(s3files_obj.kmeans_pkl) != 0 and cache_s3_file_ttl.get(
            CLUSTER_DATA_PATH
        ):
            return s3files_obj.kmeans_pkl.copy()
        Logging.info("Start fetching 'K-MEANS_JOIN' data from s3...")
        FilesFromS3.download_and_update(CLUSTER_DATA_PATH)
        return s3files_obj.kmeans_pkl.copy()

    @staticmethod
    @custom_exception()
    def user_viewed_data_from_s3():
        if len(s3files_obj.viewed_pkl) != 0 and cache_s3_file_ttl.get(UBD_DATA_PATH):
            return s3files_obj.viewed_pkl.copy()
        Logging.info("Start fetching 'VIEWED_JOIN' file from s3...")
        FilesFromS3.download_and_update(UBD_DATA_PATH)
        return s3files_obj.viewed_pkl.copy()

    @staticmethod
    @custom_exception()
    def implicit_rating_data_from_s3():
        if len(s3files_obj.rating_pkl) != 0 and cache_s3_file_ttl.get(
            IMPLICIT_RATING_PATH
        ):
            return s3files_obj.rating_pkl.copy()
        Logging.info("Start fetching 'IMPLICIT_RATING_JOIN' file from s3...")
        FilesFromS3.download_and_update(IMPLICIT_RATING_PATH)
        return s3files_obj.rating_pkl.copy()

    @staticmethod
    @custom_exception()
    def content_data(pay_tv_label=NO_PAY_TV_CONTENT, features=[CONTENT_ID, CREATED_ON]):
        feature_str = ""
        for feature in features:
            feature_str += "'" + feature + "',"
        query = f"""g.V().hasLabel('{pay_tv_label}', '{STATUS}', '{ACTIVE_LABEL}').valueMap({feature_str[:-1]})"""
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        data = [rec for idx in data for rec in idx]
        graph.connection.close()
        data = DataFrame(data)
        for col in data.columns:
            data[col] = data[col].apply(lambda x: x[0])
        return data

    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=60 * 10))
    @custom_exception()
    def active_content_and_homepage_ids(
        pay_tv_label=NO_PAY_TV_CONTENT,
    ):
        Logging.info("Start fetching 'CONTENT' and their 'HOMEPAGE'...")
        query = f"""
                g.V()
                .has('{pay_tv_label}', '{STATUS}', '{ACTIVE_LABEL}')
                .outE('{HAS_HOMEPAGE}')
                .inV()
                .has('{HOMEPAGE}', '{HOMEPAGE_STATUS}', '{ACTIVE_LABEL}')
                .path()
                .by(valueMap('{CONTENT_ID}', '{HOMEPAGE_ID}'))
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        return df

    @staticmethod
    @custom_exception()
    def reserved_homepage_id(is_pay_tv=True):
        if is_pay_tv:
            pay_tv_na_hid = list(CONFIG_NOT_APPLICABLE_FOR_REC_PAYTV.keys())
            pay_tv_special = list(CONFIG_HOMEPAGE_PAYTV.keys())
            return set(pay_tv_na_hid + pay_tv_special)
        no_pay_tv_na_hid = list(CONFIG_NOT_APPLICABLE_FOR_REC_NO_PAYTV.keys())
        no_pay_tv_special = list(CONFIG_HOMEPAGE_NO_PAYTV.keys())
        return set(no_pay_tv_na_hid + no_pay_tv_special)

    @staticmethod
    @custom_exception()
    def get_tv_channels(
            is_pay_tv=True
    ) -> list:
        channel = LIVE_TV_CHANNEL_HOMEPAGE_PAYTV if is_pay_tv else LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV
        query = f""" g.V().has('{CONTENT_ID}').match(
                    __.as("c").valueMap('{CONTENT_ID}').as('{CONTENT_ID}'),
                    __.as("c").out('{HAS_HOMEPAGE}').has('{HOMEPAGE_ID}',within({channel}))
                    ).select('{CONTENT_ID}')
                    """
        graph = ANGraphDb.new_connection_config().graph
        Logging.info(f"Fetching Live TV Channel Data for id: {channel}")
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = DataFrame(data)[CONTENT_ID].apply(lambda x: x[0]).to_list()
        return data


    @staticmethod
    @custom_exception()
    def round_score(df):
        if SCORE in df.columns:
            num_round_off = {
                1: 0.1,
                2: 0.01,
                3: 0.001,
                4: 0.0001,
                5: 0.00001,
                6: 0.000001,
                7: 0.0000001,
                8: 0.00000001,
            }
            if df[SCORE].min() <= num_round_off.get(SCORE_ROUNDOFF, 0):
                scaler = MinMaxScaler(
                    feature_range=(num_round_off.get(SCORE_ROUNDOFF, 0), 1)
                )
                df[SCORE] = (
                    scaler.fit_transform(df[[SCORE]].to_numpy()).flatten().tolist()
                )
            elif df[SCORE].min() > 1:
                scaler = MinMaxScaler(
                    feature_range=(num_round_off.get(SCORE_ROUNDOFF, 0), 1))
                df[SCORE] = (scaler.fit_transform(df[[SCORE]].to_numpy()).flatten().tolist())
            df = df.sort_values([SCORE], ascending=False, ignore_index=True)
            df[SCORE] = df[SCORE].round(decimals=SCORE_ROUNDOFF)
        return df

    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=60 * 10))
    @custom_exception()
    def active_content_and_homepage_ids_with_ubd(
        pay_tv_label=NO_PAY_TV_CONTENT,
    ):
        Logging.info("Start fetching 'CONTENT' and their 'HOMEPAGE'...")
        query = f"""
                    g.V()
                    .has('{pay_tv_label}', '{STATUS}', '{ACTIVE_LABEL}')
                    .filter(__.in('{VIEWED}'))
                    .outE('{HAS_HOMEPAGE}')
                    .inV()
                    .has('{HOMEPAGE}', '{HOMEPAGE_STATUS}', '{ACTIVE_LABEL}')
                    .path()
                    .by(valueMap('{CONTENT_ID}', '{HOMEPAGE_ID}'))
                    """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        return df

    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=60 * 10))
    @custom_exception()
    def get_label_wise_homepage_for_contents(
        graph, user_label, homepage_id_wise
    ) -> DataFrame:
        Logging.info("Start fetching content-homepage mapping from network...")
        content_label = PAY_TV_CONTENT if user_label == PAY_TV else NO_PAY_TV_CONTENT
        is_connected = "yes" if user_label == PAY_TV else "no"
        if homepage_id_wise:
            query = f"""g.V().has('{content_label}', '{STATUS}', '{ACTIVE_LABEL}')
                        .outE('{HAS_HOMEPAGE}').inV()
                        .has('{HOMEPAGE}', '{HOMEPAGE_STATUS}', '{ACTIVE_LABEL}')
                        .has('{IS_CONNECTED}','{is_connected}').path()
                        .by(valueMap('{CONTENT_ID}', '{HOMEPAGE_ID}'))"""
        else:
            query = f"""g.V().has('{content_label}', '{STATUS}', '{ACTIVE_LABEL}')
                        .outE('{HAS_HOMEPAGE}').inV()
                        .has('{HOMEPAGE}','{IS_CONNECTED}','{is_connected}').path()
                        .by(valueMap('{CONTENT_ID}', '{HOMEPAGE_ID}'))"""
        try:
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={})
        except Exception as e:
            Logging.error(
                f"Error while fetching content-homepage mapping from network, retrying with new connection, "
                f"Error : {e}"
            )
            graph.connection.close()
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        return df

    @staticmethod
    @cached(cache=TTLCache(maxsize=1024, ttl=60 * 10))
    @custom_exception()
    def get_active_homepage_ids_having_active_content(graph, user_label) -> DataFrame:
        Logging.info("Start fetching active homepage_ids from network...")
        content_label = PAY_TV_CONTENT if user_label == PAY_TV else NO_PAY_TV_CONTENT
        is_connected = "yes" if user_label == PAY_TV else "no"
        query = f"""
                g.V().has('{HOMEPAGE}','{IS_CONNECTED}','{is_connected}').has('{HOMEPAGE_STATUS}','{ACTIVE_LABEL}').
                filter(__.inE('{HAS_HOMEPAGE}').outV().has('{content_label}','{STATUS}','{ACTIVE_LABEL}'))
                .path().by(valueMap('{HOMEPAGE_ID}', '{CREATED_ON}'))
                """
        try:
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        except Exception as e:
            Logging.error(
                f"Error while fetching active homepage_ids from network, retrying with new connection, "
                f"Error : {e}"
            )
            graph.connection.close()
            graph = ANGraphDb.new_connection_config().graph
            data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = [list(idx)[::-1] for idx in data]
        data = [
            reduce(lambda x, y: dict(list(x.items()) + list(y.items())), list(item))
            for item in data
        ]
        df = DataFrame(data)
        df[HOMEPAGE_ID] = df[HOMEPAGE_ID].apply(lambda x: x[0])
        df[CREATED_ON] = df[CREATED_ON].apply(lambda x: x[0])
        if HOMEPAGE_ID in df.columns:
            df[HOMEPAGE_ID] = df[HOMEPAGE_ID].apply(int)
            df = df.drop_duplicates(subset=[HOMEPAGE_ID])
        return df

    @staticmethod
    @custom_exception()
    def active_contents(is_paytv=True):
        pay_tv_label = PAY_TV_CONTENT if is_paytv is True else NO_PAY_TV_CONTENT
        query = f"""
                g.V()
                .has('{pay_tv_label}', '{STATUS}', '{ACTIVE_LABEL}')
                .valueMap('{CONTENT_ID}','{CREATED_ON}')
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x[0])
        df = df.drop_duplicates()
        return df

    @custom_exception()
    def get_recommendation_scores(self, df):
        if len(df) > 0:
            df[RANK_SCORE] = [score for score in range(1, len(df) + 1)][::-1]
            df[SCORE] = df[VIEW_COUNT] + df[RANK_SCORE] if VIEW_COUNT in df.columns else df[RANK_SCORE]
            df[[SCORE]] = MinMaxScaler(
                feature_range=(0.1, 1)
            ).fit_transform(df[[SCORE]])
            df = self.round_score(df)
        return df

    @staticmethod
    @custom_exception()
    def get_content_homepage_id_mapping(graph, user_label, homepage_id_wise):
        content_label = PAY_TV_CONTENT if user_label == PAY_TV else NO_PAY_TV_CONTENT
        queries = graph.custom_query(
            f"""g.V().hasLabel('{content_label}').match(
                        __.as("c").valueMap("{CONTENT_ID}","{STATUS}","{CREATED_ON}").as("{CONTENT_ID}"),
                        __.as("c").out("{HAS_HOMEPAGE}")
                        .valueMap("{HOMEPAGE_ID}","{HOMEPAGE_STATUS}").as("{HOMEPAGE_ID}")
                        ).select("{CONTENT_ID}", "{HOMEPAGE_ID}")""",
            payload={
                content_label: content_label,
                CONTENT_ID: CONTENT_ID,
                HAS_HOMEPAGE: HAS_HOMEPAGE,
                HOMEPAGE_ID: HOMEPAGE_ID,
                HOMEPAGE_STATUS: HOMEPAGE_STATUS,
                STATUS: STATUS,
                CREATED_ON: CREATED_ON,
            },
        )
        content_homepage_map_df = pd.DataFrame()
        for query in queries:
            for data in query:
                content_id = data[CONTENT_ID][CONTENT_ID][0]
                content_status = data[CONTENT_ID][STATUS][0]
                created_on = data[CONTENT_ID][CREATED_ON][0]
                homepage_id = data[HOMEPAGE_ID][HOMEPAGE_ID][0]
                homepage_status = data[HOMEPAGE_ID][HOMEPAGE_STATUS][0]
                content_homepage_map = pd.DataFrame(
                    [
                        {
                            CONTENT_ID: content_id,
                            STATUS: content_status,
                            CREATED_ON: created_on,
                            HOMEPAGE_ID: homepage_id,
                            HOMEPAGE_STATUS: homepage_status,
                        }
                    ]
                )
                content_homepage_map_df = (
                    pd.concat([content_homepage_map_df, content_homepage_map], axis=0)
                    .sort_values(by=CONTENT_ID)
                    .reset_index(drop=True)
                )
        if homepage_id_wise:
            content_homepage_map_df = content_homepage_map_df[
                (content_homepage_map_df[HOMEPAGE_STATUS] == ACTIVE)
                & (content_homepage_map_df[STATUS] == ACTIVE)
            ].reset_index(drop=True)
        else:
            content_homepage_map_df = content_homepage_map_df[
                content_homepage_map_df[STATUS] == ACTIVE
            ].reset_index(drop=True)
        content_homepage_map_df_grouped = pd.DataFrame(
            content_homepage_map_df.groupby(CONTENT_ID)[HOMEPAGE_ID]
            .apply(list)
            .reset_index()
        )
        return content_homepage_map_df_grouped, content_homepage_map_df
