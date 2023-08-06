import configparser
import os

import boto3
from pydantic import BaseModel

from offline_results.common.constants import (
    RATING,
    ATTRIBUTE1,
    CATEGORY,
    CATEGORY_ID,
    SUBCATEGORY,
    SUBCATEGORY_ID,
    ACTORS,
    ACTOR_NAME,
    ACTOR_ID,
    DIRECTORS,
    DIRECTOR_NAME,
    TAGS,
    DEFAULT_NAN,
    TAGS_ID,
)

config = configparser.RawConfigParser()


class Config(BaseModel):
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    region_name: str = os.getenv("AWS_REGION_NAME")
    s3_bucket_name: str = os.getenv("AWS_BUCKET_NAME")


S3_RESOURCE = boto3.resource(
    "s3",
    aws_access_key_id=Config().aws_access_key_id,
    aws_secret_access_key=Config().aws_secret_access_key,
    region_name=Config().region_name,
)

KMEANS_FEATURE = "kmeans"
MINIBATCH_KMEANS_FEATURE = "minibatch_kmeans"
WARDS_HIERARCHICAL_FEATURE = "wards_hierarchical"
KMEDOIDS_FEATURE = "kmedoids"
DBSCAN_FEATURE = "dbscan"
OPTICS_FEATURE = "optics"
BIRCH_FEATURE = "birch"
BIRCH_ENSEMBLE_FEATURE = "birch_ensemble"
S3_PAYTV_PREFIX = "paytv_"
S3_NONPAYTV_PREFIX = "nonpaytv_"
IS_PAYTV_PROPERTY_LABEL = "is_paytv"

CLUSTERING_METHODS = [
    KMEANS_FEATURE,
    MINIBATCH_KMEANS_FEATURE,
    WARDS_HIERARCHICAL_FEATURE,
    KMEDOIDS_FEATURE,
    DBSCAN_FEATURE,
    OPTICS_FEATURE,
    BIRCH_FEATURE,
    BIRCH_ENSEMBLE_FEATURE,
]

TO_READ_FROM_S3_PREFERENCES = {
    RATING: ["HAS_RATING_PREFERENCE", RATING],
    ATTRIBUTE1: ["HAS_ATTRIBUTE1_PREFERENCE", ATTRIBUTE1],
    CATEGORY: ["HAS_CATEGORY_PREFERENCE", CATEGORY_ID],
    SUBCATEGORY: ["HAS_SUBCATEGORY_PREFERENCE", SUBCATEGORY_ID],
    ACTORS: ["HAS_ACTOR_PREFERENCE", ACTOR_NAME],
    DIRECTORS: ["HAS_DIRECTOR_PREFERENCE", DIRECTOR_NAME],
    TAGS: ["HAS_TAGS_PREFERENCE", TAGS],
}

TO_READ_FROM_S3_CLUSTERING_LABELS = {
    KMEANS_FEATURE: ["HAS_KMEANS_CLUSTER", KMEANS_FEATURE],
    MINIBATCH_KMEANS_FEATURE: ["HAS_MINIBATCH_CLUSTER", MINIBATCH_KMEANS_FEATURE],
    WARDS_HIERARCHICAL_FEATURE: ["HAS_WARDS_CLUSTER", WARDS_HIERARCHICAL_FEATURE],
    KMEDOIDS_FEATURE: ["HAS_KMEDOIDS_CLUSTER", KMEDOIDS_FEATURE],
    DBSCAN_FEATURE: ["HAS_DBSCAN_CLUSTER", DBSCAN_FEATURE],
    OPTICS_FEATURE: ["HAS_OPTICS_CLUSTER", OPTICS_FEATURE],
    BIRCH_FEATURE: ["HAS_BIRCH_CLUSTER", BIRCH_FEATURE],
    BIRCH_ENSEMBLE_FEATURE: ["HAS_ENSEMBLE_CLUSTER", BIRCH_ENSEMBLE_FEATURE],
}

HAS_PAYTV_PROVIDER = "HAS_PAYTV_PROVIDER"

"""
The list of possible rating values that
can be assigned to content nodes in graphDB.
"""
RATING_VALUES = ["a", "bo", "bo-a", "bo-su", "d", "r", "su"]

"""
To generate pre-trained BERT embeddings
"""
TOKENIZER = "bert-base-uncased"
MODEL = "bert-base-uncased"
ZERO_VECTOR_DIMENSION = 768

"""
List of preference attributes to discard
"""
DISCARD_ATTRIBUTES = [0, DEFAULT_NAN, ""]

"""
UBD Data file to be read from S3
"""
FILENAME_VIDEO_MEASURE = "video_measure_data"

"""
homepage category recommendation 
data filtration configs
"""
OUTLIERS_CUSTOMER = ["0"]
OUTLIERS_HOMEPAGE_ID = [306, 669]
DUPLICATE_VIEWS_CAP = 12
DEFAULT_HOMEPAGE_ID = -1
LOWER_FREQ_HOMEPAGE_ID_CUTOFF = 100

"""
Homepage content recommendations
"""
CONTENT_VIEW_LOWER_THRESHOLD = 10
CONTENT_VIEW_UPPER_THRESHOLD = 540

""" User preferences """
DURATION_CUTOFF = 27_000_000  # in milliseconds == 450 minutes

PREF_FEATURES = {
    RATING: ["HAS_RATING_PREFERENCE", RATING],
    ATTRIBUTE1: ["HAS_ATTRIBUTE1_PREFERENCE", ATTRIBUTE1],
    CATEGORY: ["HAS_CATEGORY_PREFERENCE", CATEGORY_ID],
    SUBCATEGORY: ["HAS_SUBCATEGORY_PREFERENCE", SUBCATEGORY_ID],
    ACTORS: ["HAS_ACTOR_PREFERENCE", ACTOR_ID],
    DIRECTORS: ["HAS_DIRECTOR_PREFERENCE", ACTOR_ID],
    TAGS: ["HAS_TAGS_PREFERENCE", TAGS_ID],
}

""" S3 """
BUCKET_NAME = "visionplus-dev"
USER_MAPPING_KEY = "data/historical/user/raw/mapping/"
"""
User-User filtering
"""
MINIMUM_SIMILAR_USERS_THRESHOLD = 5

# s3 bucket name
VISIONPLUS_DEV = "visionplus-dev"
DEV_VISIONPLUS = "dev-visionplus"

USER_PREFERENCES_PATH = (
    "data/database/user_profile/processed_data_for_an/users_preferences.csv"
)
RAW_DATA_PATH = "data/historical/user/raw/mapping/31052022/"
UBD_DATA_PATH = "pickles/27062022/join_viewed.pkl"
HOMEPAGE_HAVING_CONTENT_PATH = "mapping/24052022/Homepage_Having_Content.csv"
MODELS_PATH = "/models/"
STREAMING_VDB_KEY = "vdb/2022/"
IMPLICIT_RATING_CSV = "pickles/27062022/join_rating.pkl"

USER_CLUSTER_DIST = "data/historical/user/raw/mapping/31052022/user_cluster_dist.pkl"
PAY_TV_CENTROID_FEATURES = "data/historical/user/raw/mapping/31052022/paytv_minibatch_kmeans_centroids_feature.csv"
PAY_TV_USER_CLUSTER_FEATURE = "data/historical/user/raw/mapping/31052022/paytv_minibatch_kmeans_users_clustering_feature.csv"
NO_PAY_TV_USER_CLUSTER_FEATURE = "data/historical/user/raw/mapping/31052022/no_paytv_minibatch_kmeans_users_clustering_feature.csv"
NO_PAY_TV_CENTROID_FEATURES = "data/historical/user/raw/mapping/31052022/no_paytv_minibatch_kmeans_centroids_feature.csv"
PAYTV_USER_CLUSTER_MAPPING_PATH = (
    "data/historical/user/raw/mapping/31052022/paytv_minibatch_kmeans.csv"
)
NO_PAYTV_USER_CLUSTER_MAPPING_PATH = (
    "data/historical/user/raw/mapping/31052022/nonpaytv_minibatch_kmeans.csv"
)
PAY_TV_CLUSTER_CENTROID = (
    "data/historical/user/raw/mapping/31052022/paytv_minibatch_kmeans_centroids.csv"
)
NO_PAY_TV_CLUSTER_CENTROID = (
    "data/historical/user/raw/mapping/31052022/no_paytv_minibatch_kmeans_centroids.csv"
)

VIEWED_DATA_PATH = "pickles/27062022/join_viewed.pkl"
CLUSTER_DATA_PATH = "pickles/27062022/join_kmeans.pkl"
IMPLICIT_RATING_PATH = "pickles/27062022/join_rating.pkl"

MAPPING_KEY = "mapping/"
DURATION_BINS = [10, 20, 30, 60, 70, 90, 120]
TOD_MAPPING = {1: "night", 2: "morning", 3: "noon", 4: "evening"}
HAS_RATING_PREFERENCE = "HAS_RATING_PREFERENCE"
HAS_ATTRIBUTE1_PREFERENCE = "HAS_ATTRIBUTE1_PREFERENCE"
HAS_CATEGORY_PREFERENCE = "HAS_CATEGORY_PREFERENCE"
HAS_SUBCATEGORY_PREFERENCE = "HAS_SUBCATEGORY_PREFERENCE"
HAS_ACTOR_PREFERENCE = "HAS_ACTOR_PREFERENCE"
HAS_DIRECTOR_PREFERENCE = "HAS_DIRECTOR_PREFERENCE"
HAS_TAGS_PREFERENCE = "HAS_TAGS_PREFERENCE"
HAS_TOD_PREFERENCE = "HAS_TOD_PREFERENCE"
HAS_DURATION_PREFERENCE = "HAS_DURATION_PREFERENCE"
cluster_pkl_path_file = "pickles/27062022/join_kmeans.pkl"

MAX_NO_OF_CHUNKS = 10

ENCODING_MODEL = "homepage_encoding_model.pkl"

MAXIMUM_NUMBER_OF_RECOMMENDATIONS = 10


LIVE_TV_CHANNEL_HOMEPAGE_PAYTV = [669, 673]
LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV = [306, 585]
LIVE_TV_CHANNEL_HOMEPAGE_LIST = (
    LIVE_TV_CHANNEL_HOMEPAGE_PAYTV + LIVE_TV_CHANNEL_HOMEPAGE_NO_PAYTV
)

CONFIG_HOMEPAGE_PAYTV = {
    2648: "seasonal",
    2618: "seasonal",
    2614: "seasonal",
    2598: "seasonal",
    2585: "seasonal",
    2532: "seasonal",
    2522: "seasonal",
    2503: "seasonal",
    2488: "seasonal",
    2474: "seasonal",
    2424: "seasonal",
    2390: "seasonal",
    2354: "seasonal",
    2344: "seasonal",
    2235: "seasonal",
    1833: "seasonal",
    1892: "seasonal",
    1821: "seasonal",
    1801: "seasonal",
    1766: "seasonal",
    1995: "seasonal",
    901: "seasonal",
    701: "seasonal",
    897: "seasonal",
    881: "seasonal",
    857: "seasonal",
    797: "seasonal",
    501: "seasonal",
    489: "seasonal",
    457: "seasonal",
    341: "seasonal",
    337: "seasonal",
    533: "seasonal",
    545: "seasonal",
    1648: "seasonal",
    991: "seasonal",
    933: "seasonal",
    929: "seasonal",
    925: "seasonal",
    921: "seasonal",
    1198: "seasonal",
    1153: "seasonal",
    1099: "seasonal",
    210: "popular",
    529: "popular",
    785: "popular",
    789: "popular",
    986: "popular",
    1011: "popular",
    1063: "popular",
    1414: "popular",
    1853: "popular",
    2060: "popular",
    2063: "popular",
    2098: "popular",
    2102: "popular",
    2671: "popular",
    2639: "popular",
    2252: "popular",
    2247: "popular",
    2110: "popular",
    1360: "popular",
    1144: "popular",
    1031: "popular",
    717: "popular",
    705: "popular",
    693: "popular",
    689: "popular",
    202: "popular",
    821: "trending",
    1316: "trending",
    1342: "trending",
    1468: "trending",
    1738: "trending",
    1935: "trending",
    258: "trending",
    2119: "trending",
    2203: "trending",
    2209: "trending",
    2376: "trending",
    2729: "trending",
    2720: "trending",
    2706: "trending",
    2700: "trending",
    2689: "trending",
    2679: "trending",
    2263: "trending",
    2400: "trending",
    1595: "trending",
    1001: "trending",
    1630: "trending",
    957: "trending",
    945: "trending",
    737: "trending",
    677: "trending",
}

CONFIG_NOT_APPLICABLE_FOR_REC_PAYTV = {
    2444: "MotoGP",
    266: "Daftar Tayangan",
    274: "Melanjutkan Tayangan",
    2335: "Ikatan Cinta",
    801: "Yang Terbaru",
}

CONFIG_HOMEPAGE_NO_PAYTV = {
    2641: "seasonal",
    2617: "seasonal",
    2606: "seasonal",
    2593: "seasonal",
    2582: "seasonal",
    2529: "seasonal",
    2518: "seasonal",
    2495: "seasonal",
    2480: "seasonal",
    2468: "seasonal",
    2423: "seasonal",
    2382: "seasonal",
    2346: "seasonal",
    2343: "seasonal",
    2230: "seasonal",
    1882: "seasonal",
    1823: "seasonal",
    1811: "seasonal",
    1791: "seasonal",
    1757: "seasonal",
    1985: "seasonal",
    749: "seasonal",
    889: "seasonal",
    877: "seasonal",
    853: "seasonal",
    793: "seasonal",
    593: "seasonal",
    1639: "seasonal",
    917: "seasonal",
    913: "seasonal",
    909: "seasonal",
    996: "seasonal",
    1180: "seasonal",
    1171: "seasonal",
    1090: "seasonal",
    1026: "seasonal",
    905: "seasonal",
    162: "popular",
    753: "popular",
    761: "popular",
    781: "popular",
    981: "popular",
    1016: "popular",
    1423: "popular",
    1843: "popular",
    2053: "popular",
    2061: "popular",
    2100: "popular",
    2666: "popular",
    2632: "popular",
    2248: "popular",
    2240: "popular",
    2109: "popular",
    1369: "popular",
    1307: "popular",
    1135: "popular",
    1036: "popular",
    641: "popular",
    601: "popular",
    597: "popular",
    581: "popular",
    170: "popular",
    817: "trending",
    849: "trending",
    1325: "trending",
    1351: "trending",
    1477: "trending",
    1729: "trending",
    1945: "trending",
    122: "trending",
    2112: "trending",
    2197: "trending",
    2207: "trending",
    2370: "trending",
    2722: "trending",
    2712: "trending",
    2705: "trending",
    2695: "trending",
    2687: "trending",
    2398: "trending",
    2256: "trending",
    1621: "trending",
    1586: "trending",
    1006: "trending",
    961: "trending",
    953: "trending",
    833: "trending",
    645: "trending",
    617: "trending",
}

CONFIG_NOT_APPLICABLE_FOR_REC_NO_PAYTV = {
    2440: "MotoGP",
    114: "Daftar Tayangan",
    98: "Melanjutkan Tayangan",
    2326: "Ikatan Cinta",
    765: "Yang Terbaru",
}

NUMBER_OF_AUTO_INDENTATIONS = 4
CLUSTER_MODEL_PATH = "models/mapping/"

S3_FILES_TTL = 60 * 60 * 6

"""most-viewed-contents-limit"""
MOST_VIEWED_CONTENTS_LIMIT = 20

"""least-viewed-contents-limit"""
LEAST_VIEWED_CONTENTS_LIMIT = 20

"""top-viewed-limit"""
TOP_VIEWED_HOMEPAGES_LIMIT = 20

"""bottom-viewed-limit"""
BOTTOM_VIEWED_HOMEPAGES_LIMIT = 20

SCORE_WEIGHT = 0.6
IMPLICIT_RATING_WEIGHT = 0.4

customer_path = "vdb/customer.pkl"
user_paytv_path = "mapping/user_pay_tv.pkl"

HISTORY_THRESHOLD = 6 #6 month history only

USER_MAPPING_KEY_CLUSTERING = "data/historical/user/raw/mapping/31052022/"