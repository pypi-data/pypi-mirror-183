from datetime import datetime
from pandas import merge, DataFrame, concat

from offline_results.common.constants import (
    PAY_TV_CONTENT,
    CONTENT_ID,
    MINIBATCH_KMEANS,
    HOMEPAGE_ID,
    PAY_TV,
    HOMEPAGE_ID_BASED,
    SERVICE_NAME,
    SCORE,
    CLUSTER_ID,
    CREATED_ON,
    RECORDS,
    ALL_CONTENT_BASED,
    NO_PAY_TV,
    NO_PAY_TV_CONTENT,
    USER_TO_USER_MODULE_NAME,
    USER_SIMILAR_COUNT,
    IS_PAY_TV,
    CUSTOMER_ID,
    ACTIVE_LABEL,
    CONTENT_STATUS,
    CONTENT_LABEL_COLUMN,
    VIEW_COUNT,
    FALLBACK_USER_TO_USER_MODULE,
    REC_TYPE,
    DEFAULT_CLUSTER_ID, DURATION, RIGHT, LEFT
)
from offline_results.recommendation.homepage_recommendation.core.with_cf_user_to_user.controller import (
    UserViewershipController,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, class_custom_exception, Logging


class HICRUserToUserFilteringController(
    RecommendationUtils, MeanUserFromCluster, UserViewershipController
):
    @class_custom_exception()
    def get_data(
        self,
        pay_tv_label,
    ):
        try:
            is_paytv, paytv_content = (
                (True, PAY_TV_CONTENT)
                if pay_tv_label is PAY_TV
                else (False, NO_PAY_TV_CONTENT)
            )
            self.user_cluster = self.user_cluster_from_s3()[
                [CLUSTER_ID, CUSTOMER_ID, IS_PAY_TV]
            ]
            self.user_cluster = self.user_cluster[
                self.user_cluster[IS_PAY_TV] == is_paytv
            ]
            viewed = self.user_viewed_data_from_s3()
            self.viewed = viewed[
                (viewed[CONTENT_STATUS] == ACTIVE_LABEL)
                & (viewed[IS_PAY_TV] == is_paytv)
                & (viewed[CONTENT_LABEL_COLUMN] == paytv_content)
            ]
            self.cluster_ids = DataFrame(
                {MINIBATCH_KMEANS: list(set(self.user_cluster[CLUSTER_ID]))}
            )
            self.users_dist = self.get_all_user_cluster_dist(pay_tv_label=pay_tv_label)
            self.content_with_homepage = self.active_content_and_homepage_ids_with_ubd(
                pay_tv_label=paytv_content
            )
            active_homepage_id = set(
                self.active_homepage_ids(
                    is_paytv=True if pay_tv_label is PAY_TV else False
                )
            )
            content_data = self.active_content_and_homepage_ids_with_ubd(
                PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
            )
            self.active_homepage_id = set(content_data[HOMEPAGE_ID]).intersection(
                active_homepage_id
            )
            self.active_homepage_id = list(
                self.active_homepage_id - self.reserved_homepage_id(is_paytv)
            )
        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def user_based_homepage_id_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + USER_TO_USER_MODULE_NAME
                + ":"
                + pay_tv_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                is_paytv = True if pay_tv_label is PAY_TV else False
                similar_users = self.user_cluster[
                    self.user_cluster[CLUSTER_ID] == cluster_id
                ].head(USER_SIMILAR_COUNT)
                similar_users = list(similar_users[CUSTOMER_ID])
                for homepage_id in list(self.active_homepage_id):
                    try:
                        Logging.info(
                            f"processing cluster id: {cluster_id} and homepage id: {homepage_id} for {pay_tv_label}."
                        )
                        key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                        homepage_content = self.content_with_homepage[
                            self.content_with_homepage[HOMEPAGE_ID] == homepage_id
                        ]
                        if len(homepage_content) == 0:
                            continue
                        result = self.controller(
                            tuple(set(homepage_content[CONTENT_ID].to_list())),
                            similar_users,
                            is_paytv,
                            self.viewed,
                        )
                        if len(result) == 0:
                            continue
                        result[CREATED_ON] = datetime.utcnow().isoformat()
                        result = result.drop_duplicates(ignore_index=True)
                        result = result.sort_values(SCORE, ascending=False, ignore_index=True)
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
    def user_based_all_content_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            key_prefix = (
                SERVICE_NAME
                + ":"
                + USER_TO_USER_MODULE_NAME
                + ":"
                + pay_tv_label
                + ":"
                + ALL_CONTENT_BASED
            )
            is_paytv = True if pay_tv_label is PAY_TV else False
            tv_channel = RecommendationUtils.get_tv_channels(is_paytv)
            viewed_df = self.viewed[~self.viewed[CONTENT_ID].isin(tv_channel)].reset_index(drop=True)
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                Logging.info(
                    f"processing cluster id: {cluster_id} for {pay_tv_label} : all content based"
                )
                try:
                    similar_users = self.user_cluster[
                        self.user_cluster[CLUSTER_ID] == cluster_id
                    ].head(USER_SIMILAR_COUNT)
                    similar_users = list(similar_users[CUSTOMER_ID])
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    if len(set(self.content_with_homepage[CONTENT_ID].to_list())) == 0:
                        continue
                    result = self.controller(
                        tuple(set(self.content_with_homepage[CONTENT_ID].to_list())),
                        similar_users,
                        is_paytv,
                        viewed_df,
                    )
                    result = merge(
                        self.content_with_homepage, result, on=CONTENT_ID, how=RIGHT
                    ).reset_index(drop=True)
                    result = result.drop_duplicates(subset=[CONTENT_ID])
                    result[CREATED_ON] = datetime.utcnow().isoformat()
                    result = result.sort_values(SCORE, ascending=False, ignore_index=True)
                    result[REC_TYPE] = key_prefix_cls.split(":")[1]
                    result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                    if len(result.index) > 0:
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
    def user_based_filtering_homepage_id_data(self):
        # paytv homepage id content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_based_rec = self.user_based_homepage_id_rec(PAY_TV)

        # no_paytv homepage id content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_based_rec = self.user_based_homepage_id_rec(NO_PAY_TV)
        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @class_custom_exception()
    def user_based_filtering_all_content_data(self):
        # paytv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_all_content_based_rec = self.user_based_all_content_rec(PAY_TV)

        # no_paytv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.user_based_all_content_rec(NO_PAY_TV)

        Logging.info("Successfully compute the recommendation")
        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec

    @staticmethod
    @custom_exception()
    def data_preprocessing(
        pay_tv_label,
        ctl,
        rec_type,
    ):
        ctl.pay_tv_label = pay_tv_label
        ctl.get_data(pay_tv_label)
        pay_tv_content_label = (
            PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
        )
        viewed = ctl.viewed[
            ctl.viewed[CONTENT_LABEL_COLUMN] == pay_tv_content_label
        ].copy()
        is_paytv = True if pay_tv_label == PAY_TV else False
        tv_channel = RecommendationUtils.get_tv_channels(is_paytv)
        if rec_type == ALL_CONTENT_BASED:
            viewed = viewed[~viewed[CONTENT_ID].isin(tv_channel)]
        content_duration_counts = ctl.calculate_total_duration(viewed)
        viewed = viewed.groupby([CONTENT_ID])[VIEW_COUNT].sum().reset_index()
        viewed = merge(
            viewed, content_duration_counts, on=CONTENT_ID, how=LEFT
        ).reset_index(drop=True)
        viewed = merge(
            viewed,
            ctl.content_with_homepage[[CONTENT_ID, HOMEPAGE_ID]],
            on=CONTENT_ID,
            how=LEFT,
        )
        remaining_id = set(ctl.content_with_homepage[CONTENT_ID]).difference(
            set(viewed[CONTENT_ID])
        )
        remaining_id = ctl.content_with_homepage[
            ctl.content_with_homepage[CONTENT_ID].isin(remaining_id)
        ].copy()
        remaining_id[VIEW_COUNT] = -1
        viewed = concat(
            [viewed, remaining_id[[VIEW_COUNT, CONTENT_ID, HOMEPAGE_ID]]], axis=0
        ).reset_index(drop=True)
        key = (
            SERVICE_NAME
            + ":"
            + FALLBACK_USER_TO_USER_MODULE
            + ":"
            + pay_tv_label
            + ":"
            + rec_type
        )
        return viewed, key

    @staticmethod
    @custom_exception()
    def generate_rec(rec_type, df, key, homepage_ids=None):
        rec = {}
        if rec_type == ALL_CONTENT_BASED:
            df[CREATED_ON] = datetime.utcnow().isoformat()
            df[[VIEW_COUNT, DURATION]] = df[[VIEW_COUNT, DURATION]].fillna(value=0)
            df[SCORE] = (df[VIEW_COUNT] * 0.5) + (df[DURATION] * 0.5)
            df = RecommendationUtils.round_score(df)
            df = df.drop_duplicates(subset=[CONTENT_ID])
            df[REC_TYPE] = key.split(":")[1]
            df = df[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
            rec[key.lower()] = df.to_dict(RECORDS)
            return rec
        for homepage_id in homepage_ids:
            try:
                Logging.info(f"processing for {key}:{homepage_id}")
                data = df[df[HOMEPAGE_ID] == homepage_id].copy()
                if len(data) == 0:
                    continue
                data[CREATED_ON] = datetime.utcnow().isoformat()
                data[[VIEW_COUNT, DURATION]] = data[[VIEW_COUNT, DURATION]].fillna(value=0)
                data[SCORE] = (data[VIEW_COUNT] * 0.5) + (data[DURATION] * 0.5)
                data = RecommendationUtils.round_score(data)
                data[SCORE] = 1 if data[SCORE].max() == 0.001 else data[SCORE]
                data[REC_TYPE] = key.split(":")[1]
                data = data[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                rec[key.lower() + ":" + str(homepage_id)] = data.to_dict(RECORDS)
            except Exception as e:
                Logging.error(f"Error for homepage id: '{homepage_id}'. Error: {e}")
                continue
        return rec

    @staticmethod
    @custom_exception()
    def fallback_homepage_id_data():

        ctl = HICRUserToUserFilteringController()

        # #fallback no_paytv homepage id content recommendation
        paytv_viewed, key = ctl.data_preprocessing(PAY_TV, ctl, HOMEPAGE_ID_BASED)
        pay_tv_homepage_id_based_rec = ctl.generate_rec(
            HOMEPAGE_ID_BASED, paytv_viewed, key, ctl.active_homepage_id
        )

        # fallback no_paytv homepage id content recommendation
        no_paytv_viewed, key = ctl.data_preprocessing(NO_PAY_TV, ctl, HOMEPAGE_ID_BASED)
        no_pay_tv_homepage_id_based_rec = ctl.generate_rec(
            HOMEPAGE_ID_BASED, no_paytv_viewed, key, ctl.active_homepage_id
        )
        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @staticmethod
    @custom_exception()
    def fallback_all_content_data():

        ctl = HICRUserToUserFilteringController()

        # fallback no_paytv homepage id content recommendation
        paytv_rating, key = ctl.data_preprocessing(PAY_TV, ctl, ALL_CONTENT_BASED)
        pay_tv_all_content_based_rec = ctl.generate_rec(
            ALL_CONTENT_BASED, paytv_rating, key
        )

        # fallback no_paytv homepage id content recommendation
        no_paytv_rating, key = ctl.data_preprocessing(NO_PAY_TV, ctl, ALL_CONTENT_BASED)
        no_pay_tv_all_content_based_rec = ctl.generate_rec(
            ALL_CONTENT_BASED, no_paytv_rating, key
        )
        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec


# ctl = HICRUserToUserFilteringController()
# x,y = ctl.user_based_filtering_homepage_id_data()
# z,g = ctl.user_based_filtering_all_content_data()
#
# h,c = ctl.fallback_homepage_id_data()
# f,n = ctl.fallback_all_content_data()
#
# print(len(x), len(y), len(z),len(g))
# print(len(h), len(c), len(f),len(n))
# print(x, y)
# print(z, g)
