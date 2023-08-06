from graphdb.graph import GraphDb
from graphdb.schema import Node
from offline_results.common.config import TO_READ_FROM_S3_PREFERENCES
from pandas import DataFrame, concat

from offline_results.common.read_write_from_s3 import ConnectS3
from offline_results.clustering.config import GENDER_MAP
from offline_results.clustering.inter_centroid_distance import \
    InterCentroidDistance
from offline_results.common.constants import \
    CUSTOMER_ID, BIRTHDAY, CUSTOMER_CREATED_ON, \
    CUSTOMER_MODIFIED_ON, GENDER, LABEL, CENTROID, PROPERTIES, IS_PAYTV, IS_PAY_TV, MINIBATCH_KMEANS, STATUS
from offline_results.common.constants import DURATION, CONTENT_DURATION


class CentroidGenerator(InterCentroidDistance):

    def __init__(
            self,
            user_features=DataFrame,
            user_clusters=DataFrame,
            connection_object=None
    ):
        """
        Inherits the utils class to forward
        clustering results
        :param user_features: user profile features
        used for generating clustering labels
        :param user_clusters: clustering results
        """

        # merge features and cluster labels using
        # inner join on customer_id
        user_features = user_features.merge(
            user_clusters,
            on=CUSTOMER_ID
        )

        # drop unnecessary parameters
        user_features = user_features.drop(
            columns=[
                BIRTHDAY,
                CUSTOMER_CREATED_ON,
                CUSTOMER_MODIFIED_ON,
                STATUS
            ]
        )

        # map gender values so as to be used
        # in centroid calculations
        user_features[GENDER] = \
            [GENDER_MAP[gender] for
             gender in user_features[GENDER]]

        # call to parent class' constructor
        InterCentroidDistance.__init__(
            self,
            data=user_features
        )

        self.graph = GraphDb.from_connection(
            connection_object
        )

    def get_centroid_df(
            self,
            centroids
    ):
        """
        Convert 2D array of centroid vectors
        into a single dataframe object
        :param centroids: 2D array of centroid
        vectors
        :return: dataframe object pandas
        """
        centroid_df = DataFrame(
            columns=self.features.columns
        )

        for _, centroid in centroids.items():
            centroid = DataFrame(centroid).T
            centroid.columns = centroid_df.columns
            centroid_df = concat(
                [centroid_df, centroid],
                axis=0
            ).reset_index(drop=True)

        centroid_df.columns = centroid_df.columns.str.replace(CONTENT_DURATION, DURATION)

        return centroid_df

    def get_features_to_merge(
            self,
            centroids_df,
            feature
    ):
        """
        Find all the dummy attributes
        for a given feature
        :param centroids_df: dataframe object
        :param feature: feature to find
        dummy attributes of
        :return: list of dummy attributes
        """
        features_to_merge = []
        for column in centroids_df.columns:
            if column.split("_")[0] == feature:
                features_to_merge.append(column)
        return features_to_merge

    def retrieve_feature_preferences(
            self,
            merge_features_df
    ):
        """
        From dummy attributes created during
        user preference generation, retrieve
        the centroid preferences
        :param merge_features_df: dataframe
        object consisting of all dummy attributes
        for a given feature
        :return: centroid property values for
        the given feature
        """

        merge_features = merge_features_df.columns
        preferences = merge_features_df.gt(0.0).values
        return [','.join(merge_features[preference].tolist())
                for preference in preferences]

    def prepare_centroid_properties(
            self,
            centroids_df
    ):
        """
        Prepares centroid properties from
        dummy fields and user demographic
        attributes
        :param centroids_df: feature
        dataframe object for centroids
        :return: centroid node properties
        dataframe object
        """
        property_df = DataFrame()

        # for each user preference feature
        for feature in TO_READ_FROM_S3_PREFERENCES.keys():

            # retrieve the dummy attributes
            features_to_merge = \
                self.get_features_to_merge(
                    centroids_df=centroids_df,
                    feature=feature
                )

            if len(features_to_merge) == 0:
                continue

            # prepare a separate dataframe object for
            # these dummy attributes
            merge_features_df = centroids_df[features_to_merge]

            # retrieve preferences from dummy attributes
            feature_preferences = \
                self.retrieve_feature_preferences(
                    merge_features_df=merge_features_df
                )

            # drop dummy attributes from the centroid
            # dataframe object. The final state of
            # centroids_df will only consist of features
            # that are to included as centroid properties
            centroids_df = centroids_df.drop(
                columns=features_to_merge
            )

            property_df[feature] = feature_preferences

        return concat([centroids_df, property_df], axis=1)

    def plot_centroids(
            self,
            centroid_properties
    ):
        """
        Plot centroids in graphDB
        :param centroid_properties: node properties for
        all centroids
        :return: None, nodes are created in graphDB
        """
        for index in range(len(centroid_properties)):
            centroid = Node(
                **{
                    LABEL: CENTROID,
                    PROPERTIES: centroid_properties[index]
                }
            )
            self.graph.create_node(centroid)

    def compute_centroids(
            self,
            s3_bucket_name,
            s3_object_name,
            resource,
            paytv: bool
    ):
        """
        Driver function for calculating centroids
        and plotting them in graphDB
        :param s3_bucket_name: bucket name of s3
        :param s3_object_name: key where object
        shall be written
        :param resource: boto resource
        :param paytv: boolean indicator variable
        :return: None, creates centroid nodes
        in the graphDB
        """

        # find centroid for each cluster label
        centroids = self.find_all_centroids(
            self.features.to_numpy(),
            self.data[MINIBATCH_KMEANS].to_numpy(),
            MINIBATCH_KMEANS
        )

        # obtain dataframe object of centroid vectors
        centroids_df = self.get_centroid_df(
            centroids
        )

        # create additional centroid property denoting
        # the cluster label to which it belongs
        centroids_df[MINIBATCH_KMEANS] = list(centroids.keys())
        centroids_df[MINIBATCH_KMEANS] = list(map(int, centroids_df[MINIBATCH_KMEANS]))

        # retrieve the set of centroid properties
        centroid_properties = \
            self.prepare_centroid_properties(
                centroids_df
            )

        # add payTV property to the centroid
        if paytv is not None:
            centroid_properties[IS_PAYTV] = str(paytv)
        self.write_centroid_properties_to_s3(centroid_properties=centroid_properties, centroids_df=centroids_df,
                                             resource=resource, s3_bucket_name=s3_bucket_name,
                                             s3_object_name=s3_object_name, paytv=paytv)
        return centroids_df, centroid_properties

    def write_centroid_properties_to_s3(self, centroid_properties, centroids_df, resource, s3_bucket_name,
                                        s3_object_name, paytv):
        if paytv:
            status = "paytv_"
        else:
            status = "no_paytv_"

        ConnectS3().write_csv_to_s3(bucket_name=s3_bucket_name,
                                    object_name=s3_object_name + status + MINIBATCH_KMEANS + "_centroids.csv",
                                    df_to_upload=centroid_properties,
                                    resource=resource)
        ConnectS3().write_csv_to_s3(bucket_name=s3_bucket_name,
                                    object_name=s3_object_name + status + MINIBATCH_KMEANS + "_centroids_feature.csv",
                                    df_to_upload=centroids_df,
                                    resource=resource)
        ConnectS3().write_csv_to_s3(bucket_name=s3_bucket_name,
                                    object_name=s3_object_name + status + MINIBATCH_KMEANS + "_users_clustering_feature.csv",
                                    df_to_upload=self.data,
                                    resource=resource)
        return True
