import time
from typing import Any, Dict

from offline_results.common.constants import (
    CONTENT_STATUS,
    ACTIVE,
    IS_PAY_TV,
    PAY_TV,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    USER_CLUSTER_INFO,
    HOMEPAGE_CONTENT_DF,
    ACTIVE_HOMEPAGE_ID_LIST,
)
from offline_results.recommendation.homepage_recommendation.core.with_cf_item_to_item.item_to_item_utils import (
    ItemToItemUtils,
)
from offline_results.similarity.content_profile.query_utils import QueryUtils
from offline_results.utils import custom_exception, Logging


class CFII:
    local_cache: Dict[str, Any]

    def __init__(self, content_label):
        CFII.local_cache = {
            USER_CLUSTER_INFO: ItemToItemUtils.user_cluster_mapping_with_user_log(),
            HOMEPAGE_CONTENT_DF: ItemToItemUtils.homepage_data(PAY_TV_CONTENT)
            if content_label == PAY_TV_CONTENT
            else ItemToItemUtils.homepage_data(NO_PAY_TV_CONTENT),
            ACTIVE_HOMEPAGE_ID_LIST: list(
                QueryUtils.active_homepage_ids(PAY_TV_CONTENT)
            )
            if content_label == PAY_TV_CONTENT
            else list(QueryUtils.active_homepage_ids(NO_PAY_TV_CONTENT)),
        }

    @staticmethod
    @custom_exception()
    def get_most_similar_contents_based_on_all_contents(paytv_label):
        start_time = time.time()
        user_cluster_map = CFII.local_cache[USER_CLUSTER_INFO]
        user_log_mapped_with_cluster = user_cluster_map[
            user_cluster_map[CONTENT_STATUS] == ACTIVE
        ]

        Logging.info("Dividing data based on paytv flag of the customers")

        content_label = PAY_TV_CONTENT if paytv_label == PAY_TV else NO_PAY_TV_CONTENT

        user_log = (
            user_log_mapped_with_cluster[
                user_log_mapped_with_cluster[IS_PAY_TV] == True
            ]
            if content_label == PAY_TV_CONTENT
            else user_log_mapped_with_cluster[
                user_log_mapped_with_cluster[IS_PAY_TV] == False
            ]
        )

        Logging.info(
            "Getting most similar contents for {} : based on all contents".format(
                content_label
            )
        )

        paytv_df = ItemToItemUtils.get_similar_contents_based_on_all(content_label)

        Logging.info("Preparing expected output schema")

        resp = ItemToItemUtils.cf_ii_all_content_based_rec(
            user_log, paytv_df, paytv_label
        )

        end_time = time.time()

        Logging.info(
            "Time taken to prepare response based on all contents: {} seconds".format(
                end_time - start_time
            )
        )

        return resp
