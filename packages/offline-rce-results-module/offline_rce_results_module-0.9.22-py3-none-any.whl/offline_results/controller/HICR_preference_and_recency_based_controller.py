from datetime import datetime

from offline_results.common.constants import (
    CONTENT_ID,
    MINIBATCH_KMEANS,
    PAY_TV,
    HOMEPAGE_ID_BASED,
    SERVICE_NAME,
    SCORE,
    CREATED_ON,
    RECORDS,
    ALL_CONTENT_BASED,
    NO_PAY_TV,
    PREFERENCE_AND_RECENCY_MODULE,
    IS_PAYTV,
    FALLBACK_PREFERENCE_AND_RECENCY_MODULE,
    REC_TYPE,
    DEFAULT_CLUSTER_ID,
)
from offline_results.recommendation.homepage_recommendation.core.with_preference_and_recency.p_r import (
    UserPrefBasedRecommendation,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception, Logging


class HICRPreferenceAndRecencyController(
    RecommendationUtils,
    MeanUserFromCluster,
):
    @class_custom_exception()
    def get_data(
        self,
        pay_tv_label,
    ):
        try:
            # self.cluster_ids = self.find_all_cluster_id(pay_tv_label='True' if pay_tv_label is PAY_TV else 'False')
            is_paytv = True if pay_tv_label is PAY_TV else False
            active_homepage_id = set(self.active_homepage_ids(is_paytv=is_paytv))
            self.active_homepage_id = list(
                active_homepage_id - self.reserved_homepage_id(is_paytv)
            )
            self.ctl = UserPrefBasedRecommendation()
            self.ctl.data_gathering(is_paytv)
            self.ctl.data_preprocessing()
            cluster_ids = self.ctl.cluster_pref[[MINIBATCH_KMEANS, IS_PAYTV]]
            self.cluster_ids = cluster_ids[cluster_ids[IS_PAYTV] == is_paytv]
            act_content = self.content_having_homepage(is_paytv)
            self.ctl.content_properties = self.ctl.content_properties[
                self.ctl.content_properties[CONTENT_ID].isin(act_content[CONTENT_ID])
            ]

        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def homepage_id_based_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_based_rec = {}
            is_paytv = True if pay_tv_label is PAY_TV else False
            key_prefix = (
                SERVICE_NAME
                + ":"
                + PREFERENCE_AND_RECENCY_MODULE
                + ":"
                + pay_tv_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                Logging.info(
                    f"preparing result for '{pay_tv_label}' users and cluster id '{cluster_id}' : homepage id based"
                )
                for homepage_id in self.active_homepage_id:
                    try:
                        key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                        result = self.ctl.generate_recommendation(
                            cluster_id=cluster_id,
                            homepage_id=homepage_id,
                            is_paytv=is_paytv,
                        )
                        if len(result) == 0:
                            continue
                        result[CREATED_ON] = datetime.utcnow().isoformat()
                        result[REC_TYPE] = key_prefix_cls_hid.split(":")[1]
                        result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                        homepage_id_based_rec[
                            key_prefix_cls_hid.lower()
                        ] = result.to_dict(RECORDS)
                    except Exception as e:
                        Logging.error(
                            f"Error for cluster id: '{cluster_id}' and homepage id: '{homepage_id}'. Error: {e}"
                        )
                        continue
            return homepage_id_based_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing homepage id based recommendation for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def all_content_based_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            is_paytv = True if pay_tv_label == PAY_TV else False
            tv_channel = RecommendationUtils.get_tv_channels(is_paytv)
            is_paytv = True if pay_tv_label is PAY_TV else False
            key_prefix = (
                SERVICE_NAME
                + ":"
                + PREFERENCE_AND_RECENCY_MODULE
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                try:
                    Logging.info(
                        f"preparing result for '{pay_tv_label}' users and cluster id '{cluster_id}' : all content based"
                    )
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    result = self.ctl.generate_recommendation(
                        cluster_id=cluster_id, is_paytv=is_paytv
                    )
                    if len(result) == 0:
                        continue
                    result = result[~result[CONTENT_ID].isin(tv_channel)]
                    result[CREATED_ON] = datetime.utcnow().isoformat()
                    result = result.drop_duplicates(subset=[CONTENT_ID])
                    result[REC_TYPE] = key_prefix_cls.split(":")[1]
                    result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                    all_content_based_rec[key_prefix_cls.lower()] = result.to_dict(
                        "records"
                    )
                except Exception as e:
                    Logging.error(f"Error for cluster id: '{cluster_id}'. Error: {e}")
                    continue
            return all_content_based_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def preference_and_recency_based_homepage_id_data(self):
        # paytv homepage id content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_based_rec = self.homepage_id_based_rec(PAY_TV)

        # no_paytv homepage id content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_based_rec = self.homepage_id_based_rec(NO_PAY_TV)

        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @class_custom_exception()
    def preference_and_recency_based_all_content_data(self):
        # paytv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_all_content_based_rec = self.all_content_based_rec(PAY_TV)

        # no_paytv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.all_content_based_rec(NO_PAY_TV)

        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec


class HICRPreferenceAndRecencyFallbackController(
    RecommendationUtils,
    MeanUserFromCluster,
):
    @class_custom_exception()
    def get_data(
        self,
        pay_tv_label,
    ):
        try:
            is_paytv = True if pay_tv_label is PAY_TV else False
            self.active_homepage_id = list(
                set(self.active_homepage_ids(is_paytv=is_paytv))
            )
            self.ctl = UserPrefBasedRecommendation()
            self.ctl.data_gathering(is_paytv)
            self.ctl.data_preprocessing()
            cluster_ids = self.ctl.cluster_pref[[MINIBATCH_KMEANS, IS_PAYTV]]
            self.cluster_ids = cluster_ids[cluster_ids[IS_PAYTV] == is_paytv]

        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def homepage_id_based_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_based_rec = {}
            is_paytv = True if pay_tv_label is PAY_TV else False
            key_prefix = (
                SERVICE_NAME
                + ":"
                + FALLBACK_PREFERENCE_AND_RECENCY_MODULE
                + ":"
                + pay_tv_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            for homepage_id in self.active_homepage_id:
                try:

                    key_prefix_cls_hid = key_prefix + ":" + str(homepage_id)
                    Logging.info(f"preparing result for '{key_prefix_cls_hid}'")
                    result = self.ctl.generate_recommendation(
                        homepage_id=homepage_id,
                        cluster_id=DEFAULT_CLUSTER_ID,
                        is_paytv=is_paytv,
                    )
                    if len(result) == 0:
                        continue
                    result[CREATED_ON] = datetime.utcnow().isoformat()
                    result[REC_TYPE] = key_prefix_cls_hid.split(":")[1]
                    result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                    homepage_id_based_rec[key_prefix_cls_hid.lower()] = result.to_dict(
                        RECORDS
                    )
                except Exception as e:
                    Logging.error(f"Error for homepage id: '{homepage_id}'. Error: {e}")
                    continue
            return homepage_id_based_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing homepage id based recommendation for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def all_content_based_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            is_paytv = True if pay_tv_label is PAY_TV else False
            tv_channel = RecommendationUtils.get_tv_channels(is_paytv)
            key_prefix_cls = (
                SERVICE_NAME
                + ":"
                + FALLBACK_PREFERENCE_AND_RECENCY_MODULE
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            Logging.info(f"preparing result for '{key_prefix_cls}'")
            result = self.ctl.generate_recommendation(
                is_paytv=is_paytv, cluster_id=DEFAULT_CLUSTER_ID
            )
            result[CREATED_ON] = datetime.utcnow().isoformat()
            result = result.drop_duplicates(subset=[CONTENT_ID])
            result = result[~result[CONTENT_ID].isin(tv_channel)]
            result[REC_TYPE] = key_prefix_cls.split(":")[1]
            result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
            all_content_based_rec[key_prefix_cls.lower()] = result.to_dict("records")
            return all_content_based_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def fallback_preference_and_recency_based_homepage_id_data(self):
        # paytv homepage id content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_based_rec = self.homepage_id_based_rec(PAY_TV)

        # no_paytv homepage id content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_based_rec = self.homepage_id_based_rec(NO_PAY_TV)

        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @class_custom_exception()
    def fallback_preference_and_recency_based_all_content_data(self):
        # paytv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_all_content_based_rec = self.all_content_based_rec(PAY_TV)

        # no_paytv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.all_content_based_rec(NO_PAY_TV)

        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec


#
# ctl = HICRPreferenceAndRecencyController()
# x,y = ctl.preference_and_recency_based_homepage_id_data()
# z,g = ctl.preference_and_recency_based_all_content_data()
#
# ctl = HICRPreferenceAndRecencyFallbackController()
# h,c = ctl.fallback_preference_and_recency_based_homepage_id_data()
# f,n = ctl.fallback_preference_and_recency_based_all_content_data()
#
#
# print(len(x), len(y), len(z),len(g))
# print(len(h), len(c), len(f),len(n))
