import datetime
import math

import pandas as pd
from pandas import DataFrame, concat

from offline_results.common.config import MAPPING_KEY
from offline_results.common.config import (
    S3_RESOURCE,
    BUCKET_NAME,
    DURATION_CUTOFF,
    cluster_pkl_path_file,
)
from offline_results.common.constants import (
    CONTENT_ID,
    CATEGORY_ID,
    SUBCATEGORY_ID,
    CATEGORY,
    SUBCATEGORY,
    ACTORS,
    TAGS,
    TAGS_ID,
    CUSTOMER_ID,
    DURATION,
    REGION_NAME,
    DEVOPS,
    VIDEO_ID1,
    ATTRIBUTE1,
    CATEGORY1,
    CATEGORY2,
    ACTOR_ID,
    DIRECTORS,
    DIRECTOR_ID,
    LEFT,
    CREATED_ON,
    VIDEO_ID2,
    CNH_ACTOR_FILENAME,
    CNH_TAGS_FILENAME,
    CNH_DIRECTOR_FILENAME,
    ACTOR_REQUIRED_COLUMN,
    PAY_TV_CONTENT,
    NO_PAY_TV_CONTENT,
    RATING,
    DURATION_REMOVE_LIMIT,
)
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.repository.graph_db_connection import ANGraphDb
from offline_results.updater.utils import UpdaterUtils
from offline_results.utils import custom_exception, Logging


class UserMap:
    @staticmethod
    @custom_exception()
    def get_week_number_from_month(date: datetime.datetime) -> int:
        """Returns the week of the month for the specified date.
        :param date: datetime object
        :return: int week number
        """
        # first day in this month
        fd = date.replace(day=1)
        dom = date.day
        adjusted_dom = dom + fd.weekday()
        return int(math.ceil(adjusted_dom / 7.0))

    @staticmethod
    @custom_exception()
    def get_ubd() -> DataFrame:
        """
        Get year/month/week wise raw ubd data from S3
        """
        now = datetime.datetime.now()
        video_measure_data_1 = DataFrame()
        video_measure_data_2 = DataFrame()
        try:
            path_file_1 = "ubd/{year}/{month_name}/week_{week_number}.csv".format(
                year=now.year,
                month_name=now.strftime("%B"),
                week_number=UserMap.get_week_number_from_month(now),
            )
            video_measure_data_1 = ConnectS3().read_compress_csv_from_s3(
                bucket_name=BUCKET_NAME, object_name=path_file_1, resource=S3_RESOURCE
            )
        except Exception as e:
            Logging.error(f"Error while reading ubd file from S3, Error: {e}")
        try:
            path_file_2 = "ubd/{year}/{month_name}/week_{week_number}.csv".format(
                year=now.year,
                month_name=now.strftime("%B"),
                week_number=UserMap.get_week_number_from_month(now) - 1,
            )
            video_measure_data_2 = ConnectS3().read_compress_csv_from_s3(
                bucket_name=BUCKET_NAME, object_name=path_file_2, resource=S3_RESOURCE
            )
        except Exception as e:
            Logging.error(f"Error while reading ubd file from S3, Error: {e}")
        video_measure_data = concat(
            [video_measure_data_2, video_measure_data_1], ignore_index=True
        )
        if video_measure_data.empty:
            return video_measure_data
        video_measure_data = video_measure_data[video_measure_data[DURATION].notnull()]
        video_measure_data[DURATION] = video_measure_data[DURATION].astype(int)
        video_measure_data = video_measure_data[
            video_measure_data[DURATION] > DURATION_REMOVE_LIMIT
        ]
        data = (
            video_measure_data.groupby([CUSTOMER_ID, VIDEO_ID1])[DURATION]
            .sum()
            .reset_index()
        )
        data = data[data[DURATION] > DURATION_CUTOFF].reset_index(drop=True)
        data = data.drop(columns=[DURATION])
        video_measure_data = pd.merge(
            video_measure_data, data, on=[CUSTOMER_ID, VIDEO_ID1], how="inner"
        )

        return video_measure_data

    @staticmethod
    @custom_exception()
    def get_content_rating(content_label) -> DataFrame:
        """
        Searches the graphdb for content label and returns
        dataframe with content_id and rating.
        :param content_label: no_paytv or pay_tv content label
        :param graph: graph connection object
        :return: Dataframe object pandas
        """
        graph = ANGraphDb.new_connection_config().graph
        response = graph.custom_query(
            query=f"""g.V().hasLabel('{content_label}').match(
                __.as("c").values("content_id").as("content_id"),
                __.as("c").values("rating").as("rating")
                ).select("content_id", "rating")""",
            payload={content_label: content_label},
        )
        graph.connection.close()
        content_ratings = DataFrame()
        for i, j in enumerate(response):
            tmp = DataFrame(j)
            content_ratings = concat([content_ratings, tmp], axis=0)

        return content_ratings.reset_index(drop=True)

    @staticmethod
    @custom_exception()
    def get_ratings_from_content_nodes(data: DataFrame) -> DataFrame:
        """
        Searches the GraphDB for content nodes
         present in UBD and returns the ratings
         from their respective properties
        :param data: UBD dataframe object pandas
        :return: UBD data with ratings field
        """
        print("Retrieving Pay TV Content Ratings...")
        paytv_content_df = UserMap.get_content_rating(PAY_TV_CONTENT)
        print("Retrieving No Pay TV Content Ratings...")
        nopaytv_content_df = UserMap.get_content_rating(NO_PAY_TV_CONTENT)
        ratings = concat(
            [paytv_content_df, nopaytv_content_df], axis=0
        ).drop_duplicates(subset=[CONTENT_ID], keep="first", ignore_index=True)
        print("Merging ratings with UBD data...")
        data = data.merge(ratings, how="left", left_on=VIDEO_ID1, right_on=CONTENT_ID)
        data[RATING] = data[RATING].fillna("nan")
        data = data.drop(columns=[CONTENT_ID])

        return data

    @staticmethod
    @custom_exception()
    def get_content_having_actor():
        contain_having_actor = ConnectS3().read_compress_pickles_from_S3(
            bucket_name=BUCKET_NAME,
            object_name=MAPPING_KEY + CNH_ACTOR_FILENAME,
            resource=S3_RESOURCE,
        )
        return contain_having_actor[ACTOR_REQUIRED_COLUMN]

    @staticmethod
    @custom_exception()
    def get_content_having_director():
        contain_having_director = ConnectS3().read_compress_pickles_from_S3(
            bucket_name=BUCKET_NAME,
            object_name=MAPPING_KEY + CNH_DIRECTOR_FILENAME,
            resource=S3_RESOURCE,
        )
        return contain_having_director[ACTOR_REQUIRED_COLUMN]

    @staticmethod
    @custom_exception()
    def get_content_having_tags():
        content_having_tags = ConnectS3().read_compress_pickles_from_S3(
            bucket_name=BUCKET_NAME,
            object_name=MAPPING_KEY + CNH_TAGS_FILENAME,
            resource=S3_RESOURCE,
        )
        return content_having_tags

    @staticmethod
    @custom_exception()
    def preprocessing_ubd(ubd=None):
        ubd = ubd[ubd[CUSTOMER_ID].notnull()]
        ubd[CUSTOMER_ID] = ubd[CUSTOMER_ID].astype(str)
        ubd = ubd[ubd[CUSTOMER_ID] != "0"]
        ubd[CREATED_ON] = pd.to_datetime(ubd[CREATED_ON], unit="s")
        ubd[REGION_NAME] = ubd[REGION_NAME].astype(str)
        ubd[DEVOPS] = ubd[DEVOPS].astype(str)
        ubd[ATTRIBUTE1] = ubd[ATTRIBUTE1].astype(str)
        ubd[VIDEO_ID1] = ubd[VIDEO_ID1].astype(str)
        ubd = ubd[~ubd[VIDEO_ID1].str.contains(",", na=False)]
        ubd[VIDEO_ID1] = ubd[VIDEO_ID1].astype(int)
        ubd[VIDEO_ID2] = ubd[VIDEO_ID2].fillna(-1)
        ubd[VIDEO_ID2] = ubd[VIDEO_ID2].astype(int)
        ubd = UserMap.fetch_prepare_category(ubd=ubd)
        ubd = UserMap.fetch_prepare_subcategory(ubd=ubd)
        return ubd

    @staticmethod
    @custom_exception()
    def fetch_prepare_category(ubd=None):
        ubd = ubd[pd.to_numeric(ubd[CATEGORY1], errors="coerce").notnull()]

        ubd[CATEGORY] = ubd[CATEGORY1].apply(lambda x: [{CATEGORY_ID: int(float(x))}])
        ubd = ubd.drop(CATEGORY1, axis=1)
        return ubd

    @staticmethod
    @custom_exception()
    def fetch_prepare_subcategory(ubd=None):
        ubd = ubd[pd.to_numeric(ubd[CATEGORY2], errors="coerce").notnull()]
        ubd[SUBCATEGORY] = ubd[CATEGORY2].apply(
            lambda x: [{SUBCATEGORY_ID: int(float(x))}]
        )
        ubd = ubd.drop(CATEGORY2, axis=1)
        return ubd

    @staticmethod
    @custom_exception()
    def prepare_tags(ubd, df_content_having_tag):
        tag = (
            df_content_having_tag.groupby([CONTENT_ID])[TAGS_ID]
            .apply(list)
            .reset_index(name=TAGS_ID)
        )

        tags_df = pd.merge(ubd, tag, left_on=VIDEO_ID1, right_on=CONTENT_ID, how=LEFT)

        tags_df = tags_df[tags_df[TAGS_ID].notnull()]
        tags_df[TAGS] = tags_df[TAGS_ID].apply(lambda x: [{TAGS_ID: int(i)} for i in x])
        tags_df = tags_df.drop([CONTENT_ID, TAGS_ID], axis=1)
        return tags_df

    @staticmethod
    @custom_exception()
    def prepare_actor(ubd, df_content_having_actor):
        actor = (
            df_content_having_actor.groupby([CONTENT_ID])[ACTOR_ID]
            .apply(list)
            .reset_index(name=ACTOR_ID)
        )

        actor_df = pd.merge(
            ubd, actor, left_on=VIDEO_ID1, right_on=CONTENT_ID, how=LEFT
        )

        actor_df = actor_df[actor_df[ACTOR_ID].notnull()]
        actor_df[ACTORS] = actor_df[ACTOR_ID].apply(
            lambda x: [{ACTOR_ID: i} for i in x]
        )
        actor_df = actor_df.drop([CONTENT_ID, ACTOR_ID], axis=1)
        return actor_df

    @staticmethod
    @custom_exception()
    def prepare_director(ubd, df_content_having_actor):
        director = (
            df_content_having_actor.groupby([CONTENT_ID])[ACTOR_ID]
            .apply(list)
            .reset_index(name=DIRECTOR_ID)
        )

        director_df = pd.merge(
            ubd, director, left_on=VIDEO_ID1, right_on=CONTENT_ID, how=LEFT
        )

        director_df = director_df[director_df[DIRECTOR_ID].notnull()]
        director_df[DIRECTORS] = director_df[DIRECTOR_ID].apply(
            lambda x: [{DIRECTOR_ID: i} for i in x]
        )
        director_df = director_df.drop([CONTENT_ID, DIRECTOR_ID], axis=1)
        return director_df

    @staticmethod
    @custom_exception()
    def mapping_ubd(update: bool, ubd=None):
        if update:
            ubd = UserMap.get_ubd()
            if ubd.empty:
                return ubd
        try:
            ubd = UserMap.preprocessing_ubd(ubd)
            existing_clusters = UpdaterUtils.fetch_existing_cluster(
                bucket_name=BUCKET_NAME, object_name=cluster_pkl_path_file
            )
            existing_clusters[CUSTOMER_ID] = existing_clusters[CUSTOMER_ID].astype(str)
            ubd = ubd.merge(
                existing_clusters[[CUSTOMER_ID]], on=CUSTOMER_ID, how="inner"
            )
            del existing_clusters
            tag_data = UserMap.get_content_having_tags()
            actor_data = UserMap.get_content_having_actor()
            director_data = UserMap.get_content_having_director()
            ubd = UserMap.prepare_tags(ubd, tag_data)
            ubd = UserMap.prepare_actor(ubd, actor_data)
            ubd = UserMap.prepare_director(ubd, director_data)
            ubd = UserMap.get_ratings_from_content_nodes(ubd)
        except Exception as e:
            Logging.error(f"Error while reading file from S3, Error: {e}")
        finally:
            return ubd
