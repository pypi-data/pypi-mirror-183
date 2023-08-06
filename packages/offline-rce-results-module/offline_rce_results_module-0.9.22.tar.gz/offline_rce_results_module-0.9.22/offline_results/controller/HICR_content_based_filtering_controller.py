import pickle
from datetime import datetime

from numpy import nan
from pandas import merge, concat, DataFrame
from sklearn.preprocessing import MinMaxScaler

from offline_results.common.constants import (
    PAY_TV_CONTENT,
    CONTENT_ID,
    MINIBATCH_KMEANS,
    HOMEPAGE_ID,
    PAY_TV,
    CBF_MODULE_NAME,
    HOMEPAGE_ID_BASED,
    SERVICE_NAME,
    SCORE,
    CLUSTER_ID,
    CREATED_ON,
    RECORDS,
    ALL_CONTENT_BASED,
    NO_PAY_TV,
    NO_PAY_TV_CONTENT,
    CONTENT_STATUS,
    ACTIVE_LABEL,
    CONTENT_LABEL_COLUMN,
    IMPLICIT_RATING,
    CBF_FALLBACK_MODULE_NAME,
    REC_TYPE,
    SIMILAR_USER_COUNT,
    CUSTOMER_ID,
    IS_PAY_TV,
    DEFAULT_CLUSTER_ID, DISTANCE_FROM_MEAN_USER,
)
from offline_results.recommendation.homepage_cluster_category.config import (
    MIN_CONTENT_HAVING_RATING,
    MIN_USER_GIVEN_RATING,
)
from offline_results.recommendation.homepage_recommendation.core.with_content_based_filtering.generate_recommendation import (
    HomepageIdContentScorePred,
)
from offline_results.recommendation.mean_user_from_cluster import MeanUserFromCluster
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, class_custom_exception, Logging


class HICRContentBasedFilteringController(
    RecommendationUtils, MeanUserFromCluster, HomepageIdContentScorePred
):
    paytv_cluster_ids = DataFrame()
    paytv_users_dist = DataFrame()
    paytv_content_with_homepage = DataFrame()
    no_paytv_cluster_ids = DataFrame()
    no_paytv_users_dist = DataFrame()
    no_paytv_content_with_homepage = DataFrame()
    implicit_rating = DataFrame()
    implicit_rating_all = DataFrame()
    cbf_model = pickle.dumps({})

    @class_custom_exception()
    def load_from_cache(self, pay_tv_label, obj):
        is_paytv, content_type = (
            (True, PAY_TV_CONTENT)
            if pay_tv_label is PAY_TV
            else (False, NO_PAY_TV_CONTENT)
        )
        self.cluster_ids = (
            obj.paytv_cluster_ids.copy()
            if pay_tv_label == PAY_TV
            else obj.no_paytv_cluster_ids.copy()
        )
        self.users_dist = (
            obj.paytv_users_dist.copy()
            if pay_tv_label == PAY_TV
            else obj.no_paytv_users_dist.copy()
        )
        self.content_with_homepage = obj.active_content_and_homepage_ids_with_ubd(
            content_type
        )
        active_homepage_id = set(self.active_homepage_ids(is_paytv=is_paytv))
        self.active_homepage_id = set(
            self.content_with_homepage[HOMEPAGE_ID]
        ).intersection(active_homepage_id)
        self.active_homepage_id = list(
            self.active_homepage_id - self.reserved_homepage_id(is_paytv)
        )
        self.cbf_model = (
            obj.cbf_model
            if obj.cbf_model != pickle.dumps({})
            else self.load_model_from_s3()
        )
        self.implicit_rating_all = obj.implicit_rating_all
    @class_custom_exception()
    def clear_data(self):

        ctl = HICRContentBasedFilteringController
        ctl.paytv_cluster_ids = DataFrame()
        ctl.paytv_users_dist = DataFrame()
        ctl.paytv_content_with_homepage = DataFrame()
        ctl.no_paytv_cluster_ids = DataFrame()
        ctl.no_paytv_users_dist = DataFrame()
        ctl.no_paytv_content_with_homepage = DataFrame()
        ctl.implicit_rating = DataFrame()
        ctl.implicit_rating_all = DataFrame()
        ctl.cbf_model = pickle.dumps({})

    @class_custom_exception()
    def get_data(
        self,
        pay_tv_label,
    ):
        try:
            obj = HICRContentBasedFilteringController
            if len(obj.paytv_cluster_ids) != 0:
                self.load_from_cache(pay_tv_label, obj)
                return
            obj.paytv_cluster_ids = self.find_all_cluster_id(pay_tv_label="True")
            obj.paytv_users_dist = self.get_all_user_cluster_dist(pay_tv_label=PAY_TV)
            obj.paytv_content_with_homepage = (
                self.active_content_and_homepage_ids_with_ubd(PAY_TV_CONTENT)
            )
            obj.no_paytv_cluster_ids = self.find_all_cluster_id(pay_tv_label="False")
            obj.no_paytv_users_dist = self.get_all_user_cluster_dist(
                pay_tv_label=NO_PAY_TV
            )
            obj.no_paytv_content_with_homepage = (
                self.active_content_and_homepage_ids_with_ubd(NO_PAY_TV_CONTENT)
            )
            obj.cbf_model = self.load_model_from_s3()
            obj_rating = self.implicit_rating_data_from_s3()
            obj.implicit_rating_all = obj_rating
            obj.implicit_rating = self.filter_rating_df(
                obj_rating, obj.paytv_users_dist, obj.no_paytv_users_dist
            )

            self.load_from_cache(pay_tv_label, obj)
        except Exception as e:
            Logging.error(f"Error while preparing data for {pay_tv_label}, Error: {e}")

    @class_custom_exception()
    def slice_similar_users(
        self, similar_user_df, cluster_id, no_of_users=SIMILAR_USER_COUNT
    ):
        try:
            is_pay_tv = True if self.pay_tv_label is PAY_TV else False
            rating = HICRContentBasedFilteringController.implicit_rating
            rating = rating[rating[IS_PAY_TV] == is_pay_tv]
            rating = rating[rating[MINIBATCH_KMEANS] == cluster_id]
            rating = rating[CUSTOMER_ID].to_list()
            similar_user_temp_df = similar_user_df[
                similar_user_df[CUSTOMER_ID].isin(rating)
            ]
            if len(similar_user_temp_df) > 0:
                return similar_user_temp_df
            else:
                similar_user_df = similar_user_df.round({DISTANCE_FROM_MEAN_USER: 1})
                similar_user_df = similar_user_df.drop_duplicates(subset=DISTANCE_FROM_MEAN_USER, ignore_index=True)
                return similar_user_df
        except Exception as e:
            Logging.error(f"Error while calculating similar user. Error {e}")
            return similar_user_df.head(no_of_users)

    @class_custom_exception()
    def filter_rating_df(self, dataset, paytv_user_dist, no_paytv_user_dist):
        try:
            user_dist = concat([paytv_user_dist, no_paytv_user_dist], ignore_index=True)
            filter_items = (
                dataset[CONTENT_ID].value_counts() > MIN_CONTENT_HAVING_RATING
            )
            filter_items = filter_items[filter_items].index.tolist()
            filter_users = dataset[CUSTOMER_ID].value_counts() > MIN_USER_GIVEN_RATING
            filter_users = filter_users[filter_users].index.tolist()
            dataset = dataset[
                (dataset[CONTENT_ID].isin(filter_items))
                & (dataset[CUSTOMER_ID].isin(filter_users))
            ]
            dataset = merge(
                dataset, user_dist, how="left", on=CUSTOMER_ID
            ).reset_index()
            return dataset[[CUSTOMER_ID, CONTENT_ID, IS_PAY_TV, MINIBATCH_KMEANS]]
        except Exception as e:
            Logging.error(f"Error while filtering data. Error :{e}")
            return dataset

    @class_custom_exception()
    def cbf_homepage_id_based_rec(
        self,
        pay_tv_label,
    ):
        try:
            homepage_id_based_rec = {}
            key_ = CBF_MODULE_NAME.lower()
            key_prefix = (
                SERVICE_NAME + ":" + key_ + ":" + pay_tv_label + ":" + HOMEPAGE_ID_BASED
            )
            for cluster_id in self.cluster_ids[MINIBATCH_KMEANS]:
                if cluster_id == DEFAULT_CLUSTER_ID:
                    continue
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                Logging.info(
                    f"CBF Homepage id based:- Preparing result for '{pay_tv_label}' content & cluster id: '{cluster_id}'..."
                )
                mean_user = MeanUserFromCluster.get_mean_user(
                    cluster_id, pay_tv_label, self.users_dist
                )
                similar_user = self.similar_users(
                    cluster_id, pay_tv_label, self.users_dist, None, mean_user
                )
                similar_user = self.slice_similar_users(
                    similar_user, cluster_id, SIMILAR_USER_COUNT
                )
                for homepage_id in list(self.active_homepage_id):
                    try:
                        key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                        homepage_content = self.content_with_homepage[
                            self.content_with_homepage[HOMEPAGE_ID] == homepage_id
                        ]
                        result = self.get_score(
                            users=similar_user,
                            contents=homepage_content[CONTENT_ID].to_list(),
                            implicit_rating=self.implicit_rating_all,
                            model=self.cbf_model,
                        )
                        result[CREATED_ON] = datetime.utcnow().isoformat()
                        result[REC_TYPE] = CBF_MODULE_NAME
                        result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                        result = result.drop_duplicates(ignore_index=True)
                        result = self.round_score(result)
                        homepage_id_based_rec[key_prefix_cls_hid] = result.to_dict(
                            RECORDS
                        )
                    except Exception as e:
                        Logging.error(
                            f"Error for cluster id {cluster_id} and homepage id {homepage_id}. Error: {e}"
                        )
                        continue
            return homepage_id_based_rec
        except Exception as e:
            self.clear_data()
            Logging.error(
                f"Error while preparing homepage id based recommendation for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def cbf_all_content_based_rec(self, pay_tv_label):
        try:
            all_content_based_rec = {}
            is_paytv = True if pay_tv_label is PAY_TV else False
            tv_channel = self.get_tv_channels(is_paytv)
            key_prefix = (
                SERVICE_NAME
                + ":"
                + CBF_MODULE_NAME
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
                        f"CBF All content based:- Preparing result for '{pay_tv_label}' content & cluster id: '{cluster_id}'..."
                    )
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    mean_user = MeanUserFromCluster.get_mean_user(
                        cluster_id=cluster_id,
                        users_dist=self.users_dist,
                        pay_tv_label=pay_tv_label,
                    )
                    similar_user = self.similar_users(
                        cluster_id,
                        pay_tv_label,
                        self.users_dist,
                        SIMILAR_USER_COUNT,
                        mean_user,
                    )
                    similar_user = self.slice_similar_users(
                        similar_user, cluster_id, SIMILAR_USER_COUNT
                    )
                    result = self.get_score(
                        users=similar_user,
                        contents=self.content_with_homepage[CONTENT_ID].to_list(),
                        implicit_rating=self.implicit_rating_all,
                        model=self.cbf_model,
                    )
                    result[CREATED_ON] = datetime.utcnow().isoformat()
                    result[REC_TYPE] = CBF_MODULE_NAME
                    result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                    result = result.groupby(CONTENT_ID).first().reset_index()
                    result = result.sort_values(
                        SCORE, ascending=False, ignore_index=True
                    )
                    result = result.drop_duplicates(subset=[CONTENT_ID])
                    result = result[~result[CONTENT_ID].isin(tv_channel)]
                    result = self.round_score(result)
                    all_content_based_rec[key_prefix_cls.lower()] = result.to_dict(
                        "records"
                    )
                except Exception as e:
                    Logging.error(f"Error for cluster id {cluster_id} . Error: {e}")
                    continue
            return all_content_based_rec
        except Exception as e:
            self.clear_data()
            Logging.error(
                f"Error while preparing all content based rec for {pay_tv_label}, Error: {e}"
            )

    @class_custom_exception()
    def content_based_filtering_homepage_id_data(self):
        # paytv homepage id content recommendation
        self.clear_data()
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_homepage_id_based_rec = self.cbf_homepage_id_based_rec(PAY_TV)

        # no_paytv homepage id content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_homepage_id_based_rec = self.cbf_homepage_id_based_rec(NO_PAY_TV)

        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @class_custom_exception()
    def content_based_filtering_all_content_data(self):
        # paytv all_content based content recommendation
        self.pay_tv_label = PAY_TV
        self.get_data(PAY_TV)
        pay_tv_all_content_based_rec = self.cbf_all_content_based_rec(PAY_TV)

        # no_paytv all_content_based content recommendation
        self.pay_tv_label = NO_PAY_TV
        self.get_data(NO_PAY_TV)
        no_pay_tv_all_content_based_rec = self.cbf_all_content_based_rec(NO_PAY_TV)

        self.clear_data()
        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec

    @staticmethod
    @custom_exception()
    def data_preprocessing(
        rating,
        pay_tv_label,
        ctl,
        rec_type,
    ):
        ctl.pay_tv_label = pay_tv_label
        ctl.get_data(pay_tv_label)
        pay_tv_content_label = (
            PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
        )
        content_data = ctl.content_data(
            PAY_TV_CONTENT if pay_tv_label is PAY_TV else NO_PAY_TV_CONTENT
        )
        content_data = content_data[
            content_data[CONTENT_ID].isin(ctl.content_with_homepage[CONTENT_ID])
        ]
        rating = rating[rating[CONTENT_LABEL_COLUMN] == pay_tv_content_label].copy()
        rating = rating.groupby([CONTENT_ID])[SCORE].sum().reset_index()
        rating = merge(
            rating,
            ctl.content_with_homepage[[CONTENT_ID, HOMEPAGE_ID]],
            on=CONTENT_ID,
            how="left",
        )
        rating = rating[[SCORE, CONTENT_ID, HOMEPAGE_ID]]
        remaining_id = set(ctl.content_with_homepage[CONTENT_ID]).difference(
            set(rating[CONTENT_ID])
        )
        remaining_id = ctl.content_with_homepage[
            ctl.content_with_homepage[CONTENT_ID].isin(remaining_id)
        ].copy()
        remaining_id[SCORE] = -1
        rating = concat(
            [rating, remaining_id[[SCORE, CONTENT_ID, HOMEPAGE_ID]]], axis=0
        ).reset_index(drop=True)
        rating = merge(rating, content_data, on=CONTENT_ID, how="left")
        key = (
            SERVICE_NAME
            + ":"
            + CBF_FALLBACK_MODULE_NAME.lower()
            + ":"
            + pay_tv_label
            + ":"
            + rec_type
        )
        return rating, key

    @staticmethod
    @custom_exception()
    def generate_rec(rec_type, rating, key, homepage_ids=None, is_paytv=False):
        rec = {}
        tv_channel = RecommendationUtils.get_tv_channels(is_paytv)
        scaler = MinMaxScaler(feature_range=(0, 1))
        if rec_type == ALL_CONTENT_BASED:
            rating[[CLUSTER_ID, CREATED_ON]] = nan, datetime.utcnow().isoformat()
            rating[SCORE] = (
                scaler.fit_transform(rating[[SCORE]].to_numpy()).flatten().tolist()
            )
            rating[SCORE] = 1 if rating[SCORE].max() == 0 else rating[SCORE]
            #rating[SCORE] = rating[SCORE].replace({0: -1})
            result = rating.sort_values(SCORE, ascending=False, ignore_index=True)
            result = result.drop_duplicates(subset=[CONTENT_ID])
            result[REC_TYPE] = key.split(":")[1].upper()
            result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
            result = RecommendationUtils.round_score(result)
            result = result[~result[CONTENT_ID].isin(tv_channel)]
            rec[key] = result.to_dict(RECORDS)
            return rec
        for homepage_id in homepage_ids:
            try:
                Logging.info(
                    f"CBF Fallback homepage id based:- Preparing result for & homepage id: '{homepage_id}'..."
                )
                result = rating[rating[HOMEPAGE_ID] == homepage_id].copy()
                result[[CLUSTER_ID, CREATED_ON]] = nan, datetime.utcnow().isoformat()
                if len(result) > 0:
                    result[SCORE] = (
                        scaler.fit_transform(result[[SCORE]].to_numpy())
                        .flatten()
                        .tolist()
                    )
                result[SCORE] = 1 if result[SCORE].max() == 0 else result[SCORE]
                result[SCORE] = result[SCORE].replace({0: -1})
                result = result.sort_values(
                    [SCORE, CREATED_ON], ascending=False, ignore_index=True
                )
                result[REC_TYPE] = key.split(":")[1].upper()
                result = result[[CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]]
                result = RecommendationUtils.round_score(result)
                rec[key + ":" + str(homepage_id)] = result.to_dict(RECORDS)
            except Exception as e:
                Logging.error(f"Error for homepage id {homepage_id}. Error: {e}")
                continue
        return rec

    @staticmethod
    @custom_exception()
    def fallback_homepage_id_data():

        ctl = HICRContentBasedFilteringController()
        ctl.clear_data()
        rating = ctl.implicit_rating_data_from_s3()
        rating = rating[rating[CONTENT_STATUS] == ACTIVE_LABEL]
        rating.rename(columns={IMPLICIT_RATING: SCORE}, inplace=True)

        # #fallback no_paytv homepage id content recommendation
        paytv_rating, key = ctl.data_preprocessing(
            rating.copy(), PAY_TV, ctl, HOMEPAGE_ID_BASED
        )
        pay_tv_homepage_id_based_rec = ctl.generate_rec(
            HOMEPAGE_ID_BASED, paytv_rating, key, ctl.active_homepage_id
        )

        # fallback no_paytv homepage id content recommendation
        no_paytv_rating, key = ctl.data_preprocessing(
            rating.copy(), NO_PAY_TV, ctl, HOMEPAGE_ID_BASED
        )
        no_pay_tv_homepage_id_based_rec = ctl.generate_rec(
            HOMEPAGE_ID_BASED, no_paytv_rating, key, ctl.active_homepage_id
        )
        return pay_tv_homepage_id_based_rec, no_pay_tv_homepage_id_based_rec

    @staticmethod
    @custom_exception()
    def fallback_all_content_data():

        ctl = HICRContentBasedFilteringController()
        rating = ctl.implicit_rating_data_from_s3()
        rating = rating[rating[CONTENT_STATUS] == ACTIVE_LABEL]
        rating.rename(columns={IMPLICIT_RATING: SCORE}, inplace=True)

        # fallback no_paytv homepage id content recommendation
        paytv_rating, key = ctl.data_preprocessing(
            rating.copy(), PAY_TV, ctl, ALL_CONTENT_BASED
        )
        pay_tv_all_content_based_rec = ctl.generate_rec(
            ALL_CONTENT_BASED, paytv_rating, key, is_paytv=True
        )

        # fallback no_paytv homepage id content recommendation
        no_paytv_rating, key = ctl.data_preprocessing(
            rating.copy(), NO_PAY_TV, ctl, ALL_CONTENT_BASED
        )
        no_pay_tv_all_content_based_rec = ctl.generate_rec(
            ALL_CONTENT_BASED, no_paytv_rating, key, is_paytv=False
        )

        ctl.clear_data()
        return pay_tv_all_content_based_rec, no_pay_tv_all_content_based_rec


# ctl = HICRContentBasedFilteringController()
# x,y = ctl.content_based_filtering_homepage_id_data()
# z,g = ctl.content_based_filtering_all_content_data()
# ctl = HICRContentBasedFilteringController()
# h,c = ctl.fallback_homepage_id_data()
# f,n = ctl.fallback_all_content_data()
#
# print(len(x), len(y), len(z),len(g))
# print(len(h), len(c), len(f),len(n))

# print(x,y)
# print(z,g)
