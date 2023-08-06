import time
from datetime import datetime
from typing import Dict, Any

from graphdb import GraphDb
from numpy import subtract, int64
from pandas import DataFrame, merge

from offline_results.common.config import (
    CONFIG_HOMEPAGE_PAYTV,
    CONFIG_HOMEPAGE_NO_PAYTV,
)
from offline_results.common.constants import (
    HOMEPAGE_ID,
    MODEL_NAME,
    CONTENT_ID,
    VIEW_COUNT,
    SUM,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    SCORE,
    PAY_TV,
    RECOMMENDED_CONTENT_ID,
    CREATED_ON,
    RECORDS,
    SERVICE_NAME,
    ITEM_TO_ITEM_DEFAULT_MODULE_NAME,
    ACTIVE,
    HOMEPAGE_ID_BASED,
    HOMEPAGE_CONTENT_DF,
    USER_LOG,
    ACTIVE_HOMEPAGE_ID_LIST,
    CONTENT_STATUS,
    IS_PAY_TV,
    SIMILARITY_DF,
    REC_TYPE,
)
from offline_results.recommendation.homepage_recommendation.core.with_cf_item_to_item.item_to_item_utils import (
    ItemToItemUtils,
)
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.similarity.content_profile.query_utils import QueryUtils
from offline_results.utils import custom_exception, Logging


class CFIIFallback:
    local_cache: Dict[str, Any]
    graph: GraphDb

    def __init__(self, content_label):
        CFIIFallback.graph = ANGraphDb.new_connection_config().graph
        CFIIFallback.local_cache = {
            USER_LOG: ItemToItemUtils.read_join_viewed_from_s3(),
            HOMEPAGE_CONTENT_DF: ItemToItemUtils.homepage_data(content_label),
            ACTIVE_HOMEPAGE_ID_LIST: list(
                QueryUtils.active_homepage_ids(content_label)
            ),
            SIMILARITY_DF: ItemToItemUtils.get_similar_contents_based_on_all(
                content_label
            ),
        }

    @staticmethod
    @custom_exception()
    def get_default_user_log_for_homepage_based_rec(content_label):
        start_time = time.time()

        Logging.info(
            "Retrieving user log and homepage content mapping from the local cache"
        )

        homepage_data = CFIIFallback.local_cache[HOMEPAGE_CONTENT_DF]

        user_log = CFIIFallback.local_cache[USER_LOG]

        Logging.info("Getting all user log mapped with the homepage IDs")

        user_log_homepage = ItemToItemUtils.merge_on_content_id(user_log, homepage_data)

        Logging.info("Filtering data for only active contents")

        user_log_homepage = user_log_homepage[
            user_log_homepage[CONTENT_STATUS] == ACTIVE
        ].explode(column=HOMEPAGE_ID)

        Logging.info("Selecting the data for content label : {}".format(content_label))

        user_log_homepage = (
            user_log_homepage[user_log_homepage[IS_PAY_TV] == True]
            if content_label == PAY_TV_CONTENT
            else user_log_homepage[user_log_homepage[IS_PAY_TV] == False]
        )

        user_log_homepage = user_log_homepage[user_log_homepage[HOMEPAGE_ID].notnull()]

        Logging.info("Filtering data for only active homepage IDs")

        user_log_homepage[HOMEPAGE_ID] = user_log_homepage[HOMEPAGE_ID].astype(int64)

        active_homepage_df = DataFrame(
            CFIIFallback.local_cache[ACTIVE_HOMEPAGE_ID_LIST], columns=[HOMEPAGE_ID]
        )

        user_log_homepage = merge(
            user_log_homepage, active_homepage_df, on=[HOMEPAGE_ID]
        )

        Logging.info(
            "Getting homepage IDs dedicated to trending, popular, seasonal & BYW from config."
        )
        config_homepage = (
            DataFrame(CONFIG_HOMEPAGE_PAYTV.items(), columns=[HOMEPAGE_ID, MODEL_NAME])
            if content_label == PAY_TV_CONTENT
            else DataFrame(
                CONFIG_HOMEPAGE_NO_PAYTV.items(), columns=[HOMEPAGE_ID, MODEL_NAME]
            )
        )

        Logging.info("Eliminating these homepage IDs from current user log")
        user_log_with_paytv_status = merge(
            user_log_homepage,
            DataFrame(
                subtract(
                    set(user_log_homepage[HOMEPAGE_ID].to_numpy().tolist()),
                    set(config_homepage[HOMEPAGE_ID].to_numpy().tolist()),
                ),
                columns=[HOMEPAGE_ID],
            ),
            on=[HOMEPAGE_ID],
        )

        end_time = time.time()

        Logging.info(
            "Time taken for the process of receiving unique homepage IDs list: {} seconds".format(
                end_time - start_time
            )
        )
        return user_log_with_paytv_status

    @staticmethod
    @custom_exception()
    def get_default_item_to_item_recommendations_based_on_homepage_id(pay_tv_label):
        start_time = time.time()
        homepage_based_rec = {}
        key_prefix = (
            SERVICE_NAME
            + ":"
            + ITEM_TO_ITEM_DEFAULT_MODULE_NAME.lower()
            + ":"
            + pay_tv_label
            + ":"
            + HOMEPAGE_ID_BASED
        )

        user_log = CFIIFallback.get_default_user_log_for_homepage_based_rec(
            content_label=PAY_TV_CONTENT
            if pay_tv_label == PAY_TV
            else NO_PAY_TV_CONTENT
        )

        for homepage_id in sorted(user_log[HOMEPAGE_ID].unique()):
            key_prefix_cls = key_prefix + ":" + str(homepage_id)
            user_log_homepage_specific = user_log[user_log[HOMEPAGE_ID] == homepage_id]
            highest_view_df = (
                user_log_homepage_specific.groupby(CONTENT_ID, as_index=False)[
                    VIEW_COUNT
                ]
                .agg(SUM)
                .sort_values(by=VIEW_COUNT, ascending=False)
                .iloc[:1, :]
            )
            similarity_df = ItemToItemUtils.merge_on_content_id(
                highest_view_df, CFIIFallback.local_cache[SIMILARITY_DF]
            )
            df_for_json = (
                similarity_df[[RECOMMENDED_CONTENT_ID, SCORE]]
                .rename(columns={RECOMMENDED_CONTENT_ID: CONTENT_ID})
                .sort_values(by=SCORE, ascending=False)
                .head(10)
            )
            df_for_json[CREATED_ON] = datetime.utcnow().isoformat()
            df_for_json[REC_TYPE] = ITEM_TO_ITEM_DEFAULT_MODULE_NAME
            df_for_json[SCORE] = df_for_json[SCORE].apply(lambda x: round(x, 2))
            if (df_for_json is not None) and (len(df_for_json) != 0):
                homepage_based_rec[key_prefix_cls] = df_for_json.to_dict(RECORDS)

        end_time = time.time()

        Logging.info(
            "Time taken for preparing item to item results based on homepage_id: {} seconds".format(
                end_time - start_time
            )
        )

        return homepage_based_rec
