from datetime import datetime

import pandas as pd
from pandas import DataFrame

from offline_results.common.config import TOP_VIEWED_HOMEPAGES_LIMIT
from offline_results.common.constants import (
    HOMEPAGE_ID,
    CREATED_ON,
    VIEW_COUNT,
    INNER,
    RECORDS,
    REC_TYPE,
    CLUSTER_ID, SCORE,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class TopViewedUtils:
    @staticmethod
    @custom_exception()
    def get_cluster_wise_top_viewed_homepages(ubd):
        try:
            Logging.info("Finding cluster-wise top-viewed homepages")
            cluster_wise_top_viewed_homepages = pd.DataFrame()
            unique_cluster_id = ubd[CLUSTER_ID].unique()
            for cluster_id in unique_cluster_id:
                cluster_ubd = ubd.loc[ubd[CLUSTER_ID] == cluster_id]
                homepage_views_df = cluster_ubd.groupby(
                    [HOMEPAGE_ID], as_index=False
                ).agg(view_count=(VIEW_COUNT, sum))
                homepage_views_df[CLUSTER_ID] = cluster_id
                homepage_views_df = homepage_views_df.sort_values(
                    [VIEW_COUNT], ascending=False
                ).reset_index(drop=True)
                homepage_views_df = homepage_views_df.head(
                    TOP_VIEWED_HOMEPAGES_LIMIT
                ).reset_index(drop=True)
                homepage_views_df = RecommendationUtils().get_recommendation_scores(
                    homepage_views_df)
                cluster_wise_top_viewed_homepages = pd.concat(
                    [cluster_wise_top_viewed_homepages, homepage_views_df], axis=0
                ).reset_index(drop=True)
            cluster_wise_top_viewed_homepages = (
                cluster_wise_top_viewed_homepages.sort_values(
                    [CLUSTER_ID, SCORE], ascending=(True, False)
                ).reset_index(drop=True)
            )
            return cluster_wise_top_viewed_homepages
        except Exception as e:
            Logging.error(
                f"Error while Finding cluster-wise top-viewed homepages, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_default_top_viewed_homepages(ubd):
        try:
            Logging.info("Finding FALLBACK top-viewed homepages")
            homepage_views_df = ubd.groupby(
                [HOMEPAGE_ID], as_index=False
            ).agg(view_count=(VIEW_COUNT, sum))

            top_viewed_homepages = homepage_views_df.sort_values(
                [VIEW_COUNT], ascending=False
            ).reset_index(drop=True)
            top_viewed_homepages = top_viewed_homepages.head(
                TOP_VIEWED_HOMEPAGES_LIMIT
            ).reset_index(drop=True)
            top_viewed_homepages = RecommendationUtils().get_recommendation_scores(
                top_viewed_homepages)
            return top_viewed_homepages
        except Exception as e:
            Logging.error(
                f"Error while Finding FALLBACK top-viewed homepages, Error: {e}"
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
    def get_json_format_output(df, key_prefix):
        try:
            output_dict = {}
            unique_cluster_id = df[CLUSTER_ID].unique()
            for cluster_id in unique_cluster_id:
                temp_output_dict = {}
                key_prefix_cls = key_prefix + ":" + str(cluster_id)
                output_df = df.loc[df[CLUSTER_ID] == cluster_id]
                output_df = output_df[[HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE]]
                temp_output_dict[key_prefix_cls] = output_df.to_dict(RECORDS)
                output_dict.update(temp_output_dict)
            return output_dict
        except Exception as e:
            Logging.error(
                f"Error while converting df to json format for {key_prefix}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_default_json_format_output(df, key_prefix):
        try:
            output_dict = {}
            key_prefix_cls = key_prefix
            df = df[[HOMEPAGE_ID, CREATED_ON, REC_TYPE, SCORE]]
            output_dict[key_prefix_cls] = df.to_dict(RECORDS)
            return output_dict
        except Exception as e:
            Logging.error(
                f"Error while converting df to json format for{key_prefix}, Error: {e}"
            )
