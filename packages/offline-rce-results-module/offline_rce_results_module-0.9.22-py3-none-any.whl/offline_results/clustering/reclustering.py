import logging
import math
from typing import Tuple, Any
import numpy as np
from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.common.config import S3_RESOURCE, VISIONPLUS_DEV, customer_path, \
    user_paytv_path, HISTORY_THRESHOLD
from offline_results.common.constants import CUSTOMER_ID, STATUS, PAYTVPROVIDER_ID, NAN, \
    ACTIVE_LOWER, USER_DETAIL_UDKEY, GENDER, CUSTOMER_CREATED_ON, CUSTOMER_MODIFIED_ON, BIRTHDAY
import datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame, concat, merge
from offline_results.updater.prepare_ubd import UserMap
from offline_results.common.constants import DURATION, DURATION_REMOVE_LIMIT
from offline_results.updater.preference_updater import PreferenceUpdater
from offline_results.updater.demographics import PreprocessDemography
from offline_results.clustering.config import GENDER_MAP
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans

import matplotlib

matplotlib.use('svg')


class ReCluster:

    @staticmethod
    def get_week_number(date: datetime.datetime) -> int:
        """Returns the week of the month for the specified date.
        :param date: datetime object
        :return: int week number
        """
        # first day in this month
        fd = date.replace(day=1)
        dom = (date.replace(month=date.month % 12 + 1, day=1) - datetime.timedelta(days=1)).day
        adjusted_dom = dom + fd.weekday()
        return int(math.ceil(adjusted_dom / 7.0))

    @staticmethod
    def last_year_months(pre_months: int, date: datetime.datetime) -> DataFrame:
        """
        Function to fetch last year's month/ week wise data
        :param pre_months: integer month number
        :param date: datetime object
        :return: Dataframe object pandas
        """
        concat_data = DataFrame()
        vm_data = DataFrame()
        last_year = date.year - 1
        for old_month in range(pre_months, 13):
            first_datetime = datetime.datetime(last_year, old_month, 1)
            week_number = ReCluster.get_week_number(first_datetime)
            for week in range(1, week_number + 1):
                path = "ubd/{year}/{month_name}/week_{week_number}.csv".format(
                    year=last_year,
                    month_name=datetime.date(1900, old_month, 1).strftime("%B"),
                    week_number=week
                )
                try:
                    vm_data = ConnectS3().read_compress_csv_from_s3(
                        bucket_name=VISIONPLUS_DEV, object_name=path, resource=S3_RESOURCE
                    )
                    if vm_data is None:
                        continue
                except Exception as e:
                    logging.info(f"Error while reading ubd file from S3, Error: {e}")
                vm_data = vm_data[vm_data[DURATION].notnull()]
                vm_data[DURATION] = vm_data[DURATION].astype(int)
                vm_data = vm_data[
                    vm_data[DURATION] > DURATION_REMOVE_LIMIT
                    ]
                concat_data = concat([concat_data, vm_data])
        return concat_data

    @staticmethod
    def fetch_ubd_data() -> DataFrame:
        """
        Fetches ubd data from month/week wise S3 folders
        and concats into a single dataframe.
        return: Dataframe object pandas
        """
        ubd_data = DataFrame()
        vm_data = DataFrame()
        now = datetime.datetime.now()
        month_now = int(now.strftime("%m"))
        month_old = int((now + relativedelta(months=-HISTORY_THRESHOLD)).strftime("%m"))  # Last six months data needed
        if month_old >= month_now:
            ubd_data = ReCluster.last_year_months(pre_months=month_old, date=now)
            month_old = 1
        for month in range(month_old, month_now + 1):
            first_datetime = datetime.datetime(now.year, month, 1)
            week_number = ReCluster.get_week_number(first_datetime)
            for week in range(1, week_number + 1):
                path = "ubd/{year}/{month_name}/week_{week_number}.csv".format(
                    year=now.year,
                    month_name=datetime.date(1900, month, 1).strftime("%B"),
                    week_number=week
                )
                try:
                    vm_data = ConnectS3().read_compress_csv_from_s3(
                        bucket_name=VISIONPLUS_DEV, object_name=path, resource=S3_RESOURCE
                    )
                    if vm_data is None:
                        continue
                except Exception as e:
                    logging.info(f"Error while reading ubd file from S3, Error: {e}")
                vm_data = vm_data[vm_data[DURATION].notnull()]
                vm_data[DURATION] = vm_data[DURATION].astype(int)
                vm_data = vm_data[
                    vm_data[DURATION] > DURATION_REMOVE_LIMIT
                    ]
                ubd_data = concat([ubd_data, vm_data])
        return ubd_data

    @staticmethod
    def fetch_demography(list_users: list) -> DataFrame:
        """
        Fetch demography data of users
        :param list_users: list of customer_ids
        :return: Dataframe object pandas
        """
        customer = DataFrame()
        try:
            customer = ConnectS3().read_compress_pickles_from_S3(
                bucket_name=VISIONPLUS_DEV, object_name=customer_path, resource=S3_RESOURCE
            )
            if "internal_id" in customer.columns:
                customer = customer.drop(columns=["internal_id", "internal_table"])
            customer[CUSTOMER_ID] = customer[CUSTOMER_ID].astype(str)
            customer = customer[customer[CUSTOMER_ID].isin(list_users)].reset_index(drop=True)
            customer = customer.replace(to_replace="nan", value=np.nan)
            user_paytv = ConnectS3().read_compress_pickles_from_S3(
                bucket_name=VISIONPLUS_DEV, object_name=user_paytv_path, resource=S3_RESOURCE
            )
            if "internal_id" in user_paytv.columns:
                user_paytv = user_paytv.drop(columns=["internal_id", "internal_table"])
            user_paytv[STATUS] = user_paytv[STATUS].str.lower()
            customer = customer.merge(user_paytv, on=USER_DETAIL_UDKEY, how="left")
            customer = PreprocessDemography().controller(df=customer, update=False)
            customer[PAYTVPROVIDER_ID] = customer[PAYTVPROVIDER_ID].fillna(NAN)
            customer[PAYTVPROVIDER_ID] = customer[PAYTVPROVIDER_ID].apply(
                lambda x: [{PAYTVPROVIDER_ID: int(float(x))}] if x != NAN else np.nan
            )
        except Exception as e:
            logging.info(f"Unable to read file from S3, Error: {e}")
        finally:
            return customer

    @staticmethod
    def prepare_cluster_features() -> DataFrame:
        """
        Function to prepare features used in clustering
        :return: Dataframe object pandas
        """
        ubd = ReCluster.fetch_ubd_data()
        ubd = UserMap.mapping_ubd(ubd=ubd, update=False)
        if len(ubd) < 100000:
            return
        merged_preferences = PreferenceUpdater.controller(ubd=ubd, update=False)
        user_profile = ReCluster.fetch_demography(list_users=list(set(ubd[CUSTOMER_ID])))
        clustering_features = merge(user_profile, merged_preferences, on=CUSTOMER_ID, how="inner")
        return clustering_features

    @staticmethod
    def segregate_users() -> Tuple[Any, Any]:
        """
        Function to separate paytv and nopaytv users
        :return: Dataframe object pandas
        """
        clustering_features = ReCluster.prepare_cluster_features()
        if clustering_features is None:
            return
        paytv_users = clustering_features[clustering_features[STATUS] == ACTIVE_LOWER].reset_index(drop=True)
        no_paytv_users = clustering_features[clustering_features[STATUS] != ACTIVE_LOWER].reset_index(drop=True)
        return paytv_users, no_paytv_users

    @staticmethod
    def non_attributes(data: DataFrame) -> DataFrame:
        """
        Function to prepare input data for finding optimal
        value of k for paytv and nopaytv users clustering
        :param data: Dataframe object pandas
        :return: Dataframe object pandas
        """
        data = data.drop(
            columns=[CUSTOMER_CREATED_ON, CUSTOMER_MODIFIED_ON, USER_DETAIL_UDKEY, STATUS, BIRTHDAY])
        data = data.replace(to_replace=NAN, value=-1)
        data[GENDER] = data[GENDER].replace(GENDER_MAP)
        data[PAYTVPROVIDER_ID] = data[PAYTVPROVIDER_ID].fillna(NAN)
        data[PAYTVPROVIDER_ID] = data[PAYTVPROVIDER_ID].apply(
            lambda x: x[0][PAYTVPROVIDER_ID] if x != NAN else -1
        )
        data = data.set_index(CUSTOMER_ID)
        return data

    @staticmethod
    def find_k():
        """
        Function to optimal value of k clusters based on
        input data
        """
        users = ReCluster.segregate_users()
        if users is None:
            return
        paytv_users_feature = ReCluster.non_attributes(users[0])
        no_paytv_users_feature = ReCluster.non_attributes(users[1])
        model = KMeans()
        if len(paytv_users_feature) >= 2:
            paytv_visualizer = KElbowVisualizer(model, k=(1, min(100, int(len(paytv_users_feature) / 10))))
            paytv_visualizer.fit(paytv_users_feature)
            paytv_k = paytv_visualizer.elbow_value_
        else:
            paytv_k = len(paytv_users_feature)
        if len(no_paytv_users_feature) >= 2:
            no_paytv_visualizer = KElbowVisualizer(model, k=(1, min(100, int(len(no_paytv_users_feature) / 10))))
            no_paytv_visualizer.fit(no_paytv_users_feature)
            no_paytv_k = no_paytv_visualizer.elbow_value_
        else:
            no_paytv_k = len(no_paytv_users_feature)
        return users, paytv_k, no_paytv_k

