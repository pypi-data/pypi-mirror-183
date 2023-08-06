import time
from functools import reduce

from pandas import DataFrame, merge

from offline_results.common.config import (
    HAS_TOD_PREFERENCE,
    HAS_DURATION_PREFERENCE,
    HAS_CATEGORY_PREFERENCE,
    HAS_ACTOR_PREFERENCE,
    HAS_TAGS_PREFERENCE,
    HAS_RATING_PREFERENCE,
    HAS_DIRECTOR_PREFERENCE,
    HAS_SUBCATEGORY_PREFERENCE,
    HAS_ATTRIBUTE1_PREFERENCE,
)
from offline_results.common.constants import (
    CUSTOMER_ID,
    ACTOR,
    RATING,
    ATTRIBUTE1,
    PREFERENCE_FEATURE_DICT,
    CATEGORY,
    SUBCATEGORY,
    ACTORS,
    TAGS,
    DIRECTORS,
    ACTOR_ID,
    TAGS_ID,
    SUBCATEGORY_ID,
    CATEGORY_ID,
    TOD,
    VALUE,
    CONTENT_DURATION,
)
from offline_results.preferences.generate_preferences import PreferenceGenerator
from offline_results.preferences.relationship_extractor import RelationshipExtractor
from offline_results.preferences.viewtime_preferences import UserViewTimePreferences
from offline_results.updater.behaviour import PreprocessBehaviour
from offline_results.updater.process_generate_pref import MainImplementation
from offline_results.updater.utils import UpdaterUtils
from offline_results.utils import custom_exception


class PreferenceUpdater:
    @staticmethod
    @custom_exception()
    def get_solo_preferences(data: DataFrame, update: bool):
        """
        Find user preferences for rating and attribute1
        :param data: dataframe object pandas
        :param update: True if running from UpdaterMain
        :return: preferences dataframe object pandas
        """
        main_implementation = MainImplementation(df=data)

        behaviour = PreprocessBehaviour()

        print("Preprocessing rating and attribute1 features...")
        solo_features = behaviour.controller(
            data=main_implementation.df, to_explode=False
        )
        print("Successfully preprocessed rating and attribute1 features...")

        print("Generating rating preferences...")
        rating_obj = PreferenceGenerator(
            feature=RATING, feature_cutoff=2, user_cutoff=2
        )
        rating_raw_preference = rating_obj.controller(data=solo_features)
        if update:
            rating_preference = PreferenceUpdater.get_feature_relations(
                rating_raw_preference.copy()
            )
            print("Starting dropping existing HAS_RATING_PREFERENCE...")
            time.sleep(5)
            UpdaterUtils.drop_existing_rel(rating_preference, HAS_RATING_PREFERENCE)
            print("Starting dumping HAS_RATING_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_str_relations(
                dump_data=rating_preference,
                destination_label=RATING,
                relation_label=HAS_RATING_PREFERENCE,
                df_attribute=rating_preference.columns[-1],
                destination_property=RATING,
            )

        print("Generating attribute1 preferences...")
        attribute1_obj = PreferenceGenerator(
            feature=ATTRIBUTE1, feature_cutoff=2, user_cutoff=2
        )
        attribute1_raw_preference = attribute1_obj.controller(data=solo_features)
        if update:
            attribute1_preference = PreferenceUpdater.get_feature_relations(
                attribute1_raw_preference.copy()
            )
            print("Starting dropping existing HAS_ATTRIBUTE1_PREFERENCE...")
            time.sleep(5)
            UpdaterUtils.drop_existing_rel(attribute1_preference, HAS_ATTRIBUTE1_PREFERENCE)
            print("Starting dumping HAS_ATTRIBUTE1_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_str_relations(
                dump_data=attribute1_preference,
                destination_label=ATTRIBUTE1,
                relation_label=HAS_ATTRIBUTE1_PREFERENCE,
                df_attribute=attribute1_preference.columns[-1],
                destination_property=ATTRIBUTE1,
            )
        print("Attribute1 preferences created successfully...")
        del solo_features
        del behaviour
        del main_implementation
        return rating_raw_preference, attribute1_raw_preference

    @staticmethod
    @custom_exception()
    def get_category_preference(data: DataFrame, update: bool):
        """
        Find user preference for category attribute
        :param data: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: category preference dataframe
        """
        main_implementation = MainImplementation(df=data)

        print("Working on category attribute...")
        category_raw_preference = main_implementation.controller(
            feature=CATEGORY, value=PREFERENCE_FEATURE_DICT[CATEGORY]
        )
        print("Category preferences created successfully...")
        del main_implementation
        if update:
            category_preference = PreferenceUpdater.get_feature_relations(
                category_raw_preference.copy()
            )
            print("Starting to drop existing HAS_CATEGORY_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(category_preference, HAS_CATEGORY_PREFERENCE)
            print("Starting dumping HAS_CATEGORY_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=category_preference,
                destination_label=CATEGORY,
                relation_label=HAS_CATEGORY_PREFERENCE,
                df_attribute=category_preference.columns[-1],
                destination_property=CATEGORY_ID,
            )
        return category_raw_preference

    @staticmethod
    @custom_exception()
    def get_subcategory_preference(data: DataFrame, update: bool):
        """
        Find user preference for subcategory attribute
        :param data: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: subcategory preference dataframe
        """
        main_implementation = MainImplementation(df=data)
        print("Working on subcategory attribute...")
        subcategory_raw_preference = main_implementation.controller(
            feature=SUBCATEGORY, value=PREFERENCE_FEATURE_DICT[SUBCATEGORY]
        )
        print("Subcategory preferences created successfully...")
        del main_implementation
        if update:
            subcategory_preference = PreferenceUpdater.get_feature_relations(
                subcategory_raw_preference.copy()
            )
            print("Starting to drop existing HAS_SUBCATEGORY_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(
                subcategory_preference, HAS_SUBCATEGORY_PREFERENCE
            )
            print("Starting dumping HAS_SUBCATEGORY_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=subcategory_preference,
                destination_label=SUBCATEGORY,
                relation_label=HAS_SUBCATEGORY_PREFERENCE,
                df_attribute=subcategory_preference.columns[-1],
                destination_property=SUBCATEGORY_ID,
            )
        return subcategory_raw_preference

    @staticmethod
    @custom_exception()
    def get_tags_preference(data: DataFrame, update: bool):
        """
        Find user preference for tags attribute
        :param data: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: tags preference dataframe
        """
        main_implementation = MainImplementation(df=data)
        print("Working on tags attribute...")
        tags_raw_preference = main_implementation.controller(
            feature=TAGS, value=PREFERENCE_FEATURE_DICT[TAGS]
        )
        print("Tags preferences created successfully...")
        del main_implementation
        if update:
            tags_preference = PreferenceUpdater.get_feature_relations(
                tags_raw_preference.copy()
            )
            print("Starting to drop existing HAS_TAGS_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(tags_preference, HAS_TAGS_PREFERENCE)
            print("Starting dumping HAS_TAGS_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=tags_preference,
                destination_label=TAGS,
                relation_label=HAS_TAGS_PREFERENCE,
                df_attribute=tags_preference.columns[-1],
                destination_property=TAGS_ID,
            )
        return tags_raw_preference

    @staticmethod
    @custom_exception()
    def get_directors_preference(
        data: DataFrame, update: bool
    ):
        """
        Find user preference for director attribute
        :param data: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: directors preference dataframe
        """
        main_implementation = MainImplementation(df=data)
        print("Working on directors attribute....")
        directors_raw_preference = main_implementation.controller(
            feature=DIRECTORS, value=PREFERENCE_FEATURE_DICT[DIRECTORS]
        )
        print("Directors preferences created successfully...")
        del main_implementation
        if update:
            directors_preference = PreferenceUpdater.get_feature_relations(
                directors_raw_preference.copy()
            )
            print("Starting to drop existing HAS_DIRECTOR_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(directors_preference, HAS_DIRECTOR_PREFERENCE)
            print("Starting dumping HAS_DIRECTOR_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=directors_preference,
                destination_label=ACTOR,
                relation_label=HAS_DIRECTOR_PREFERENCE,
                df_attribute=directors_preference.columns[-1],
                destination_property=ACTOR_ID,
            )
        return directors_raw_preference

    @staticmethod
    @custom_exception()
    def get_actors_preference(
        data: DataFrame, update: bool
    ):
        """
        Find user preference for actors attribute
        :param data: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: actors preference dataframe
        """
        main_implementation = MainImplementation(df=data)
        print("Working on actors attribute...")
        actors_raw_preference = main_implementation.controller(
            feature=ACTORS, value=PREFERENCE_FEATURE_DICT[ACTORS]
        )
        print("Actors preferences created successfully...")
        del main_implementation
        if update:
            actors_preference = PreferenceUpdater.get_feature_relations(
                actors_raw_preference.copy()
            )
            print("Starting to drop existing HAS_ACTOR_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(actors_preference, HAS_ACTOR_PREFERENCE)
            print("Starting dumping HAS_ACTOR_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=actors_preference,
                destination_label=ACTOR,
                relation_label=HAS_ACTOR_PREFERENCE,
                destination_property=ACTOR_ID,
                df_attribute=actors_preference.columns[-1],
            )
        return actors_raw_preference

    @staticmethod
    @custom_exception()
    def get_viewtime_duration_preference(data: DataFrame, update: bool):
        """
        Function to fetch, drop and dump tod and duration preference
        from ubd data
        :param data: Dataframe object pandas
        :param update: True if running from UpdaterMain
        """
        view_time_preference = UserViewTimePreferences()
        print("Generating TOD and Duration preferences...")
        (
            tod_raw_preference,
            duration_raw_preference,
        ) = view_time_preference.get_viewtime_preferences(data)
        if update:
            tod_preference = PreferenceUpdater.get_feature_relations(
                tod_raw_preference.copy()
            )
            print("Starting to drop existing HAS_TOD_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(tod_preference, HAS_TOD_PREFERENCE)
            print("Starting dumping HAS_TOD_PREFERENCE relations...")
            UpdaterUtils.dump_str_relations(
                dump_data=tod_preference,
                destination_label=TOD,
                relation_label=HAS_TOD_PREFERENCE,
                df_attribute=tod_preference.columns[-1],
                destination_property=VALUE,
            )
        if update:
            duration_preference = PreferenceUpdater.get_feature_relations(
                duration_raw_preference.copy()
            )
            print("Starting to drop existing HAS_DURATION_PREFERENCE...")
            UpdaterUtils.drop_existing_rel(duration_preference, HAS_DURATION_PREFERENCE)
            print("Starting dumping HAS_DURATION_PREFERENCE relations...")
            time.sleep(5)
            UpdaterUtils.dump_relations(
                dump_data=duration_preference,
                destination_label=CONTENT_DURATION,
                relation_label=HAS_DURATION_PREFERENCE,
                df_attribute=duration_preference.columns[-1],
                destination_property=VALUE,
            )
        return tod_raw_preference, duration_raw_preference

    @staticmethod
    @custom_exception()
    def get_feature_relations(data: DataFrame) -> DataFrame:
        """
        Use the relationship extractor to extract
        relationship dataframe object based on
        user's preferences
        :param data: dataframe object pandas
        :return: dataframe object pandas with each
        record representing a relationship between
        a user and a node type.
        """
        re = RelationshipExtractor(data=data)
        return re.controller()

    @staticmethod
    @custom_exception()
    def get_merged_df(ubd: DataFrame, update: bool):
        """
        Function to call all other preference function and
        get merged_df of all the raw preferences to be used
        in cluster updater part
        :param ubd: ubd dataframe
        :param update: True if running from UpdaterMain
        :return: Dataframe object pandas
        """
        preference_df_list = []
        preference_updater = PreferenceUpdater()
        actors_preference = preference_updater.get_actors_preference(data=ubd, update=update)
        preference_df_list.append(actors_preference)
        time.sleep(5)
        directors_preference = preference_updater.get_directors_preference(data=ubd, update=update)
        preference_df_list.append(directors_preference)
        time.sleep(5)
        tags_preference = preference_updater.get_tags_preference(data=ubd, update=update)
        preference_df_list.append(tags_preference)
        time.sleep(5)
        (
            rating_preference,
            attribute1_preference,
        ) = preference_updater.get_solo_preferences(data=ubd, update=update)
        preference_df_list.append(rating_preference)
        preference_df_list.append(attribute1_preference)
        time.sleep(5)
        category_preference = preference_updater.get_category_preference(data=ubd, update=update)
        preference_df_list.append(category_preference)
        time.sleep(5)
        subcategory_preference = preference_updater.get_subcategory_preference(data=ubd, update=update)
        preference_df_list.append(subcategory_preference)
        time.sleep(5)
        (
            tod_preference,
            content_duration_preference,
        ) = preference_updater.get_viewtime_duration_preference(data=ubd, update=update)
        preference_df_list.append(tod_preference)
        preference_df_list.append(content_duration_preference)
        time.sleep(5)
        merged_df = reduce(
            lambda l, r: merge(l, r, on=CUSTOMER_ID, how="inner"), preference_df_list
        )
        return merged_df

    @staticmethod
    @custom_exception()
    def controller(
        ubd: DataFrame, update: bool
    ) -> DataFrame:
        """
        Driver function for PreferenceUpdater class.
        :param ubd: ubd dataframe
        :param update: True if running from UpdaterMain
        :return : Dataframe object pandas
        """
        merged_df = PreferenceUpdater.get_merged_df(ubd=ubd, update=update)
        return merged_df
