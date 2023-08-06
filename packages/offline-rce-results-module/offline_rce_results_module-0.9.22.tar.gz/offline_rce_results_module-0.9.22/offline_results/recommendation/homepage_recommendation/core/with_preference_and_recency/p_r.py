from pandas import merge, concat, DataFrame
from functools import reduce

from pandas import merge, concat, DataFrame
from sklearn.preprocessing import MinMaxScaler

from offline_results.common.config import (
    ENCODING_MODEL,
    VISIONPLUS_DEV,
    NO_PAY_TV_CLUSTER_CENTROID,
    PAY_TV_CLUSTER_CENTROID,
)
from offline_results.common.constants import (
    NO_PAY_TV_CONTENT,
    PAY_TV_CONTENT,
    CONTENT_ID,
    ACTOR,
    ACTOR_ID,
    HAS_ACTOR,
    HAS_TAG,
    SUBCATEGORY,
    HAS_SUBCATEGORY,
    TAGS,
    SUBCATEGORY_ID,
    TAGS_ID,
    ACTORS,
    MINIBATCH_KMEANS,
    IS_PAYTV,
    HOMEPAGE_ID,
    SCORE,
    CREATED_ON,
    DEFAULT_CLUSTER_ID,
    CLUSTER_ID,
    FIRST_QUANTILE,
    THIRD_QUANTILE,
    SCORE_ROUNDOFF,
    IS_PAY_TV,
    CUSTOMER_ID,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.recommendation.homepage_cluster_category.hompage_id_recommendation import (
    HomepageIdRecommendation,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.updater.utils import UpdaterUtils
from offline_results.utils import class_custom_exception, Logging


class UserPrefBasedRecommendation(
    HomepageIdRecommendation,
    RecommendationUtils,
    UpdaterUtils,
):
    @class_custom_exception()
    def get_content_properties(self, is_paytv, no_ubd=True):

        try:
            content_tag_property = self.content_property(
                is_paytv, HAS_TAG, TAGS, TAGS_ID
            )
            content_actor_property = self.content_property(
                is_paytv, HAS_ACTOR, ACTOR, ACTOR_ID
            )
            content_subcategory_property = self.content_property(
                is_paytv, HAS_SUBCATEGORY, SUBCATEGORY, SUBCATEGORY_ID
            )
            content_tag_property = (
                content_tag_property.groupby(CONTENT_ID)[TAGS_ID]
                .apply(list)
                .reset_index(name=TAGS_ID)
            )
            content_actor_property = (
                content_actor_property.groupby(CONTENT_ID)[ACTOR_ID]
                .apply(list)
                .reset_index(name=ACTOR_ID)
            )
            content_subcategory_property = (
                content_subcategory_property.groupby(CONTENT_ID)[SUBCATEGORY_ID]
                .apply(list)
                .reset_index(name=SUBCATEGORY_ID)
            )
            pref_list = [
                content_tag_property,
                content_subcategory_property,
                content_actor_property,
            ]
            self.content_properties = reduce(
                lambda left, right: merge(left, right, on=CONTENT_ID), pref_list
            )
            content_label = PAY_TV_CONTENT if is_paytv else NO_PAY_TV_CONTENT
            content = (
                self.get_content_data(content_label)
                if no_ubd
                else self.content_data(content_label)
            )
            if no_ubd:
                all_content = self.active_contents(is_paytv)
                content_with_no_homepage = all_content[
                    ~all_content[CONTENT_ID].isin(content[CONTENT_ID])
                ]
                content_with_no_homepage.insert(0, column=HOMEPAGE_ID, value=-1)
                content = concat([content, content_with_no_homepage], ignore_index=True)
                self.process_s3_data(is_paytv)
            self.content_properties = merge(
                content, self.content_properties, on=CONTENT_ID, how="left"
            )
            self.content_properties = self.content_properties.dropna().reset_index(
                drop=True
            )

            return self.content_properties

        except Exception as e:
            Logging.error(f"Error while get content properties, Error: {e}")

    @class_custom_exception()
    def process_s3_data(self, is_pay_tv=False):
        user_cluster = self.user_cluster_from_s3()
        user_cluster = user_cluster[user_cluster[IS_PAY_TV] == is_pay_tv]
        view_data = self.user_viewed_data_from_s3()
        view_data = view_data[view_data[IS_PAY_TV] == is_pay_tv]
        self.view_data = merge(view_data, user_cluster, on=CUSTOMER_ID, how="left")
        self.view_data = self.view_data.dropna(subset=[CLUSTER_ID])
        self.view_data[CLUSTER_ID] = self.view_data[CLUSTER_ID].apply(int)

    @class_custom_exception()
    def get_cluster_pref_from_s3(self):
        ctl = ConnectS3()
        resource = ctl.create_connection()
        paytv_cluster = ctl.read_csv_from_s3(
            bucket_name=VISIONPLUS_DEV,
            object_name=PAY_TV_CLUSTER_CENTROID,
            resource=resource,
        )
        no_paytv_cluster = ctl.read_csv_from_s3(
            bucket_name=VISIONPLUS_DEV,
            object_name=NO_PAY_TV_CLUSTER_CENTROID,
            resource=resource,
        )
        self.cluster_pref = concat(
            [paytv_cluster, no_paytv_cluster], axis=0, ignore_index=True
        )

    @class_custom_exception()
    def cluster_preferences(
        self,
    ):
        try:
            self.cluster_pref = self.fetch_centroids()
            if len(self.cluster_pref) == 0:
                self.get_cluster_pref_from_s3()
            self.cluster_pref[IS_PAYTV].replace(
                {"True": True, "False": False}, inplace=True
            )
            self.cluster_pref = self.cluster_pref[
                [MINIBATCH_KMEANS, TAGS, SUBCATEGORY, ACTORS, IS_PAYTV]
            ]
            self.cluster_pref[TAGS] = self.cluster_pref[TAGS].apply(
                lambda x: [int(rec.split("_")[1]) for rec in x.split(",")]
            )
            self.cluster_pref[SUBCATEGORY] = self.cluster_pref[SUBCATEGORY].apply(
                lambda x: [int(rec.split("_")[1]) for rec in x.split(",")]
            )
            self.cluster_pref[ACTORS] = self.cluster_pref[ACTORS].apply(
                lambda x: [int(rec.split("_")[1]) for rec in x.split(",")]
            )
            return self.cluster_pref

        except Exception as e:
            Logging.error(f"Error while getting user preferences, Error: {e}")

    @class_custom_exception()
    def data_gathering(self, is_paytv, no_ubd=True):
        self.cluster_pref = self.cluster_preferences()
        self.content_properties = self.get_content_properties(is_paytv, no_ubd)
        self.content_properties.rename(
            columns={TAGS_ID: TAGS, SUBCATEGORY_ID: SUBCATEGORY, ACTOR_ID: ACTORS},
            inplace=True,
        )
        self.encoding_model = self.load_model_from_s3(is_paytv, ENCODING_MODEL)
        self.encoding_model[ACTORS] = set(self.all_actor_ids())

    @class_custom_exception()
    def data_preprocessing(self):
        for col in self.cluster_pref.columns:
            if col not in [ACTORS, SUBCATEGORY, TAGS]:
                continue
            self.cluster_pref = self.encode_df(
                self.cluster_pref, col, self.encoding_model[col]
            )
            self.cluster_pref = RecommendationUtils.expand_features(
                self.cluster_pref, col
            )

        for col in self.content_properties.columns:
            if col not in [ACTORS, SUBCATEGORY, TAGS]:
                continue
            self.content_properties = self.encode_df(
                self.content_properties, col, self.encoding_model[col]
            )
            self.content_properties = RecommendationUtils.expand_features(
                self.content_properties, col
            )

        self.features = list(
            self.cluster_pref.head(1).drop(columns=[MINIBATCH_KMEANS, IS_PAYTV]).columns
        )
        return self.cluster_pref, self.content_properties

    @class_custom_exception()
    def scale_and_sort(self, df):
        scaler = MinMaxScaler(
            feature_range=(float("0." + "0" * (SCORE_ROUNDOFF - 1) + "1"), 1)
        )
        df[SCORE] = scaler.fit_transform(df[[SCORE]].to_numpy()).flatten().tolist()
        df[SCORE] = 1 if df[SCORE].max() == float("0." + "0" * (SCORE_ROUNDOFF - 1) + "1") else df[SCORE]
        df = df.sort_values([SCORE, CREATED_ON], ascending=False, ignore_index=True)
        df[SCORE] = round(df[SCORE], SCORE_ROUNDOFF)
        return df[[CONTENT_ID, SCORE]]

    @class_custom_exception()
    def compute_score(self, homepage_id_content, cluster_id_pref):

        cluster_feature = DataFrame(cluster_id_pref).T.reset_index()[self.features].T[0]
        homepage_id_content[SCORE] = homepage_id_content.apply(
            lambda x: self.calculate_euclidean_dist(x[self.features], cluster_feature),
            axis=1,
        )
        result = homepage_id_content[[CONTENT_ID, CREATED_ON, SCORE]].copy()
        result[SCORE] = result[SCORE].max() - result[SCORE]
        result = self.scale_and_sort(result.copy())
        return result

    @class_custom_exception()
    def common_pref(self, df, content, is_paytv):
        try:
            df = df[df[IS_PAYTV] == is_paytv].copy()
            pref = df.head(1).reset_index(drop=True)
            features = [ACTORS, SUBCATEGORY, TAGS]
            for feature in features:
                col = [col for col in df if col.startswith(feature)]
                pref.loc[0, col] = 0
                temp = df[col].sum()
                feature_range = temp[temp > 0].quantile(
                    [FIRST_QUANTILE, THIRD_QUANTILE]
                )
                temp = list(
                    temp[
                        (temp > feature_range[FIRST_QUANTILE])
                        & (temp < feature_range[THIRD_QUANTILE])
                    ].index
                )
                pref.loc[0, temp] = 1
            pref = pref.loc[0, pref.columns.difference([MINIBATCH_KMEANS, IS_PAYTV])]
            result = self.compute_score(content, pref)
            return result

        except Exception as e:
            Logging.error(f"Error while creating common preference, Error: {e}")

    @class_custom_exception()
    def prepare_default_result(self, homepage_id_content):
        homepage_id_content = homepage_id_content[
            ~homepage_id_content[CONTENT_ID].isin(set(self.view_data[CONTENT_ID]))
        ]
        homepage_id_content = homepage_id_content.sort_values(
            [CREATED_ON], ascending=False
        ).reset_index(drop=True)
        homepage_id_content[SCORE] = [idx+1 for idx in range(len(homepage_id_content))][::-1]
        homepage_id_content[SCORE] = (
            homepage_id_content[SCORE] / homepage_id_content[SCORE].max()
        )
        homepage_id_content[SCORE] = round(homepage_id_content[SCORE], SCORE_ROUNDOFF)
        return homepage_id_content[[CONTENT_ID, SCORE]]

    @class_custom_exception()
    def return_cluster_wise_result(self, homepage_id_content, cluster_id, is_paytv):
        viewed = self.view_data[self.view_data[CLUSTER_ID] == cluster_id]
        homepage_id_content = homepage_id_content[
            ~homepage_id_content[CONTENT_ID].isin(set(viewed[CONTENT_ID]))
        ]
        homepage_id_content = homepage_id_content.drop_duplicates(subset=[CONTENT_ID])
        if len(homepage_id_content) == 0:
            return DataFrame(columns=[CONTENT_ID, SCORE])
        cluster_id_pref = self.cluster_pref[self.cluster_pref[IS_PAYTV] == is_paytv]
        cluster_id_pref = cluster_id_pref[
            cluster_id_pref[MINIBATCH_KMEANS] == cluster_id
        ]
        cluster_id_pref = cluster_id_pref.loc[
            cluster_id_pref.index[0],
            cluster_id_pref.columns.difference([MINIBATCH_KMEANS, IS_PAYTV]),
        ]
        result = self.compute_score(homepage_id_content.copy(), cluster_id_pref.copy())
        return result

    @class_custom_exception()
    def generate_recommendation(self, is_paytv, cluster_id=None, homepage_id=None):

        homepage_id_content = self.content_properties.copy()
        if homepage_id is not None:
            homepage_id_content = self.content_properties[
                self.content_properties[HOMEPAGE_ID] == homepage_id
            ].copy()
            homepage_id_content[SCORE] = -1
        if len(homepage_id_content) == 0:
            return DataFrame(columns=[CONTENT_ID, SCORE])
        if cluster_id is None:
            return self.common_pref(
                self.cluster_pref, homepage_id_content.copy(), is_paytv
            )
        if cluster_id is DEFAULT_CLUSTER_ID:
            return self.prepare_default_result(homepage_id_content)
        return self.return_cluster_wise_result(
            homepage_id_content, cluster_id, is_paytv
        )


#
# if __name__ == "__main__":
#     ctl = UserPrefBasedRecommendation()
#     ctl.data_gathering(True)
#     ctl.data_preprocessing()
#     ctl.generate_recommendation()
