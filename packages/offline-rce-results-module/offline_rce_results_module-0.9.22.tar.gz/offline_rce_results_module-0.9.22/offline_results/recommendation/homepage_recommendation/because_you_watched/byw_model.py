import time
from datetime import datetime
from functools import reduce

import numpy as np
import pandas as pd
from pandas import DataFrame

from offline_results.common.constants import (
    SCORE,
    CREATED_ON,
    CLUSTER_ID,
    LEFT,
    CONTENT_ID,
    HOMEPAGE_ID,
    RECORDS,
    SERVICE_NAME,
    BYW_MODULE_NAME,
    HOMEPAGE_ID_BASED,
    ALL_CONTENT_BASED,
    PAY_TV,
    NO_PAY_TV,
    REC_TYPE,
    BECAUSE_YOU_WATCHED,
)
from offline_results.recommendation.homepage_recommendation.because_you_watched.prepare_byw_data import (
    BYWData,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import custom_exception, Logging


class BYWModel:
    viewed_relation_history_df = DataFrame()
    user_cluster_mapping = DataFrame()
    content_similarity_no_paytv = DataFrame()
    content_similarity_paytv = DataFrame()

    @staticmethod
    @custom_exception()
    def get_data():
        obj = BYWModel
        if len(obj.viewed_relation_history_df) != 0:
            return
        obj.viewed_relation_history_df = RecommendationUtils.user_viewed_data_from_s3()
        obj.user_cluster_mapping = RecommendationUtils.user_cluster_from_s3()
        obj.content_similarity_paytv = (
            BYWData.get_content_similarity_based_on_all_content(user_label=PAY_TV)
        )
        obj.content_similarity_no_paytv = (
            BYWData.get_content_similarity_based_on_all_content(user_label=NO_PAY_TV)
        )

    @staticmethod
    @custom_exception()
    def clear_data():
        obj = BYWModel
        obj.viewed_relation_history_df = DataFrame()
        obj.user_cluster_mapping = DataFrame()
        obj.content_similarity_no_paytv = DataFrame()
        obj.content_similarity_paytv = DataFrame()

    @staticmethod
    @custom_exception()
    def get_dict_format_output(df, key_prefix, homepage_id_wise):
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
                        [CLUSTER_ID, CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]
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
                output_df = output_df[
                    [CLUSTER_ID, CONTENT_ID, HOMEPAGE_ID, SCORE, CREATED_ON, REC_TYPE]
                ]
                temp_output_dict[key_prefix_cls] = output_df.to_dict(RECORDS)
                output_dict.update(temp_output_dict)
        return output_dict

    @staticmethod
    @custom_exception()
    def byw_algorithm(graph, user_label, homepage_id_wise):
        cluster_content_data, content_homepage_mapping = BYWData.get_viewed_content(
            graph,
            user_label,
            homepage_id_wise,
            BYWModel.viewed_relation_history_df,
            BYWModel.user_cluster_mapping,
        )
        if len(cluster_content_data.index) == 0:
            Logging.info("There is no UBD Data from dedicated BYW Homepage_id")
            Logging.info("There is no content which will be recommended to the user")
            return cluster_content_data

        content_similarity_data = (
            BYWModel.content_similarity_paytv
            if user_label == PAY_TV
            else BYWModel.content_similarity_no_paytv
        )
        Logging.info("Calculating BYW Recommendation Score")
        all_recommendation_dict = {}
        all_recommendation_dict_score = {}
        for idx, data_property in cluster_content_data.iterrows():
            list_content_id = data_property.content_id
            cluster_id = data_property.cluster_id
            if len(list_content_id) == 1:
                # USE-CASE CONDITION : Recommending the content if customer only watched 1 content

                # Iterate through all content_id which watched by user
                for id_content in list_content_id:
                    # Iterate through all content similarity data
                    for (
                        key_content_id,
                        similarity_data,
                    ) in content_similarity_data.items():
                        # If the content which watched by user is available on the content_similarity_data
                        if id_content == key_content_id:
                            # Take the first 10 most similar content from similarity_data
                            list_recommended_content_id = []
                            list_recommended_content_id_score = []
                            for (
                                recommended_content_id,
                                sim_score,
                            ) in similarity_data.items():
                                list_recommended_content_id.append(
                                    recommended_content_id
                                )
                                list_recommended_content_id_score.append(
                                    round(sim_score, 3)
                                )
                                if len(list_recommended_content_id) == 10:
                                    break
                            # Create dictionary of user-recommended content
                            all_recommendation_dict[
                                cluster_id
                            ] = list_recommended_content_id
                            all_recommendation_dict_score[
                                cluster_id
                            ] = list_recommended_content_id_score
                            break
            elif len(list_content_id) > 1:
                # USE-CASE CONDITION : Recommending the content if customer watched multiple content

                list_df_recommendation = []
                # Iterate through all content_id which watched by user
                id_content_position = idx + 1
                for id_content in list_content_id:
                    # Iterate through all content similarity data
                    for (
                        key_content_id,
                        similarity_data,
                    ) in content_similarity_data.items():
                        # If the content which watched by user is available on the content_similarity_data
                        if id_content == key_content_id:
                            list_recommended_content_id = []
                            # Take the first 10 most similar content from similarity_data
                            for (
                                recommended_content_id,
                                sim_score,
                            ) in similarity_data.items():
                                list_recommended_content_id.append(
                                    recommended_content_id
                                )
                                # When length of the list already has 10 content_id data
                                if len(list_recommended_content_id) == 10:
                                    # Give the point recommendation_score to all recommended content_id
                                    # The most similar content_id will give 10 points divided by id_content_position
                                    # The Most Similar Content Point = (10/id_content_position)

                                    # Until the least similar content_id will give 1 point divided by id_content_position
                                    # The Least Similar Content Point = (10/id_content_position)

                                    dict_recommendation = dict(
                                        zip(
                                            list_recommended_content_id,
                                            np.arange(
                                                10 / id_content_position,
                                                0 / id_content_position,
                                                -1 / id_content_position,
                                            ),
                                        )
                                    )

                                    # convert to dataframe and sort by recommendation score in descending
                                    df_temp = pd.DataFrame(
                                        {SCORE: dict_recommendation}
                                    ).sort_values(by=SCORE, ascending=False)
                                    # append df_temp recommendation from current content_id to the list_df_recommendation
                                    list_df_recommendation.append(df_temp)
                                    id_content_position += 1
                                    break
                # After having multiple df_recommendation, we sum all recommendation_score points based on content_id
                final_df = reduce(
                    lambda df_source, df_target: df_source.add(df_target, fill_value=0),
                    list_df_recommendation,
                )
                # After do summation from all dataframe, we remove content_id which already watched by user from
                # recommendation content dataframe
                for content_id in list_content_id:
                    if content_id in final_df.index.values.tolist():
                        final_df = final_df.drop(content_id)

                # Sort the recommendation content based on recommendation_score in descending method
                # and take the first 10 content with the highest score
                final_df = final_df.sort_values(by=SCORE, ascending=False)
                # Take the content_id from the index and transform it to the list
                final_recommended_content_id = final_df.index.values.tolist()
                final_recommended_content_id_score = final_df[SCORE].tolist()
                # Create dictionary of user-recommended content
                all_recommendation_dict[cluster_id] = final_recommended_content_id
                all_recommendation_dict_score[
                    cluster_id
                ] = final_recommended_content_id_score

        Logging.info("Preparing BYW Recommendation Content Output")
        # This step is to create output as dataframe
        # which contain customer_id, recommended_content_id, and rc_created_on
        all_recommendation_dict_df = pd.DataFrame(
            [all_recommendation_dict]
        ).T.reset_index(level=0)
        all_recommendation_dict_score_df = pd.DataFrame(
            [all_recommendation_dict_score]
        ).T.reset_index(level=0)
        all_recommendation_dict_df.columns = [CLUSTER_ID, CONTENT_ID]
        all_recommendation_dict_score_df.columns = [CLUSTER_ID, SCORE]
        all_recommendation_dict_df = pd.merge(
            all_recommendation_dict_df,
            all_recommendation_dict_score_df,
            on=CLUSTER_ID,
            how=LEFT,
        )
        all_recommendation_dict_df[REC_TYPE] = BECAUSE_YOU_WATCHED
        all_recommendation_dict_df[CREATED_ON] = datetime.utcnow().isoformat()
        all_recommendation_dict_df[CLUSTER_ID] = all_recommendation_dict_df[
            CLUSTER_ID
        ].apply(str)
        all_recommendation_dict_df = all_recommendation_dict_df.explode(
            [CONTENT_ID, SCORE]
        )
        all_recommendation_dict_df[SCORE] = all_recommendation_dict_df[SCORE].apply(
            lambda x: round(x, 3)
        )
        if homepage_id_wise:
            all_recommendation_dict_df = pd.merge(
                all_recommendation_dict_df,
                content_homepage_mapping,
                on=CONTENT_ID,
                how=LEFT,
            )
            all_recommendation_dict_df = all_recommendation_dict_df[
                ~all_recommendation_dict_df[HOMEPAGE_ID].isnull()
            ].reset_index(drop=True)
            all_recommendation_dict_df = all_recommendation_dict_df.explode(
                column=HOMEPAGE_ID
            )
            # all_recommendation_dict_df = BYWData.filter_by_dedicated_homepage_id(all_recommendation_dict_df, user_label,
            #                                                                      filter_on_ubd=False)
            all_recommendation_dict_df = all_recommendation_dict_df.sort_values(
                by=[CLUSTER_ID, HOMEPAGE_ID, SCORE], ascending=[True, True, False]
            )
        else:
            all_recommendation_dict_df = pd.merge(
                all_recommendation_dict_df,
                content_homepage_mapping,
                on=CONTENT_ID,
                how=LEFT,
            )
            all_recommendation_dict_df = all_recommendation_dict_df[
                ~all_recommendation_dict_df[HOMEPAGE_ID].isnull()
            ].reset_index(drop=True)
            all_recommendation_dict_df = all_recommendation_dict_df.explode(
                column=HOMEPAGE_ID
            )
            # all_recommendation_dict_df = BYWData.filter_by_dedicated_homepage_id(all_recommendation_dict_df, user_label,
            #                                                                      filter_on_ubd=False)
            all_recommendation_dict_df = all_recommendation_dict_df.sort_values(
                by=[CLUSTER_ID, SCORE], ascending=[True, False]
            )

        return all_recommendation_dict_df

    @staticmethod
    @custom_exception()
    def get_byw_content_all_content(graph):

        BYWModel.get_data()
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        empty_df = DataFrame()
        Logging.info("Generating BYW Content based on All Content")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Generating BYW Content All Content wise for " + user_label + " users"
            )
            output_df = BYWModel.byw_algorithm(graph, user_label, homepage_id_wise)
            if len(output_df.index) == 0:
                Logging.info(
                    "Failed to generate BYW Content All Content Wise for "
                    + user_label
                    + " users"
                )
                continue
            key_prefix = (
                SERVICE_NAME
                + ":"
                + BYW_MODULE_NAME
                + ":"
                + user_label
                + ":"
                + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        if len(list_output_df) == 0:
            return empty_df, empty_df
        byw_pay_tv_all_content, byw_no_pay_tv_all_content = list_output_df
        Logging.info("Converting BYW Recommendation Content Output to JSON Schema")
        byw_pay_tv_all_content_dict = BYWModel.get_dict_format_output(
            byw_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
        )
        byw_no_pay_tv_all_content_dict = BYWModel.get_dict_format_output(
            byw_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
        )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for generating BYW content All Content wise : " + str(duration)
        )
        BYWModel.clear_data()
        return byw_pay_tv_all_content_dict, byw_no_pay_tv_all_content_dict

    @staticmethod
    @custom_exception()
    def get_byw_content_homepage_id(graph):

        BYWModel.clear_data()
        BYWModel.get_data()
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        empty_df = DataFrame()
        Logging.info("Generating BYW Content based on Homepage_id")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Generating BYW Content Homepage_id wise for " + user_label + " users"
            )
            output_df = BYWModel.byw_algorithm(graph, user_label, homepage_id_wise)
            if len(output_df.index) == 0:
                Logging.info(
                    "Failed to generate BYW Content Homepage_id Wise for "
                    + user_label
                    + " users"
                )
                continue
            key_prefix = (
                SERVICE_NAME
                + ":"
                + BYW_MODULE_NAME
                + ":"
                + user_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        if len(list_output_df) == 0:
            return empty_df, empty_df
        byw_pay_tv_homepage_id, byw_no_pay_tv_homepage_id = list_output_df

        byw_pay_tv_homepage_id_dict = BYWModel.get_dict_format_output(
            byw_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
        )
        byw_no_pay_tv_homepage_id_dict = BYWModel.get_dict_format_output(
            byw_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
        )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for generating BYW content Homepage_id wise : " + str(duration)
        )
        return byw_pay_tv_homepage_id_dict, byw_no_pay_tv_homepage_id_dict
