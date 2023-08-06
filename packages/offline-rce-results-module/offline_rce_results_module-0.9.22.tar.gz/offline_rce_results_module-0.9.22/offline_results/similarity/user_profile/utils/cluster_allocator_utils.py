from graphdb.graph import GraphDb
from pandas import DataFrame, concat

from offline_results.common.constants import (
    PAYTVPROVIDER_ID,
    GENDER,
    AGE,
    ACTIVE_LOWER,
    STATUS,
)
from offline_results.similarity.user_profile.config import (
    ASSIGN_CLUSTER_FEATURES,
    GENDER_MAP,
)
from offline_results.similarity.user_profile.config import (
    CLUSTER_NODE_LABEL,
    DEFAULT_CLUSTER_LABEL,
)
from offline_results.utils import class_custom_exception


class ClusterAllocatorUtils:
    def __init__(self, connection_object):
        """
        Constructor to create graph object using
        the input connection details
        :param connection_object: graph
        connection object
        """
        self.connection_object = connection_object
        self.graph = GraphDb.from_connection(connection_object)

    @class_custom_exception()
    def filter_features(self, data=DataFrame) -> DataFrame:
        """
        Filter the dataframe object to only keep
        the features used for identifying
        the cluster labels
        :param data: dataframe object pandas
        :return dataframe object pandas
        """
        return data[ASSIGN_CLUSTER_FEATURES]

    @class_custom_exception()
    def user_has_paytv(self, paytv_val) -> bool:
        """
        Check whether the user is of paytv
        type or non-paytv type
        :param paytv_val: paytv provider
        value in the user record
        :return: boolean indicator
        """
        if paytv_val == -1:
            return False
        return True

    @class_custom_exception()
    def process_user_centroid_records(self, centroids: DataFrame, user: DataFrame):
        """
        Remove unnecessary features from user
        and centroid dataframe objects
        :param centroids: dataframe object pandas
        :param user: dataframe object pandas
        :return: processed centroid and user
        objects
        """
        user = user.reset_index(drop=True)
        user = self.filter_features(data=user)
        user = user.loc[0, :].values.tolist()
        centroids = self.filter_features(data=centroids)
        return centroids, user

    @class_custom_exception()
    def process_paytv_feature(self, users: DataFrame):
        """
        Process the paytvprovider_id field for
        user records
        :param users: dataframe object pandas
        :return: dataframe object pandas
        """
        users[PAYTVPROVIDER_ID] = users[PAYTVPROVIDER_ID].fillna(-1)

        for index in range(len(users)):
            if not isinstance(users.loc[index, PAYTVPROVIDER_ID], int):
                paytv = (users.loc[index, PAYTVPROVIDER_ID])[0]
                users.loc[index, PAYTVPROVIDER_ID] = paytv[PAYTVPROVIDER_ID]

        return users

    @class_custom_exception()
    def get_paytv_wise_users(self, users):
        """
        Segregate users dataframe object into
        paytv and non-paytv users
        :param users: dataframe object pandas
        :return: paytv and nonpaytv users
        dataframe objects
        """
        paytv_users = users[users[STATUS] == ACTIVE_LOWER].reset_index(drop=True)
        nonpaytv_users = users[users[STATUS] != ACTIVE_LOWER].reset_index(drop=True)

        return nonpaytv_users, paytv_users

    @class_custom_exception()
    def preprocess_user_attributes(self, users: DataFrame):
        if GENDER and AGE and PAYTVPROVIDER_ID not in users.columns:
            users = users.assign(gender=-1, age=-1, paytvprovider_id=-1)
            return users

        users[GENDER] = users[GENDER].apply(lambda x: GENDER_MAP[str(x)])
        users[PAYTVPROVIDER_ID] = users[PAYTVPROVIDER_ID].fillna(-1)
        user_paytv = users[users[STATUS] == ACTIVE_LOWER]
        user_no_paytv = users[users[STATUS] != ACTIVE_LOWER]

        user_no_paytv_label = user_no_paytv[
            (user_no_paytv[GENDER] == -1) & (user_no_paytv[PAYTVPROVIDER_ID] == -1)
        ]
        user_no_paytv_label[CLUSTER_NODE_LABEL] = DEFAULT_CLUSTER_LABEL
        user_no_paytv_nlabel = user_no_paytv[
            ~((user_no_paytv[GENDER] == -1) & (user_no_paytv[PAYTVPROVIDER_ID] == -1))
        ]

        user_no_paytv = concat([user_no_paytv_label, user_no_paytv_nlabel], axis=0)
        user_no_paytv[PAYTVPROVIDER_ID] = -1
        user_paytv[PAYTVPROVIDER_ID] = user_paytv[PAYTVPROVIDER_ID].apply(
            lambda x: x[0][PAYTVPROVIDER_ID]
        )

        users = concat([user_paytv, user_no_paytv], axis=0).reset_index(drop=True)

        return users.reset_index(drop=True)
