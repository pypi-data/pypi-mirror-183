import ast
import time
from datetime import datetime

from pandas import DataFrame, merge, to_datetime

from offline_results.common.config import (
    CONFIG_HOMEPAGE_PAYTV,
    CONFIG_HOMEPAGE_NO_PAYTV,
)
from offline_results.common.constants import (
    PAY_TV,
    NO_PAY_TV,
    SERVICE_NAME,
    ALL_CONTENT_BASED,
    HOMEPAGE_ID,
    CONTENT_ID,
    SCORE,
    CREATED_ON,
    HOMEPAGE_ID_BASED,
    VIEW_COUNT,
    DEFAULT_BYW_MODULE_NAME,
    LEFT,
    UBD_CONTENT_ID,
    REC_TYPE,
    BECAUSE_YOU_WATCHED_FALLBACK,
    RECORDS,
    UBD_CREATED_ON,
    UBD_WEEKOFYEAR,
    UBD_DAYOFWEEK,
    IS_PAY_TV,
    TV_CHANNEL_LIST,
    VIEW_HISTORY,
    DURATION,
    MODEL_NAME,
    BYW,
)
from offline_results.recommendation.homepage_recommendation.because_you_watched.prepare_byw_data import (
    BYWData,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.utils import custom_exception, Logging


class BYWModelDefault:
    viewed_relation_history_df = DataFrame()
    content_similarity_no_paytv = DataFrame()
    content_similarity_paytv = DataFrame()

    @staticmethod
    @custom_exception()
    def get_data():
        obj = BYWModelDefault
        if len(obj.viewed_relation_history_df) != 0:
            return
        obj.viewed_relation_history_df = RecommendationUtils.user_viewed_data_from_s3()
        obj.content_similarity_paytv = (
            BYWData.get_content_similarity_based_on_all_content(user_label=PAY_TV)
        )
        obj.content_similarity_no_paytv = (
            BYWData.get_content_similarity_based_on_all_content(user_label=NO_PAY_TV)
        )

    @staticmethod
    @custom_exception()
    def clear_data():
        obj = BYWModelDefault
        obj.viewed_relation_history_df = DataFrame()
        obj.content_similarity_no_paytv = DataFrame()
        obj.content_similarity_paytv = DataFrame()

    @staticmethod
    @custom_exception()
    def fetch_historical_data(graph, user_label, homepage_id_wise):
        try:
            Logging.info("Fetch content-homepage_id mapping")
            content_homepage_id_mapping = BYWData.get_content_homepage_id_mapping(
                graph, user_label, homepage_id_wise
            )
        except Exception:
            graph = ANGraphDb.new_connection_config().graph
            Logging.info("Re-trying to Fetch content-homepage_id mapping")
            content_homepage_id_mapping = BYWData.get_content_homepage_id_mapping(
                graph, user_label, homepage_id_wise
            )
        viewed_relation_history_df = BYWModelDefault.viewed_relation_history_df
        is_pay_tv_status = True if user_label == PAY_TV else False
        viewed_relation_history_df = viewed_relation_history_df[
            viewed_relation_history_df[IS_PAY_TV] == is_pay_tv_status
        ]
        viewed_relation_history_df = viewed_relation_history_df[
            ~viewed_relation_history_df[CONTENT_ID].isin(TV_CHANNEL_LIST)
        ].reset_index(drop=True)
        Logging.info("Generating UBD Dataframe for " + user_label + " users")
        view_history = viewed_relation_history_df[VIEW_HISTORY].to_list()
        view_history2 = [ast.literal_eval(str(i)) for i in view_history]
        history_content_df = DataFrame(
            {
                CONTENT_ID: viewed_relation_history_df[CONTENT_ID].to_list(),
                VIEW_HISTORY: view_history2,
            }
        )
        history_content_df = history_content_df.explode(column=VIEW_HISTORY)
        history_content_df[DURATION] = history_content_df[VIEW_HISTORY].apply(
            lambda x: x[DURATION]
        )
        history_content_df[UBD_CREATED_ON] = history_content_df[VIEW_HISTORY].apply(
            lambda x: x[CREATED_ON]
        )
        history_content_df[UBD_CREATED_ON] = to_datetime(
            history_content_df[UBD_CREATED_ON], dayfirst=True
        )
        history_content_df = history_content_df.sort_values(
            by=UBD_CREATED_ON, ascending=False
        ).reset_index(drop=True)
        history_content_df[UBD_WEEKOFYEAR] = (
            history_content_df[UBD_CREATED_ON].dt.isocalendar().week
        )
        history_content_df[UBD_DAYOFWEEK] = history_content_df[
            UBD_CREATED_ON
        ].dt.dayofweek
        history_content_df = merge(
            history_content_df, content_homepage_id_mapping, on=CONTENT_ID, how=LEFT
        )
        # Logging.info("Filter by dedicated homepage_id for BYW Fallback Model")
        # history_content_df = BYWModelDefault.filter_by_dedicated_homepage_id(history_content_df, user_label,
        #                                                                      filter_on_ubd=True)
        if len(history_content_df.index) == 0:
            return history_content_df, content_homepage_id_mapping
        return history_content_df, content_homepage_id_mapping

    @staticmethod
    @custom_exception()
    def get_dict_format_output(df, key_prefix, homepage_id_wise):
        if homepage_id_wise:
            output_dict = {}
            unique_homepage_id = df[HOMEPAGE_ID].unique()
            for homepage_id in unique_homepage_id:
                key_prefix_cls_hid = key_prefix + ":" + str(homepage_id)
                homepage_wise_df = df.loc[df[HOMEPAGE_ID] == homepage_id]
                homepage_wise_df = homepage_wise_df[
                    [CONTENT_ID, SCORE, CREATED_ON, REC_TYPE]
                ]
                output_dict[key_prefix_cls_hid] = homepage_wise_df.to_dict(RECORDS)
        else:
            df = df[[CONTENT_ID, HOMEPAGE_ID, SCORE, CREATED_ON, REC_TYPE]]
            output_dict = {key_prefix: df.to_dict(RECORDS)}
        return output_dict

    @staticmethod
    @custom_exception()
    def filter_by_dedicated_homepage_id(df, user_label, filter_on_ubd):
        config_dictionary = (
            CONFIG_HOMEPAGE_PAYTV if user_label == PAY_TV else CONFIG_HOMEPAGE_NO_PAYTV
        )
        config_df = DataFrame(config_dictionary.items())
        config_df.columns = [HOMEPAGE_ID, MODEL_NAME]
        config_df = config_df[config_df[MODEL_NAME] == BYW]
        list_config_homepage_id = config_df[HOMEPAGE_ID].tolist()
        df = df.explode(column=HOMEPAGE_ID)
        df = df[df[HOMEPAGE_ID].isin(list_config_homepage_id)].reset_index(drop=True)
        if len(df.index) == 0:
            return df
        if filter_on_ubd:
            history_content_df = df.drop_duplicates([CONTENT_ID, UBD_CREATED_ON])
        else:
            byw_fallback_content_df = df.drop_duplicates([CONTENT_ID, CREATED_ON])
        return history_content_df if filter_on_ubd else byw_fallback_content_df

    @staticmethod
    @custom_exception()
    def default_byw_algorithm(graph, user_label, homepage_id_wise):
        Logging.info("Fetching Content Similarity based on All Content")
        content_similarity_data = (
            BYWModelDefault.content_similarity_paytv
            if user_label == PAY_TV
            else BYWModelDefault.content_similarity_no_paytv
        )
        (
            history_content_df,
            content_homepage_id_mapping,
        ) = BYWModelDefault.fetch_historical_data(graph, user_label, homepage_id_wise)
        if len(history_content_df.index) == 0:
            Logging.info("There is no UBD Data from dedicated Fallback BYW Homepage_id")
            Logging.info("There is no content which will be recommended to the user")
            return history_content_df
        history_content_df_view_count = (
            history_content_df.groupby([CONTENT_ID]).size().to_frame(VIEW_COUNT)
        )
        Logging.info("Preparing Intermediate Dataframe for BYW Model - DEFAULT MODE")
        final_recommendation_df = history_content_df_view_count.sort_values(
            by=VIEW_COUNT, ascending=False
        )
        intermediate_df = (
            final_recommendation_df[[VIEW_COUNT]].rename_axis(CONTENT_ID).reset_index()
        )
        all_recommendation_dict = {}
        all_recommendation_dict_score = {}
        Logging.info(
            "Calculating BYW Score from " + user_label + " UBD data - DEFAULT MODE"
        )
        for idx, data_property in intermediate_df.iterrows():
            content_id = data_property.content_id
            for key_content_id, similarity_data in content_similarity_data.items():
                # If the content which watched by user is available on the content_similarity_data
                if content_id == key_content_id:
                    # Take the first 10 most similar content from similarity_data
                    list_recommended_content_id = []
                    list_recommended_content_id_score = []
                    for recommended_content_id, sim_score in similarity_data.items():
                        list_recommended_content_id.append(recommended_content_id)
                        list_recommended_content_id_score.append(round(sim_score, 3))
                        if len(list_recommended_content_id) == 10:
                            break
                    # Create dictionary of user-recommended content
                    all_recommendation_dict[content_id] = list_recommended_content_id
                    all_recommendation_dict_score[
                        content_id
                    ] = list_recommended_content_id_score
                    break
        Logging.info("Preparing BYW Recommendation Content Output")
        # This step is to create output as dataframe
        # which contain customer_id, recommended_content_id, and rc_created_on
        all_recommendation_dict_df = DataFrame([all_recommendation_dict]).T.reset_index(
            level=0
        )
        all_recommendation_dict_score_df = DataFrame(
            [all_recommendation_dict_score]
        ).T.reset_index(level=0)
        all_recommendation_dict_df.columns = [UBD_CONTENT_ID, CONTENT_ID]
        all_recommendation_dict_score_df.columns = [UBD_CONTENT_ID, SCORE]
        all_recommendation_dict_df = merge(
            all_recommendation_dict_df,
            all_recommendation_dict_score_df,
            on=UBD_CONTENT_ID,
            how=LEFT,
        )
        all_recommendation_dict_df[CREATED_ON] = datetime.utcnow().isoformat()
        all_recommendation_dict_df[UBD_CONTENT_ID] = all_recommendation_dict_df[
            UBD_CONTENT_ID
        ].apply(str)
        all_recommendation_dict_df = all_recommendation_dict_df.explode(
            [CONTENT_ID, SCORE]
        )
        all_recommendation_dict_df[SCORE] = all_recommendation_dict_df[SCORE].apply(
            lambda x: round(x, 3)
        )
        all_recommendation_dict_df[CREATED_ON] = datetime.utcnow().isoformat()
        all_recommendation_dict_df[REC_TYPE] = BECAUSE_YOU_WATCHED_FALLBACK

        if homepage_id_wise:
            byw_content_df = merge(
                all_recommendation_dict_df,
                content_homepage_id_mapping,
                on=CONTENT_ID,
                how=LEFT,
            )
            byw_content_df = byw_content_df[
                ~byw_content_df[HOMEPAGE_ID].isnull()
            ].reset_index(drop=True)
            byw_content_df = byw_content_df.explode(column=HOMEPAGE_ID)
            # byw_content_df = BYWModelDefault.filter_by_dedicated_homepage_id(byw_content_df, user_label, False)
            byw_content_df = byw_content_df.sort_values(
                by=[HOMEPAGE_ID, SCORE], ascending=[True, False]
            )
        else:
            byw_content_df = merge(
                all_recommendation_dict_df,
                content_homepage_id_mapping,
                on=CONTENT_ID,
                how=LEFT,
            )
            byw_content_df = byw_content_df[
                ~byw_content_df[HOMEPAGE_ID].isnull()
            ].reset_index(drop=True)
            byw_content_df = byw_content_df.explode(column=HOMEPAGE_ID)
            # byw_content_df = BYWModelDefault.filter_by_dedicated_homepage_id(byw_content_df, user_label, False)
            byw_content_df = byw_content_df.sort_values(by=SCORE, ascending=False)

        return byw_content_df

    @staticmethod
    @custom_exception()
    def get_default_byw_content_all_content(graph):
        BYWModelDefault.get_data()
        list_of_key_prefix = []
        homepage_id_wise = False
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        empty_df = DataFrame()
        Logging.info("Get BYW Content based on All Content - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating Fallback BYW content based on All Content for "
                + user_label
                + " users"
            )
            output_df = BYWModelDefault.default_byw_algorithm(
                graph, user_label, homepage_id_wise
            )
            if len(output_df.index) == 0:
                Logging.info(
                    "Failed to generate Fallback BYW Content All Content Wise for "
                    + user_label
                    + " users"
                )
                continue
            Logging.info(
                "Success Preparing Default BYW Dataframe Output - DEFAULT MODE"
            )
            key_prefix = (
                SERVICE_NAME
                + ":"
                + DEFAULT_BYW_MODULE_NAME
                + ":"
                + user_label
                + ":"
                + ALL_CONTENT_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        if len(list_output_df) == 0:
            return empty_df, empty_df
        (
            default_byw_pay_tv_all_content,
            default_byw_no_pay_tv_all_content,
        ) = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        default_byw_pay_tv_all_content_dict = BYWModelDefault.get_dict_format_output(
            default_byw_pay_tv_all_content, list_of_key_prefix[0], homepage_id_wise
        )
        default_byw_no_pay_tv_all_content_dict = BYWModelDefault.get_dict_format_output(
            default_byw_no_pay_tv_all_content, list_of_key_prefix[1], homepage_id_wise
        )
        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Default BYW Content based on All Content is "
            + str(duration)
            + " seconds"
        )
        BYWModelDefault.clear_data()
        return (
            default_byw_pay_tv_all_content_dict,
            default_byw_no_pay_tv_all_content_dict,
        )

    @staticmethod
    @custom_exception()
    def get_default_byw_content_homepage_id(graph):
        BYWModelDefault.clear_data()
        BYWModelDefault.get_data()
        list_of_key_prefix = []
        homepage_id_wise = True
        list_user_label = [PAY_TV, NO_PAY_TV]
        list_output_df = []
        empty_df = DataFrame()
        Logging.info("Get BYW Content based on Homepage_id - DEFAULT MODE")
        start = time.time()
        for user_label in list_user_label:
            Logging.info(
                "Start generating Fallback BYW content based on Homepage_id for "
                + user_label
                + " users"
            )
            output_df = BYWModelDefault.default_byw_algorithm(
                graph, user_label, homepage_id_wise
            )
            if len(output_df.index) == 0:
                Logging.info(
                    "Failed to generate Fallback BYW Content Homepage_id Wise for "
                    + user_label
                    + " users"
                )
                continue
            Logging.info(
                "Success Preparing Default BYW Dataframe Output - DEFAULT MODE"
            )
            key_prefix = (
                SERVICE_NAME
                + ":"
                + DEFAULT_BYW_MODULE_NAME
                + ":"
                + user_label
                + ":"
                + HOMEPAGE_ID_BASED
            )
            list_of_key_prefix.append(key_prefix)
            list_output_df.append(output_df)
        if len(list_output_df) == 0:
            return empty_df, empty_df
        (
            default_byw_pay_tv_homepage_id,
            default_byw_no_pay_tv_homepage_id,
        ) = list_output_df

        Logging.info("Preparing the output to JSON Schema")
        # Convert dataframe output to json output
        default_byw_pay_tv_homepage_id_dict = BYWModelDefault.get_dict_format_output(
            default_byw_pay_tv_homepage_id, list_of_key_prefix[0], homepage_id_wise
        )
        default_byw_no_pay_tv_homepage_id_dict = BYWModelDefault.get_dict_format_output(
            default_byw_no_pay_tv_homepage_id, list_of_key_prefix[1], homepage_id_wise
        )

        end = time.time()
        duration = end - start
        Logging.info(
            "Duration for Get Default BYW Content based on Homepage_id is "
            + str(duration)
            + " seconds"
        )
        return (
            default_byw_pay_tv_homepage_id_dict,
            default_byw_no_pay_tv_homepage_id_dict,
        )
