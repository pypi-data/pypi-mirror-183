from pandas import DataFrame, concat

from offline_results.common.constants import (
    CUSTOMER_ID,
    S3,
    GRAPH_DB,
    USER_LABEL,
    CONTENT_ID,
    RATING,
    IMPLICIT_RATING,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import class_custom_exception, Logging


class DataGathering:
    def __init__(self, data_source=S3):

        self.raw_data = DataFrame()
        self.dataset = DataFrame()
        self.graph = ANGraphDb.new_connection_config().graph
        self.raw_data = DataFrame()
        self.data_source = data_source
        self.dataset = DataFrame()

    @class_custom_exception()
    def get_from_s3(
        self,
    ):
        try:
            result = RecommendationUtils().implicit_rating_data_from_s3()
            result.rename(columns={IMPLICIT_RATING: RATING}, inplace=True)
            result[CUSTOMER_ID] = result[CUSTOMER_ID].apply(str)
            result[CONTENT_ID] = result[CONTENT_ID].apply(str)
            self.raw_data = result[[CUSTOMER_ID, CONTENT_ID, RATING]]

        except Exception as e:
            Logging.error(f"Error while getting data from s3. Error :{e}")

    @class_custom_exception()
    def get_from_db(self):
        try:
            Logging.info("start fetching data from db")
            data = self.graph.custom_query(
                f""" g.V().hasLabel('{USER_LABEL}').outE().hasLabel('HAS_RATING').inV().path().by(elementMap())""",
                payload={USER_LABEL: USER_LABEL},
            )
            Logging.info(f"fetching data from db of len {len(data)}")
            for view in data:
                for history in view:
                    user_data, content_data, rating_data = (
                        history[0][CUSTOMER_ID],
                        history[2][CONTENT_ID],
                        history[1][IMPLICIT_RATING],
                    )
                    user_content_data = DataFrame(
                        [
                            {
                                CUSTOMER_ID: user_data,
                                CONTENT_ID: content_data,
                                RATING: rating_data,
                            }
                        ]
                    )
                    self.raw_data = concat([self.raw_data, user_content_data], axis=0)
                    self.raw_data = self.raw_data.reset_index(drop=True)
        except Exception as e:
            Logging.error(f"Error while getting data from graph db. Error :{e}")

    @class_custom_exception()
    def data_gathering(
        self,
    ):
        if self.data_source == S3:
            self.get_from_s3()

        if self.data_source == GRAPH_DB:
            self.get_from_db()

        return self.raw_data


# test code here
# if __name__ == "__main__":
#     ctl = DataGathering(data_source="s3")
#     df=ctl.data_gathering()
