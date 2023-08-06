from datetime import datetime
from traceback import print_exc

import pandas as pd
from pandas import DataFrame

from offline_results.common.config import LEAST_VIEWED_CONTENTS_LIMIT
from offline_results.common.constants import (
    CLUSTER_ID,
    HOMEPAGE_ID,
    RECORDS,
    CREATED_ON,
    VIEW_COUNT,
    CONTENT_ID,
    ACTIVE,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    STATUS,
    INNER,
    PAY_TV,
    REC_TYPE, SCORE,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class LVUtils:
    @staticmethod
    @custom_exception()
    def get_json_format_output(df, key_prefix, homepage_id_wise):
        try:
            if homepage_id_wise:
                output_dict = {}
                unique_cluster_id = df[CLUSTER_ID].unique()
                for cluster_id in unique_cluster_id:
                    temp_output_dict = {}
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    cluster_wise_df = df.loc[df[CLUSTER_ID] == cluster_id]
                    unique_homepage_id = cluster_wise_df[HOMEPAGE_ID].unique()
                    for homepage_id in unique_homepage_id:
                        key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                        homepage_wise_df = cluster_wise_df.loc[
                            cluster_wise_df[HOMEPAGE_ID] == homepage_id
                        ]
                        homepage_wise_df = homepage_wise_df[
                            [CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
                        ]
                        temp_output_dict[key_prefix_cls_hid] = homepage_wise_df.to_dict(
                            RECORDS
                        )
                    output_dict.update(temp_output_dict)
            else:
                output_dict = {}
                unique_cluster_id = df[CLUSTER_ID].unique()
                for cluster_id in unique_cluster_id:
                    temp_output_dict = {}
                    key_prefix_cls = key_prefix + ":" + str(cluster_id)
                    output_df = df.loc[df[CLUSTER_ID] == cluster_id]
                    output_df = output_df[[CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]]
                    temp_output_dict[key_prefix_cls] = output_df.to_dict(RECORDS)
                    output_dict.update(temp_output_dict)
            return output_dict
        except Exception as e:
            Logging.error(
                f"Error while converting df to json format for{key_prefix}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_label_wise_active_contents(graph, user_label):
        try:
            content_label = (
                PAY_TV_CONTENT if user_label == PAY_TV else NO_PAY_TV_CONTENT
            )
            query = (
                f"""
                    g.V().has('{content_label}', '{STATUS}', '{ACTIVE}')"""
                + f"""
                    .valueMap("{CONTENT_ID}").by(unfold()).toList()
                    """
            )
            data = graph.custom_query(query, payload={CONTENT_ID: CONTENT_ID})
            data = [rec for idx in data for rec in idx]
            data = DataFrame(data)[[CONTENT_ID]]
            df = data.dropna(subset=[CONTENT_ID])
        except Exception:
            print_exc()
            df = []
        return df

    @staticmethod
    @custom_exception()
    def get_cluster_wise_least_viewed_contents(ubd):
        try:
            Logging.info("Finding cluster-wise least-viewed contents")
            cluster_wise_least_viewed_contents = pd.DataFrame()
            unique_cluster_id = ubd[CLUSTER_ID].unique()
            for cluster_id in unique_cluster_id:
                cluster_ubd = ubd.loc[ubd[CLUSTER_ID] == cluster_id]
                content_views_df = cluster_ubd.groupby(
                    [CONTENT_ID], as_index=False
                ).agg(view_count=(VIEW_COUNT, sum))
                content_views_df[CLUSTER_ID] = cluster_id
                content_views_df = content_views_df.sort_values(
                    [VIEW_COUNT], ascending=False
                ).reset_index(drop=True)
                content_views_df = content_views_df.tail(
                    LEAST_VIEWED_CONTENTS_LIMIT
                ).reset_index(drop=True)
                content_views_df = RecommendationUtils().get_recommendation_scores(
                    content_views_df)
                cluster_wise_least_viewed_contents = pd.concat(
                    [cluster_wise_least_viewed_contents, content_views_df], axis=0
                ).reset_index(drop=True)
            cluster_wise_least_viewed_contents = (
                cluster_wise_least_viewed_contents.sort_values(
                    [CLUSTER_ID, SCORE], ascending=(True, False)
                ).reset_index(drop=True)
            )
            return cluster_wise_least_viewed_contents
        except Exception as e:
            Logging.error(
                f"Error while Finding cluster-wise least-viewed contents, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_cluster_and_homepage_wise_least_viewed_contents(ubd):
        try:
            Logging.info("Finding cluster-and-homepage-wise least-viewed contents")
            cluster_homepage_wise_least_viewed_contents = pd.DataFrame()
            unique_cluster_id = ubd[CLUSTER_ID].unique()
            for cluster_id in unique_cluster_id:
                cluster_ubd = ubd.loc[ubd[CLUSTER_ID] == cluster_id]
                homepage_wise_least_viewed_contents = pd.DataFrame()
                unique_homepage_id = cluster_ubd[HOMEPAGE_ID].unique()
                for homepage_id in unique_homepage_id:
                    homepage_in_cluster_ubd = cluster_ubd.loc[
                        cluster_ubd[HOMEPAGE_ID] == homepage_id
                    ]
                    content_views_df = homepage_in_cluster_ubd.groupby(
                        [CONTENT_ID], as_index=False
                    ).agg(view_count=(VIEW_COUNT, sum))
                    content_views_df[HOMEPAGE_ID] = homepage_id
                    content_views_df = content_views_df.sort_values(
                        [VIEW_COUNT], ascending=False
                    ).reset_index(drop=True)
                    content_views_df = content_views_df.tail(
                        LEAST_VIEWED_CONTENTS_LIMIT
                    ).reset_index(drop=True)
                    content_views_df = RecommendationUtils().get_recommendation_scores(
                        content_views_df)
                    homepage_wise_least_viewed_contents = pd.concat(
                        [homepage_wise_least_viewed_contents, content_views_df], axis=0
                    ).reset_index(drop=True)
                homepage_wise_least_viewed_contents[CLUSTER_ID] = cluster_id
                cluster_homepage_wise_least_viewed_contents = pd.concat(
                    [
                        cluster_homepage_wise_least_viewed_contents,
                        homepage_wise_least_viewed_contents,
                    ],
                    axis=0,
                ).reset_index(drop=True)
            cluster_homepage_wise_least_viewed_contents = (
                cluster_homepage_wise_least_viewed_contents.sort_values(
                    [CLUSTER_ID, HOMEPAGE_ID, SCORE], ascending=(True, True, False)
                ).reset_index(drop=True)
            )
            return cluster_homepage_wise_least_viewed_contents
        except Exception as e:
            Logging.error(
                f"Error while Finding cluster-and-homepage-wise least viewed contents , Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def add_created_on_attribute(dataframe) -> DataFrame:
        try:
            dataframe[CREATED_ON] = datetime.utcnow().isoformat()
            return dataframe
        except Exception as e:
            Logging.error(f"Error while adding time created attribute, Error: {e}")

    @staticmethod
    @custom_exception()
    def add_recommendation_type_attribute(dataframe, rec_type) -> DataFrame:
        try:
            dataframe[REC_TYPE] = rec_type
            return dataframe
        except Exception as e:
            Logging.error(
                f"Error while adding recommendation type attribute, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_inner_merged_df(data1, data2, on):
        try:
            df = pd.merge(data1, data2, on=on, how=INNER)
            return df
        except Exception as e:
            Logging.error(f"Error while merging on {on}, Error: {e}")

    @staticmethod
    @custom_exception()
    def get_default_least_viewed_contents(ubd):
        try:
            Logging.info("Finding least-viewed contents")
            content_views_df = ubd.groupby([CONTENT_ID], as_index=False).agg(
                view_count=(VIEW_COUNT, sum)
            )
            least_viewed_contents = content_views_df.sort_values(
                [VIEW_COUNT], ascending=False
            ).reset_index(drop=True)
            least_viewed_contents = least_viewed_contents.tail(
                LEAST_VIEWED_CONTENTS_LIMIT
            ).reset_index(drop=True)
            least_viewed_contents = RecommendationUtils().get_recommendation_scores(
                least_viewed_contents)
            return least_viewed_contents
        except Exception as e:
            Logging.error(
                f"Error while Finding FALLBACK least-viewed contents, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_default_homepage_wise_least_viewed_contents(ubd):
        try:
            Logging.info("Finding homepage-wise least-viewed contents")
            homepage_wise_least_viewed_contents = pd.DataFrame()
            unique_homepage_id = ubd[HOMEPAGE_ID].unique()
            for homepage_id in unique_homepage_id:
                homepage_ubd = ubd.loc[ubd[HOMEPAGE_ID] == homepage_id]
                content_views_df = homepage_ubd.groupby(
                    [CONTENT_ID], as_index=False
                ).agg(view_count=(VIEW_COUNT, sum))
                content_views_df[HOMEPAGE_ID] = homepage_id
                content_views_df = content_views_df.sort_values(
                    [VIEW_COUNT], ascending=False
                ).reset_index(drop=True)
                content_views_df = content_views_df.tail(
                    LEAST_VIEWED_CONTENTS_LIMIT
                ).reset_index(drop=True)
                content_views_df = RecommendationUtils().get_recommendation_scores(
                    content_views_df)
                homepage_wise_least_viewed_contents = pd.concat(
                    [homepage_wise_least_viewed_contents, content_views_df], axis=0
                ).reset_index(drop=True)

            homepage_wise_least_viewed_contents = (
                homepage_wise_least_viewed_contents.sort_values(
                    [HOMEPAGE_ID, SCORE], ascending=(True, False)
                ).reset_index(drop=True)
            )
            return homepage_wise_least_viewed_contents
        except Exception as e:
            Logging.error(
                f"Error while Finding FALLBACK least-viewed contents , Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_default_json_format_output(df, key_prefix, homepage_id_wise):
        try:
            if homepage_id_wise:
                output_dict = {}
                unique_homepage_id = df[HOMEPAGE_ID].unique()
                key_prefix_cls = key_prefix
                for homepage_id in unique_homepage_id:
                    key_prefix_cls_hid = key_prefix_cls + ":" + str(homepage_id)
                    homepage_wise_df = df.loc[df[HOMEPAGE_ID] == homepage_id]
                    homepage_wise_df = homepage_wise_df[
                        [CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]
                    ]
                    output_dict[key_prefix_cls_hid] = homepage_wise_df.to_dict(RECORDS)
                    output_dict.update(output_dict)
            else:
                key_prefix_cls = key_prefix
                df = df[[CONTENT_ID, CREATED_ON, REC_TYPE, SCORE]]
                output_dict = {key_prefix_cls: df.to_dict(RECORDS)}
                output_dict.update(output_dict)
            return output_dict
        except Exception as e:
            Logging.error(
                f"Error while converting df to json format for{key_prefix}, Error: {e}"
            )
