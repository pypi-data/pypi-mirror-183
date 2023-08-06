from traceback import print_exc

from pandas import DataFrame

from offline_results.common.constants import (
    CONTENT_CORE_SYNOPSIS,
    HOMEPAGE,
    PAY_TV_CONTENT,
    IS_CONNECTED,
    HOMEPAGE_STATUS,
    ACTIVE_LABEL,
    HOMEPAGE_ID,
    CONTENT_ID,
    TAGS_DESCRIPTION,
    STATUS,
    CONTENT_CORE_ID,
)
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception


class QueryUtils:
    @staticmethod
    @custom_exception()
    def active_homepage_ids(content_label):
        pay_tv_query = (
            ""
            f".has('{IS_CONNECTED}', '{'yes' if content_label == PAY_TV_CONTENT else 'no'}')"
        )
        query = (
            f"""
                g.V().has('{HOMEPAGE}', '{HOMEPAGE_STATUS}', '{ACTIVE_LABEL}')"""
            + pay_tv_query
            + f"""
                .valueMap("{HOMEPAGE_ID}").by(unfold()).toList()
                """
        )
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={HOMEPAGE_ID: HOMEPAGE_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data)[HOMEPAGE_ID]
        return df

    @staticmethod
    @custom_exception()
    def tag_data(content_label, features=[CONTENT_ID, TAGS_DESCRIPTION]):
        feature_str = ""
        for feature in features:
            feature_str += "values('" + feature + "'),"
        query = f"""
                g.V().hasLabel('{content_label}','{STATUS}','Active').
                outE('HAS_TAG').
                project('HAS_TAG', '{CONTENT_ID}', 'tags_description').
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
        df = df[[CONTENT_ID, TAGS_DESCRIPTION]].explode(
            column=[TAGS_DESCRIPTION], ignore_index=True
        )
        return df[[CONTENT_ID, TAGS_DESCRIPTION]]

    @staticmethod
    @custom_exception()
    def get_content_id_title_and_synopsis(content_label) -> DataFrame:
        graph = ANGraphDb.new_connection_config().graph
        response = graph.custom_query(
            query=f"""g.V().hasLabel('{content_label}').has('{STATUS}','Active').match(
                                __.as("c").values("content_id").as("content_id"),
                                __.as("c").values("title").as("title"),
                                __.as("c").values("synopsis").as("synopsis")
                                ).select("content_id", "title", "synopsis")""",
            payload={content_label: content_label, STATUS: STATUS},
        )
        graph.connection.close()
        return DataFrame([item for subresponse in response for item in subresponse])

    @staticmethod
    @custom_exception()
    def get_all_synopsys() -> DataFrame:
        graph = ANGraphDb.new_connection_config().graph
        response = graph.custom_query(
            query=f"""g.V().hasLabel('{CONTENT_CORE_SYNOPSIS}').match(
                                __.as("c").values("content_core_id").as("content_core_id"),
                                __.as("c").values("content_core_synopsis").as("content_core_synopsis")
                                ).select("content_core_id", "content_core_synopsis")""",
            payload={CONTENT_CORE_SYNOPSIS: CONTENT_CORE_SYNOPSIS},
        )
        graph.connection.close()
        return DataFrame([item for subresponse in response for item in subresponse])

    @staticmethod
    @custom_exception()
    def content_core_data(content_label, features=[CONTENT_ID, CONTENT_CORE_ID]):
        feature_str = ""
        for feature in features:
            feature_str += "values('" + feature + "'),"
        query = f"""
                g.V().hasLabel('{content_label}','{STATUS}','Active').
                outE('HAS_CONTENT_CORE').
                project('HAS_CONTENT_CORE', '{CONTENT_ID}', 'content_core_id').
                by(label).
                by(outV().values('{CONTENT_ID}')).
                by(inV().union(
                {feature_str[:-1]}).fold())
                """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={CONTENT_ID: CONTENT_ID})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        df = DataFrame(data)
        df = df[[CONTENT_ID, CONTENT_CORE_ID]].explode(column=[CONTENT_CORE_ID])
        return df[~(df[CONTENT_ID] == df[CONTENT_CORE_ID])]

    @staticmethod
    @custom_exception()
    def query_homepage_for_all_contents(content_label):
        try:
            graph = ANGraphDb.new_connection_config().graph
            response = graph.custom_query(
                query=f"""g.with('Neptune#enableResultCache', true).V().hasLabel('{content_label}')
                              .match(
                            __. as ("c").valueMap("content_id", "status"). as ("content_id"),
                            __. as ("c").out("HAS_HOMEPAGE").valueMap("homepage_id", "homepage_status", "is_connected").as("homepage_id")
                            ).select("content_id","homepage_id")""",
                payload={content_label: content_label},
            )
            graph.connection.close()
        except Exception:
            print_exc()
            graph = ANGraphDb.new_connection_config().graph
            response = graph.custom_query(
                query=f"""g.with('Neptune#enableResultCache', true).V().hasLabel('{content_label}')
                              .match(
                            __. as ("c").valueMap("content_id", "status"). as ("content_id"),
                            __. as ("c").out("HAS_HOMEPAGE").valueMap("homepage_id", "homepage_status", "is_connected").as("homepage_id")
                            ).select("content_id","homepage_id")""",
                payload={content_label: content_label},
            )
            graph.connection.close()

        return response

    @staticmethod
    @custom_exception()
    def homepage_data(pay_tv_label, features=[CONTENT_ID, HOMEPAGE_ID]):
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
