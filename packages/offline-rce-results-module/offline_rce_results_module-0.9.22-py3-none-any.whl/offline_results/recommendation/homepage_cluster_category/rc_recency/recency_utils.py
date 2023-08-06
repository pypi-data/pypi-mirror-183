from datetime import datetime

import pandas as pd
from pandas import DataFrame

from offline_results.common.constants import (
    INNER,
    CREATED_ON,
    HOMEPAGE_ID,
    CLUSTER_ID,
    RECORDS,
    REC_TYPE, SCORE,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class RecencyUtils:
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
                f"Error while converting df to json format for{key_prefix}, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_cluster_wise_homepage_id_not_in_ubd(
        active_static_homepage_data, cluster_homepage_mapped_user_content_df
    ):
        try:
            Logging.info("Finding cluster-wise homepage_ids not in log")
            active_homepage_df = set(active_static_homepage_data[HOMEPAGE_ID].unique())
            cluster_wise_homepage_id_not_in_ubd = pd.DataFrame()
            unique_cluster_id = cluster_homepage_mapped_user_content_df[
                CLUSTER_ID
            ].unique()
            for cluster_id in unique_cluster_id:
                ubd = cluster_homepage_mapped_user_content_df.loc[
                    cluster_homepage_mapped_user_content_df[CLUSTER_ID] == cluster_id
                ]
                unique_ubd_homepage = set(ubd[HOMEPAGE_ID].unique())
                homepage_id_not_in_ubd_list = list(
                    active_homepage_df.difference(unique_ubd_homepage)
                )
                homepage_id_not_in_ubd_dict = {
                    CLUSTER_ID: cluster_id,
                    HOMEPAGE_ID: homepage_id_not_in_ubd_list,
                }
                homepage_id_not_in_ubd_df = pd.DataFrame(homepage_id_not_in_ubd_dict)
                homepage_id_not_in_ubd_df = RecencyUtils.get_inner_merged_df(
                    homepage_id_not_in_ubd_df, active_static_homepage_data,
                    on=HOMEPAGE_ID,
                )
                homepage_id_not_in_ubd_df = homepage_id_not_in_ubd_df.sort_values(
                    by=[CREATED_ON], ascending=False).reset_index(drop=True)
                homepage_id_not_in_ubd_df = RecommendationUtils().get_recommendation_scores(
                    homepage_id_not_in_ubd_df)
                cluster_wise_homepage_id_not_in_ubd = pd.concat(
                    [cluster_wise_homepage_id_not_in_ubd, homepage_id_not_in_ubd_df],
                    axis=0,
                ).reset_index(drop=True)
            return cluster_wise_homepage_id_not_in_ubd
        except Exception as e:
            Logging.error(
                f"Error while Finding cluster-wise homepage_ids not in log, Error: {e}"
            )

    @staticmethod
    @custom_exception()
    def get_default_homepage_id_not_in_ubd(active_static_homepage_data, ubd):
        try:
            Logging.info("Finding homepage_ids not in log")
            active_homepage_df = set(active_static_homepage_data[HOMEPAGE_ID].unique())
            unique_ubd_homepage = set(ubd[HOMEPAGE_ID].unique())
            homepage_id_not_in_ubd_list = list(
                active_homepage_df.difference(unique_ubd_homepage)
            )
            homepage_id_not_in_ubd_dict = {HOMEPAGE_ID: homepage_id_not_in_ubd_list}
            homepage_id_not_in_ubd_df = pd.DataFrame(homepage_id_not_in_ubd_dict)
            homepage_id_not_in_ubd_df = RecencyUtils.get_inner_merged_df(
                homepage_id_not_in_ubd_df, active_static_homepage_data, on=HOMEPAGE_ID
            )
            homepage_id_not_in_ubd_df = homepage_id_not_in_ubd_df.sort_values \
                (by=[CREATED_ON], ascending=False) \
                .reset_index(drop=True)
            homepage_id_not_in_ubd_df = RecommendationUtils().get_recommendation_scores(
                homepage_id_not_in_ubd_df)
            return homepage_id_not_in_ubd_df
        except Exception as e:
            Logging.error(f"Error while Finding homepage_ids not in log, Error: {e}")

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
