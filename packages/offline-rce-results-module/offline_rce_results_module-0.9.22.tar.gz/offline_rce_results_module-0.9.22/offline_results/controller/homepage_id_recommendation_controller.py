import logging
from datetime import datetime

from numpy import nan
from pandas import merge
from sklearn.preprocessing import MinMaxScaler

from offline_results.common.config import ENCODING_MODEL
from offline_results.common.constants import (
    CONTENT_ID,
    MINIBATCH_KMEANS,
    HOMEPAGE_ID,
    PAY_TV,
    SERVICE_NAME,
    SCORE,
    CLUSTER_ID,
    CREATED_ON,
    RECORDS,
    NO_PAY_TV,
    IS_PAYTV,
)
from offline_results.common.constants import (
    MLC_RANK_MODULE,
    FALLBACK_MLC_RANK_MODULE,
    REC_TYPE,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    SCORE_ROUNDOFF,
)
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation import (
    HomepageIdRecommendation,
)
from offline_results.recommendation.homepage_recommendation.core.with_preference_and_recency.p_r import (
    UserPrefBasedRecommendation,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception, Logging


class HomepageIdRecommendationController(
    RecommendationUtils,
    MeanUserFromCluster,
):
    @class_custom_exception()
    def get_data(
        self,
        pay_tv_label,
    ):
        try:
            self.cluster_ids = self.find_all_cluster_id(
                pay_tv_label="True" if pay_tv_label is PAY_TV else "False"
            )
            self.users_dist = self.get_all_user_cluster_dist(
                pay_tv_label=PAY_TV if pay_tv_label is PAY_TV else NO_PAY_TV
            )
            active_homepage_id = set(
                self.active_homepage_ids(
                    is_paytv=True if pay_tv_label is PAY_TV else False
                )
            )
            content_data = self.active_content_and_homepage_ids_with_ubd(
                PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
            )
            self.active_homepage_id = list(
                set(content_data[HOMEPAGE_ID]).intersection(active_homepage_id)
            )
        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def homepage_id_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_rec = {}
            key_prefix = SERVICE_NAME + ":" + MLC_RANK_MODULE + ":" + pay_tv_label
            logging.info("Create homepage recommendation for : " + key_prefix)
            ctl = HomepageIdRecommendation()
            encoding_model = ctl.load_model_from_s3(
                True if pay_tv_label is PAY_TV else False, ENCODING_MODEL
            )
            model = ctl.load_model_from_s3(True if pay_tv_label is PAY_TV else False)
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                try:
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    logging.info("Preparing recommendation for cluster_id : " + key_prefix_cls)
                    mean_user = MeanUserFromCluster.get_mean_user(
                        cluster_id=cluster_id,
                        users_dist=self.users_dist,
                        pay_tv_label=pay_tv_label,
                    )
                    result = ctl.generate_recommendations(
                        mean_user, model, encoding_model
                    )
                    result = result[
                        result[HOMEPAGE_ID].isin(tuple(self.active_homepage_id))
                    ]
                    result[CREATED_ON] = datetime.utcnow().isoformat()
                    result = result.sort_values(
                        SCORE, ascending=False, ignore_index=True
                    )
                    result = result.drop_duplicates(ignore_index=True)
                    result[REC_TYPE] = key_prefix_cls.split(":")[1]
                    result = result[[HOMEPAGE_ID, SCORE, CREATED_ON, REC_TYPE]]
                    result = self.round_score(result)
                    homepage_id_rec[key_prefix_cls.lower()] = result.to_dict(RECORDS)
                except Exception as e:
                    Logging.error(f"Error for cluster id: '{cluster_id}'. Error: {e}")
                    continue
            return homepage_id_rec
        except Exception as e:
            Logging.error(
                f"Error while preparing homepage id based recommendation for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def homepage_id_rec_data(self):
        # paytv homepage id recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_rec = self.homepage_id_rec(PAY_TV)

        # no_paytv homepage id recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_rec = self.homepage_id_rec(NO_PAY_TV)
        return pay_tv_homepage_id_rec, no_pay_tv_homepage_id_rec


class HomepageIdFallbackController(
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
            active_homepage_id = set(
                self.active_homepage_ids(
                    is_paytv=True if pay_tv_label is PAY_TV else False
                )
            )
            content_data = self.active_content_and_homepage_ids_with_ubd(
                PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
            )
            self.active_homepage_id = list(
                set(content_data[HOMEPAGE_ID]).intersection(active_homepage_id)
            )
            self.ctl = UserPrefBasedRecommendation()
            self.ctl.data_gathering(is_paytv, no_ubd=False)
            self.ctl.data_preprocessing()
            cluster_ids = self.ctl.cluster_pref[[MINIBATCH_KMEANS, IS_PAYTV]]
            self.cluster_ids = cluster_ids[cluster_ids[IS_PAYTV] == is_paytv]

        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def sort_on_homepage_id(self, is_paytv, df):
        content_with_homepage = self.content_having_homepage(is_paytv)
        content_with_homepage = content_with_homepage[
            content_with_homepage[HOMEPAGE_ID].isin(self.active_homepage_id)
        ]
        content = merge(content_with_homepage, df, on=CONTENT_ID, how="left")
        content[SCORE] = content[SCORE].replace({-1: 0})
        content = content.groupby([HOMEPAGE_ID])[SCORE].sum().reset_index()
        scaler = MinMaxScaler(
            feature_range=(float("0." + "0" * (SCORE_ROUNDOFF - 1) + "1"), 1)
        )
        content[SCORE] = (
            scaler.fit_transform(content[[SCORE]].to_numpy()).flatten().tolist()
        )
        content[SCORE] = 1 if content[SCORE].max() == 0 else content[SCORE]
        content = content.sort_values([SCORE], ascending=False, ignore_index=True)
        return content[[HOMEPAGE_ID, SCORE]]

    @class_custom_exception()
    def homepage_id_rec_data(self, pay_tv_label):
        try:
            rec = {}
            is_paytv = True if pay_tv_label is PAY_TV else False
            key_prefix = (
                SERVICE_NAME + ":" + FALLBACK_MLC_RANK_MODULE + ":" + pay_tv_label
            )
            result = self.ctl.generate_recommendation(is_paytv=is_paytv)
            result = self.sort_on_homepage_id(is_paytv, result)
            result[CLUSTER_ID] = nan
            result[CREATED_ON] = datetime.utcnow().isoformat()
            result[REC_TYPE] = key_prefix.split(":")[1]
            result = result[[HOMEPAGE_ID, SCORE, CREATED_ON, REC_TYPE]]
            result[SCORE] = result[SCORE].apply(lambda x: float("{0:.15f}".format(x)))
            result = self.round_score(result)
            rec[key_prefix.lower()] = result.to_dict("records")
            return rec
        except Exception as e:
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def homepage_id_fallback(self):
        # paytv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_rec = self.homepage_id_rec_data(PAY_TV)

        # no_paytv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_rec = self.homepage_id_rec_data(NO_PAY_TV)

        return pay_tv_homepage_id_rec, no_pay_tv_homepage_id_rec


# ctl = HomepageIdRecommendationController()
# x,y = ctl.homepage_id_rec_data()
#
# ctl = HomepageIdFallbackController()
# z,h = ctl.homepage_id_fallback()
#
# print(len(x), len(y), len(z),len(h))
#
# print(x,y)
# print(z,h)
