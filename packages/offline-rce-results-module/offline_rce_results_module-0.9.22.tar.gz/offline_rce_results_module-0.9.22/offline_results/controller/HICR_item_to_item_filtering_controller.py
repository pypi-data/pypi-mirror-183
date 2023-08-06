from datetime import datetime

from pandas import merge, DataFrame

from offline_results.common.constants import (
    PAY_TV_CONTENT,
    CONTENT_ID,
    MINIBATCH_KMEANS,
    HOMEPAGE_ID,
    PAY_TV,
    SERVICE_NAME,
    SCORE,
    CREATED_ON,
    RECORDS,
    ITEM_TO_ITEM_MODULE_NAME,
    ALL_CONTENT_BASED,
    NO_PAY_TV,
    CONTENT_STATUS,
    NO_PAY_TV_CONTENT,
    HOMEPAGE_ID_BASED,
    ACTIVE_LABEL,
    CONTENT_LABEL_COLUMN,
    REC_TYPE,
    CUSTOMER_ID,
    VIEW_HISTORY,
    ITEM_TO_ITEM_DEFAULT_MODULE_NAME,
    DEFAULT_CLUSTER_ID,
    TV_CHANNEL_LIST,
)
from offline_results.recommendation.homepage_recommendation.core.with_cf_item_to_item.cf_item_to_item import (
    CFItemtoItem,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.similarity.content_profile.similarity_all_contents import (
    SimilarityAllContents,
)
from offline_results.utils import custom_exception, class_custom_exception, Logging

from pandas import merge, DataFrame
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.similarity.content_profile.similarity_all_contents import (
    SimilarityAllContents,
)
from offline_results.recommendation.homepage_recommendation.core.with_cf_item_to_item.cf_item_to_item import (
    CFItemtoItem,
)
from offline_results.common.constants import (
    PAY_TV_CONTENT,
    CONTENT_ID,
    MINIBATCH_KMEANS,
    HOMEPAGE_ID,
    PAY_TV,
    SERVICE_NAME,
    SCORE,
    CREATED_ON,
    RECORDS,
    ITEM_TO_ITEM_MODULE_NAME,
    ALL_CONTENT_BASED,
    NO_PAY_TV,
    CONTENT_STATUS,
    NO_PAY_TV_CONTENT,
    HOMEPAGE_ID_BASED,
    ACTIVE_LABEL,
    CONTENT_LABEL_COLUMN,
    REC_TYPE,
    CUSTOMER_ID,
    VIEW_HISTORY,
    ITEM_TO_ITEM_DEFAULT_MODULE_NAME,
    DEFAULT_CLUSTER_ID,
)


class HICRItemToItemController(RecommendationUtils, MeanUserFromCluster, CFItemtoItem):
    ubd = DataFrame()
    paytv_content_similarity = DataFrame()
    no_paytv_content_similarity = DataFrame()
    pay_tv_content_ids = DataFrame()
    no_pay_tv_content_ids = DataFrame()
    paytv_users_dist = DataFrame()
    no_paytv_users_dist = DataFrame()
    live_tv_channel_paytv = []
    live_tv_channel_nopaytv = []

    def __init__(self):
        super(HICRItemToItemController, self).__init__()
        self.content_ids = DataFrame()
        self.users_dist = DataFrame()
        self.ubd = DataFrame()
        self.cluster_ids = []
        self.homepage_ids = []
        self.module_name = ITEM_TO_ITEM_MODULE_NAME
        self.content_similarity = {}

    @class_custom_exception()
    def fetch_data(
        self,
        pay_tv_label,
    ):
        try:
            obj = HICRItemToItemController
            content_label, is_paytv = (
                (PAY_TV_CONTENT, True)
                if pay_tv_label is PAY_TV
                else (NO_PAY_TV_CONTENT, False)
            )
            if (
                len(obj.ubd)
                == len(obj.paytv_content_similarity)
                == len(obj.no_paytv_content_similarity)
                == 0
            ):
                obj.ubd = RecommendationUtils.user_viewed_data_from_s3()
                obj.ubd = obj.ubd.drop(columns=[VIEW_HISTORY])
                csl = SimilarityAllContents()
                obj.paytv_content_similarity = (
                    csl.prepare_similarity_based_on_all_content(PAY_TV_CONTENT)
                )
                obj.no_paytv_content_similarity = (
                    csl.prepare_similarity_based_on_all_content(NO_PAY_TV_CONTENT)
                )
                obj.pay_tv_content_ids = obj.active_content_and_homepage_ids_with_ubd(
                    PAY_TV_CONTENT
                )
                obj.no_pay_tv_content_ids = (
                    obj.active_content_and_homepage_ids_with_ubd(NO_PAY_TV_CONTENT)
                )
                obj.paytv_users_dist = obj.get_all_user_cluster_dist(PAY_TV)
                obj.no_paytv_users_dist = obj.get_all_user_cluster_dist(NO_PAY_TV)
            self.content_ids = (
                obj.pay_tv_content_ids if is_paytv else obj.no_pay_tv_content_ids
            )
            self.users_dist = (
                obj.paytv_users_dist if is_paytv else obj.no_paytv_users_dist
            )
            self.cluster_ids = list(set(self.users_dist[MINIBATCH_KMEANS]))
            self.content_similarity = (
                obj.paytv_content_similarity
                if pay_tv_label == PAY_TV
                else obj.no_paytv_content_similarity
            )
            active_homepage_id = set(self.active_homepage_ids(is_paytv=is_paytv))
            self.homepage_ids = set(self.content_ids[HOMEPAGE_ID]).intersection(
                active_homepage_id
            )
            self.homepage_ids = list(
                self.homepage_ids - self.reserved_homepage_id(is_paytv)
            )
            ubd = obj.ubd[
                (obj.ubd[CONTENT_STATUS] == ACTIVE_LABEL)
                & (obj.ubd[CONTENT_LABEL_COLUMN] == content_label)
            ]
            ubd = merge(ubd, self.content_ids, on=CONTENT_ID, how="left")
            ubd = merge(ubd, self.users_dist, on=CUSTOMER_ID, how="left")
            ubd = ubd.dropna(axis=0).reset_index(drop=True)
            self.ubd = ubd
            obj.live_tv_channel_paytv = RecommendationUtils.get_tv_channels(is_pay_tv=True)
            obj.live_tv_channel_nopaytv = RecommendationUtils.get_tv_channels(is_pay_tv=False)

        except Exception as e:
            Logging.error(
                f"Error while preparing data for {pay_tv_label} recommendation, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def clear_data():
        obj = HICRItemToItemController
        obj.ubd = DataFrame()
        obj.paytv_content_similarity = DataFrame()
        obj.no_paytv_content_similarity = DataFrame()
        obj.pay_tv_content_ids = DataFrame()
        obj.no_pay_tv_content_ids = DataFrame()
        obj.paytv_users_dist = DataFrame()
        obj.no_paytv_users_dist = DataFrame()
        obj.live_tv_channel_paytv = []
        obj.live_tv_channel_nopaytv = []

    @class_custom_exception()
    def fetch_result(self, cluster_id=None, homepage_id=None, default_wise=False, pay_tv_label=PAY_TV,
                     homepage_id_wise=True):
        try:
            temp_ubd = (
                self.ubd.copy()
                if cluster_id is None
                else self.ubd[self.ubd[MINIBATCH_KMEANS] == cluster_id].copy()
            )
            temp_ubd = (
                temp_ubd
                if homepage_id is None
                else temp_ubd[temp_ubd[HOMEPAGE_ID] == homepage_id]
            )
            contents = (
                self.content_ids
                if homepage_id is None
                else self.content_ids[self.content_ids[HOMEPAGE_ID] == homepage_id]
            )
            result = self.generate_rec(
                temp_ubd,
                self.content_similarity.copy(),
                list(contents[CONTENT_ID]),
                default_wise,
                pay_tv_label,
                HICRItemToItemController.live_tv_channel_paytv,
                HICRItemToItemController.live_tv_channel_nopaytv,
                homepage_id_wise
            )
            result = result[result[CONTENT_ID].isin(self.content_ids[CONTENT_ID])]
            result[CREATED_ON] = datetime.utcnow().isoformat()
            result[REC_TYPE] = self.module_name.upper()
            result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
            if not homepage_id_wise:
                result = result[
                    ~result[CONTENT_ID].isin(HICRItemToItemController.live_tv_channel_paytv if pay_tv_label == PAY_TV
                                             else HICRItemToItemController.live_tv_channel_nopaytv)
                ]
            result = result.sort_values(SCORE, ascending=False, ignore_index=True)
            result = result.drop_duplicates(subset=[CONTENT_ID], ignore_index=True)
            result[SCORE] = result[SCORE].apply(lambda x: round(x, 2))
            return result

        except Exception as e:
            Logging.error(
                f"Error for cluster id {cluster_id} and homepage id {homepage_id}. Error: {e}"
            )

    @class_custom_exception()
    def cb_ii_homepage_id_based_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + self.module_name.lower()
                + ":"
                + pay_tv_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            for cluster_id in self.cluster_ids:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                Logging.info(
                    f"Preparing result for '{pay_tv_label}' content & cluster id: '{cluster_id}'..."
                )
                for homepage_id in list(self.homepage_ids):
                    key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                    result = self.fetch_result(cluster_id, homepage_id, pay_tv_label=pay_tv_label, homepage_id_wise=True)
                    if (result is not None) and (len(result) != 0):
                        homepage_id_based_rec[key_prefix_cls_hid] = result.to_dict(
                            RECORDS
                        )
            return homepage_id_based_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing homepage id based recommendation for {pay_tv_label}, Error: {e}"
            )
            return {}

    @class_custom_exception()
    def cb_ii_all_content_based_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + self.module_name.lower()
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            for cluster_id in self.cluster_ids:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                Logging.info(
                    f"Preparing result for '{pay_tv_label}' content & cluster id: '{cluster_id}'..."
                )
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                result = self.fetch_result(cluster_id, pay_tv_label=pay_tv_label, homepage_id_wise=False)
                if (result is not None) and (len(result) != 0):
                    all_content_based_rec[key_prefix_cls] = result.to_dict(RECORDS)
            return all_content_based_rec

        except Exception as e:
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )
            return {}

    @class_custom_exception()
    def fallback_cb_ii_all_content_based_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + self.module_name.lower()
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            result = self.fetch_result(default_wise=True, pay_tv_label=pay_tv_label, homepage_id_wise=False)
            all_content_based_rec[key_prefix] = (
                [] if result is None else result.to_dict(RECORDS)
            )
            return all_content_based_rec

        except Exception as e:
            Logging.error(
                f"Error while preparing fallback all content based rec for {pay_tv_label}, Error: {e}"
            )
            return {}

    @class_custom_exception()
    def cf_ii_homepage_id_data(self):
        # pay_tv homepage id content recommendation
        HICRItemToItemController.clear_data()
        self.pay_tv_label = PAY_TV
        self.fetch_data(PAY_TV)
        self.module_name = ITEM_TO_ITEM_MODULE_NAME
        pay_tv_homepage_id_based_rec = self.cb_ii_homepage_id_based_rec(PAY_TV)

        # no_pay_tv homepage id content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.fetch_data(NO_PAY_TV)
        no_pay_tv_homepage_id_based_rec = self.cb_ii_homepage_id_based_rec(NO_PAY_TV)

        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @class_custom_exception()
    def cf_ii_all_content_data(self):
        # pay_tv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.fetch_data(PAY_TV)
        self.module_name = ITEM_TO_ITEM_MODULE_NAME
        pay_tv_all_content_based_rec = self.cb_ii_all_content_based_rec(PAY_TV)

        # no_pay_tv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.fetch_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.cb_ii_all_content_based_rec(NO_PAY_TV)
        HICRItemToItemController.clear_data()

        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec

    @class_custom_exception()
    def fallback_cf_ii_all_content_data(self):
        # pay_tv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.fetch_data(PAY_TV)
        self.module_name = ITEM_TO_ITEM_DEFAULT_MODULE_NAME
        pay_tv_all_content_based_rec = self.fallback_cb_ii_all_content_based_rec(PAY_TV)

        # no_pay_tv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.fetch_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.fallback_cb_ii_all_content_based_rec(
            NO_PAY_TV
        )
        HICRItemToItemController.clear_data()

        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec


# if __name__ == '__main__':
#     ctl = HICRItemToItemController()
#     #x, y = ctl.cf_ii_homepage_id_data()
#     z, g = ctl.cf_ii_all_content_data()
#     e, h = ctl.fallback_cf_ii_all_content_data()
#     print()
