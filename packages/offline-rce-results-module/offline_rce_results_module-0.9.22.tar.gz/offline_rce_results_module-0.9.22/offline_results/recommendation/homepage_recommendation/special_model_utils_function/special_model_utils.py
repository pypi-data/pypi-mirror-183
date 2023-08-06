import pandas as pd
from offline_results.common.config import LIVE_TV_CHANNEL_HOMEPAGE_PAYTV, LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV
from offline_results.common.constants import CONTENT_ID, HAS_HOMEPAGE, HOMEPAGE_ID, PAY_TV_CONTENT, PAY_TV, \
    NO_PAY_TV_CONTENT, STATUS, CREATED_ON, HOMEPAGE_STATUS, ACTIVE
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging
from pandas import DataFrame


class SpecialModelUtils:

    @staticmethod
    @custom_exception()
    def get_tv_channels(
            is_pay_tv=True
    ) -> list:
        channel = LIVE_TV_CHANNEL_HOMEPAGE_PAYTV if is_pay_tv else LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV
        Logging.info(f"Fetching Live TV Channel Data for id: {channel}")
        query = f""" g.V().has('{CONTENT_ID}').match(
                    __.as("c").valueMap('{CONTENT_ID}').as('{CONTENT_ID}'),
                    __.as("c").out('{HAS_HOMEPAGE}').has('{HOMEPAGE_ID}',within({channel}))
                    ).select('{CONTENT_ID}')
                    """
        graph = ANGraphDb.new_connection_config().graph
        data = graph.custom_query(query, payload={})
        graph.connection.close()
        data = [rec for idx in data for rec in idx]
        data = DataFrame(data)[CONTENT_ID].apply(lambda x: x[0]).to_list()
        return data

    @staticmethod
    @custom_exception()
    def get_content_homepage_id_mapping(user_label, homepage_id_wise):
        content_label = PAY_TV_CONTENT if user_label == PAY_TV else NO_PAY_TV_CONTENT
        Logging.info("Fetch content-homepage_id mapping")
        graph = ANGraphDb.new_connection_config().graph
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
        graph.connection.close()
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

        return content_homepage_map_df
