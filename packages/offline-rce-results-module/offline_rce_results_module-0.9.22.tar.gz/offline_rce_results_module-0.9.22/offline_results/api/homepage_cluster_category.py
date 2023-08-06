import random
from typing import List, Dict, Any

from graphdb import GraphDb
from graphdb.connection import GraphDbConnection

from offline_results.interface import RecommendationInterface
from offline_results.repository import RedisConnection
from offline_results.utils import custom_exception, class_custom_exception


class HomepageClusterCategory(RecommendationInterface):
    def __init__(self, graph_connection: GraphDb, redis_connection: RedisConnection):
        """Assumption service that include this module already create connection
        then passing that connection here, no need create new connection
        :param graph_connection: object graphdb connection
        :param redis_connection: connection uri redis
        """
        self.redis = redis_connection
        self.graph = graph_connection

    @classmethod
    def from_payload(
        cls,
        graph_connection: GraphDbConnection,
        redis_uri: str,
    ) -> "HomepageClusterCategory":
        """Create object from payload
        :param graph_connection: object connection
        :param redis_uri: string redis uri
        :return: current object
        """
        return cls(
            GraphDb.from_connection(graph_connection),
            RedisConnection.from_uri(redis_uri),
        )

    @staticmethod
    @custom_exception()
    def fetch_byw_recommendation() -> List[Dict[str, Any]]:
        """fetch because you watch recommendation type
        :return: list of dictionary
        """
        byw = []
        for i in range(1, 100):
            byw.append(
                {
                    "id": random.randint(1, 1_000),
                    "recommendation": "byw_offline_cluster_category_{}".format(
                        random.randint(1, 1_000)
                    ),
                }
            )
        return byw

    @staticmethod
    @custom_exception()
    def fetch_user_behaviour_recommendation() -> List[Dict[str, Any]]:
        """fetch because you watch recommendation type
        :return: list of dictionary
        """
        ub = []
        for i in range(1, 100):
            ub.append(
                {
                    "id": random.randint(1, 1_000),
                    "recommendation": "ub_offline_cluster_category_{}".format(
                        random.randint(1, 1_000)
                    ),
                }
            )
        return ub

    @class_custom_exception()
    def recommendation(
        self,
    ) -> List[Dict[str, List[Dict[str, Any]]]]:
        """Fetch recommendation based on total records
        :return: list of dictionary
        """
        resp = [
            {"byw": self.fetch_byw_recommendation()},
            {"user_behaviour": self.fetch_user_behaviour_recommendation()},
        ]
        return resp
