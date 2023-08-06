from typing import List, Dict, Any

from graphdb import GraphDb
from graphdb.connection import GraphDbConnection

from offline_results.api import HomepageRecommendation, HomepageClusterCategory, Ranking
from offline_results.repository import RedisConnection
from offline_results.utils import class_custom_exception


class OfflineResults:
    """This class will be as entry point"""

    def __init__(self, graph_connection: GraphDbConnection, redis_uri: str):
        """Assumption service that include this module already create connection
        then passing that connection here, no need create new connection
        :param graph_connection: object graphdb connection
        :param redis_uri: connection uri redis
        """
        self.redis = RedisConnection.from_uri(redis_uri)
        self.graph = GraphDb.from_connection(graph_connection)

    @class_custom_exception()
    def homepage_recommendation(
        self,
    ) -> List[Dict[str, List[Dict[str, Any]]]]:
        """Calculate data for homepage recommendation
        :return: none
        """
        homepage_recommendation = HomepageRecommendation(self.graph, self.redis)
        return homepage_recommendation.recommendation()

    @class_custom_exception()
    def homepage_cluster_category(
        self,
    ) -> List[Dict[str, List[Dict[str, Any]]]]:
        """Calculate data for homepage cluster category
        :return: list of dictionary
        """
        homepage_cluster_category = HomepageClusterCategory(self.graph, self.redis)
        return homepage_cluster_category.recommendation()

    @class_custom_exception()
    def ranking(
        self,
    ) -> List[Dict[str, List[Dict[str, Any]]]]:
        """Calculate data for ranking
        :return: none
        """
        ranking = Ranking(self.graph, self.redis)
        return ranking.recommendation()
