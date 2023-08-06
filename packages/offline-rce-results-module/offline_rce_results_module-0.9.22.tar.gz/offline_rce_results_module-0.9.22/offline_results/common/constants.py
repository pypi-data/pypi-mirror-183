CONTENT_NODE = "content_node"
LABEL = "label"
PROPERTIES = "properties"
RELATIONSHIP = "relationship_name"
LEFT = "left"
YES = "yes"
NO = "no"

CONTENT_LABEL_COLUMN = "content_label"
ADDITIONAL_STOPWORDS = ["and", "local", "tv", "kontent", "content", "tag"]
RECENT_VIEWED_DATE = "recent_viewed_date"
ACCESS_DATE = "access_date"
ACCESS_DATE_DAYOFYEAR = "access_date_dayofyear"
ACCESS_DATE_DAYOFWEEK = "access_date_dayofweek"
UBD_WEEKOFYEAR = "ubd_weekofyear"
UBD_DAYOFWEEK = "ubd_dayofweek"
UBD_DAYOFYEAR = "ubd_dayofyear"
UBD_CREATED_ON = "ubd_created_on"
UBD_CONTENT_ID = "ubd_content_id"
CONTENT_CREATED_ON = "content_created_on"
HAS_RATING = "HAS_RATING"
RATING_COUNT = "rating_count"
RATING_SUM = "rating_sum"
RATING_AVERAGE = "rating_average"
SCALED_DURATION = "scaled_duration"
SCALED_WEIGHTED_RATING = "scaled_weighted_rating"
SCALED_VIEW_COUNT = "scaled_view_count"
WEEKEND = "weekend"
WEEKDAY = "weekday"
TGIF = "tgif"
NEW_YEAR = "new_year"
CHRISTMAS = "christmas"
VALENTINE = "valentine"
RAMADAN = "ramadan"
ACTIVE = "Active"
BYW_MODULE_NAME = "because_you_watch"
BYW = "byw"
BECAUSE_YOU_WATCHED = "BECAUSE_YOU_WATCH"
BECAUSE_YOU_WATCHED_FALLBACK = "DEFAULT_BECAUSE_YOU_WATCH"
REC_TYPE = "rec_type"
DEFAULT_BYW_MODULE_NAME = "default_because_you_watch"
VIEWED_PICKLE_OBJECT = "pickles/27062022/join_viewed.pkl"
IMPLICIT_RATING_PICKLE_OBJECT = "pickles/27062022/join_rating.pkl"

TV_CHANNEL_LIST = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    17,
    22,
    38,
    46,
    48,
    52,
    55,
    60,
    62,
    64,
    2374,
    2440,
    2449,
    2770,
    2755,
    2830,
    2833,
    2901,
    2909,
    2933,
    6209,
    6537,
    6545,
    6549,
    6553,
    7426,
    7432,
    7414,
    19881,
]

"""for user-content network generation"""
USER_CONTENT_RELATIONSHIP_LABEL = "VIEWED"

"""for CONTENT label"""
PAY_TV_CONTENT = "pay_tv_content"
NO_PAY_TV_CONTENT = "no_pay_tv_content"
CONTENT = "content"
CONTENT_ID = "content_id"
TITLE = "title"
YEAR = "year"
STATUS = "status"
DURATION_MINUTE = "duration_minute"
IS_GEO_BLOCK = "is_geo_block"
IS_FREE = "is_free"
IS_ORIGINAL = "is_original"
IS_BRANDED = "is_branded"
IS_EXCLUSIVE = "is_exclusive"
SYNOPSIS = "synopsis"
SYNOPSIS_EN = "synopsis_en"
START_DATE = "start_date"
END_DATE = "end_date"
MODIFIED_ON = "modified_on"
TYPE = "type"

COMBINED_FEATURES = "combined_features"
CC_SIMILARITY_SCORE = "cc_similarity_score"
ALL_SIMILARITY_SCORE = "all_similarity_score"

"""for RATING label"""
RATING = "rating"

"""for CATEGORY label"""
CATEGORY = "category"
CATEGORY_ID = "category_id"
CATEGORY_EN = "category_en"

"""for SUBCATEGORY label"""
SUBCATEGORY = "subcategory"
SUBCATEGORY_ID = "subcategory_id"
SUBCATEGORY_EN = "subcategory_en"

"""for COUNTRY label"""
COUNTRY = "country"
COUNTRY_ID = "country_id"
COUNTRY_NAME = "country_name"
COUNTRY_DESCRIPTION = "country_description"

"""for TAG label"""
TAGS = "tags"
TAGS_ID = "tags_id"
TAGS_NAME = "tags_name"
DEFAULT_TAGS_DESCRIPTION = "Tidak Ada Deskripsi Tag"

"""for ACTOR label"""
ACTOR = "actor"
ACTORS = "actors"
ACTOR_NAME = "actor_name"
ACTOR_ID = "actor_id"

"""for Director label"""
DIRECTORS = "directors"
DIRECTOR_NAME = "director_name"
DIRECTOR_ID = "director_id"

"""for SEASON label"""
SEASON = "season"
SEASON_ID = "season_id"
SEASON_NAME = "season_name"

"""for CONTENT_CORE label"""
CONTENT_CORE = "content_core"
CONTENT_CORE_ID = "content_core_id"
CONTENT_CORE_SYNOPSIS = "content_core_synopsis"

"""for PACKAGE label"""
PACKAGE = "package"
PACKAGES = "packages"
PACKAGE_ID = "package_id"
PACKAGE_NAME = "package_name"
PACKAGE_NAME_EN = "package_name_en"

"""for PRODUCT label"""
PRODUCT = "product"
PRODUCTS = "products"
PRODUCT_ID = "product_id"
PRODUCT_NAME = "product_name"
PRODUCT_NAME_EN = "product_name_en"

"""for Paytv provider label"""
PAYTV_PROVIDER = "paytv_provider"
PAYTVPROVIDER_ID = "paytvprovider_id"
PAYTVPROVIDER_NAME = "paytvprovider_name"

"""for HOMEPAGE label"""
HOMEPAGE = "homepage"
HOMEPAGE_ID = "homepage_id"
HOMEPAGE_TITLE = "homepage_title"
HOMEPAGE_TITLE_EN = "homepage_title_en"
HOMEPAGE_STATUS = "homepage_status"
HOMEPAGE_TYPE = "homepage_type"
IS_CONNECTED = "is_connected"
HOMEPAGE_VALID_INVALID_IDS = "homepage_valid_invalid_ids"
ACTIVE_LABEL = "Active"

"""for homepage having content"""
HOMEPAGE_HAVING_CONTENT_ID = "id"

"""for preprocessing_utils"""
WHITESPACE_REGEX = "\s+"
SINGLE_SPACE = " "

"""for merge df : content profile"""
CONTENT_BUNDLE_ID = "content_bundle_id"

""" for user labels """
DEFAULT_CLUSTER_ID = -999
USER_DETAIL_HAVING_PACKAGE = "user_detail_having_package"
USER_DETAIL_HAVING_PRODUCT = "user_detail_having_product"
USER_PAY_TV = "user_pay_tv"
CREATED_ON = "created_on"
CUSTOMER_ID = "customer_id"
CUSTOMER_CREATED_ON = "customer_created_on"
CUSTOMER_MODIFIED_ON = "customer_modified_on"
USER_LABEL = "user"
USER_DEMOGRAPHY = "user_demography"
DURATION = "duration"
BIRTHDAY = "birthday"
GENDER = "gender"
UD_KEY = "UserDetail_UDKey"
REGION_NAME = "region_name"
DEVOPS = "devops"
VIDEO_ID1 = "video_id1"
VIDEO_ID2 = "video_id2"
ATTRIBUTE1 = "attribute1"
CATEGORY1 = "category1"
CATEGORY2 = "category2"
CHANNEL_LIVE = "channel_live"
CATCHUP = "catchup"
VOD = "vod"
DEFAULT_DATE = "1970-10-10"
AGE = "age"
MEDIAN_AGE = 52
AGE_UPPER_BOUND = 100
DEFAULT_NUM = "-1"
DEFAULT_NAN = "nan"
UNKNOWN_LABEL = "unknown"
GENDER_VALUES = {"male": "m", "female": "f", "gender": "na"}
ABSURD_VALUE = "\\N"
DUMMY_ATTRIBUTE_SPLIT_ON = "_"
DEFAULT_FEATURE_VALUES = {
    # COUNTRY_ID: DEFAULT_NAN,
    REGION_NAME: UNKNOWN_LABEL,
    DEVOPS: UNKNOWN_LABEL,
    ATTRIBUTE1: DEFAULT_NAN,
    RATING: DEFAULT_NAN,
}
LOCAL_CONNECTION_URI = "ws://localhost:8182/gremlin"
CSV_EXTENSION = ".csv"
GZIP_EXTENSION = ".gzip"
FINAL_MERGED_DF = "final_merged_df"
SOLO_FEATURE_LIST = [RATING, ATTRIBUTE1]
FEATURE_DICT = {
    CATEGORY: CATEGORY_ID,
    SUBCATEGORY: SUBCATEGORY_ID,
    ACTORS: ACTOR_ID,
    DIRECTORS: DIRECTOR_ID,
    TAGS: TAGS_ID,
}
IS_PAYTV = "is_paytv"
IS_PAY_TV = "is_pay_tv"
CLUSTER_IS_PAY_TV = "cluster_is_pay_tv"

CONTENT_BUNDLE = "content_bundle"

"""cache"""
CONTENT_HAVING_COUNTRY = "content_having_country"
CONTENT_HAVING_ACTOR = "content_having_actor"
CONTENT_HAVING_DIRECTOR = "content_having_director"
CONTENT_HAVING_TAGS = "content_having_tags"
HOMEPAGE_HAVING_CONTENT = "homepage_having_content"
PRODUCT_HAVING_PACKAGE = "product_having_package"
CONTENT_BUNDLE_HAVING_CONTENT = "content_bundle_having_content"
PACKAGE_HAVING_CONTENT_BUNDLE = "package_having_content_bundle"
HOME_PAGE_HAVING_CONTENT = "Homepage_Having_Content"
CUSTOMER = "customer"
CONTENT_ID_CONTENT = "Content_id_content"

"""for RATING label"""
RATING = "rating"

"""for CATEGORY label"""
CATEGORY = "category"
CATEGORY_ID = "category_id"

"""for SUBCATEGORY label"""
SUBCATEGORY = "subcategory"
SUBCATEGORY_ID = "subcategory_id"

"""for COUNTRY label"""
COUNTRY_ID = "country_id"

"""for TAG label"""
TAGS = "tags"
TAGS_ID = "tags_id"
TAGS_DESCRIPTION = "tags_description"

"""ubd label"""
UBD = "ubd"

"""for ACTOR label"""
ACTORS = "actors"
ACTOR_ID = "actor_id"

"""for Director label"""
DIRECTORS = "directors"
DIRECTOR_ID = "director_id"

""" for user labels """
REGION_NAME = "region_name"
DEVOPS = "devops"
ATTRIBUTE1 = "attribute1"
DEFAULT_NAN = "nan"
UNKNOWN_LABEL = "unknown"
CONTENT_CORE_TITLE = "content_core_title"
CONTENT_CORE_EPISODE = "content_core_episode"
CONTENT_CORE_SYNOPSIS_EN = "content_core_synopsis_en"
VIEW_COUNT = "view_count"
VIEW_HISTORY = "view_history"
CREATE = "create"
UPDATE = "update"
USER_PREFERENCES = "user_preferences"

"""user preferences"""
HAS_TAG_PREFERENCE = "HAS_TAG_PREFERENCE"
HAS_ACTOR_PREFERENCE = "HAS_ACTOR_PREFERENCE"
HAS_CATEGORY_PREFERENCE = "HAS_CATEGORY_PREFERENCE"
HAS_SUBCATEGORY_PREFERENCE = "HAS_SUBCATEGORY_PREFERENCE"
HAS_DIRECTOR_PREFERENCE = "HAS_DIRECTOR_PREFERENCE"
HAS_RATING_PREFERENCE = "HAS_RATING_PREFERENCE"
HAS_DURATION_PREFERENCE = "HAS_DURATION_PREFERENCE"
HAS_ATTRIBUTE1_PREFERENCE = "HAS_ATTRIBUTE1_PREFERENCE"
HAS_TOD_PREFERENCE = "HAS_TOD_PREFERENCE"
HAS_TAGS_PREFERENCE = "HAS_TAGS_PREFERENCE"

""" content relationships name """

HAS_CONTENT_CORE = "HAS_CONTENT_CORE"
HAS_HOMEPAGE = "HAS_HOMEPAGE"
HAS_ACTOR = "HAS_ACTOR"
HAS_SUBCATEGORY = "HAS_SUBCATEGORY"
HAS_TAG = "HAS_TAG"

""" for horizontal ranking """
RATINGS = "ratings"
VIEWED = "VIEWED"
RECENCY = "recency"
LAST_VIEWED = "last_viewed"
USER_RECENCY = "user_recency"
UNIQUE_USERS_COUNT = "unique_users_count"
R_SCORE = "r_score"
D_SCORE = "d_score"
U_SCORE = "u_score"
V_SCORE = "v_score"
bin_features = {RECENCY: R_SCORE, DURATION: D_SCORE, VIEW_COUNT: V_SCORE}
# UNIQUE_USERS_COUNT: U_SCORE}


COUNT = "count"

""" for merging """
INNER = "inner"

""" for computing rating"""
AGE_OF_EVENT = "age_of_event"
SIZE = "size"
BINS = "bins"
TOP_RATING = "top_rating"
VERY_POSITIVE = "very_positive"
POSITIVE = "positive"
NOT_SURE = "not_sure"
TIME_DECAY_FACTOR = "time_decay_factor"
INVERSE_USER_FREQUENCY = "inverse_user_frequency"
WEIGHTED_RATING = "user_rating"

"""for preference generation"""
DURATION_WEIGHT = 0.8
CLICK_COUNT_WEIGHT = 0.2

"""homepage recommendation"""
VALID_IDS = "valid_ids"
INVALID_IDS = "invalid_ids"
ONE_HOT_ENCODER = "one_hot_encoder"
SCORE = "score"
RANK_SCORE = "rank_score"
CURRENT_MODEL_NAME = "current_model_name"
IMPLICIT_RATING = "implicit_rating"
MEAN_CLUSTER_DIST = "mean_cluster_dist"
MINIBATCH_KMEANS = "minibatch_kmeans"
DISTANCE_FROM_CENTROID = "distance_from_centroid"
USER_DETAIL_UDKEY = "UserDetail_UDKey"
TOD = "tod"
DURATION = "duration"

# source name
S3 = "s3"
GRAPH_DB = "graph_db"

MESSAGE = "message"

# For item-item collaborative filtering
INDEX = "index"
TIME_CREATED = "time_created"
EDGE = "edge"
CLUSTER_ID = "cluster_id"
RECOMMENDED_CONTENT_ID = "recommended_content_id"
RECOMMENDATION_SCORE = "recommendation_score"
SERVICE_NAME = "rce_offline_results_module"

# module names
CBF_MODULE_NAME = "CBF"
CBF_FALLBACK_MODULE_NAME = "DEFAULT_CBF"
ITEM_TO_ITEM_MODULE_NAME = "CF_II"
ITEM_TO_ITEM_DEFAULT_MODULE_NAME = "DEFAULT_CF_II"
USER_TO_USER_MODULE_NAME = "CF_UU"
FALLBACK_USER_TO_USER_MODULE = "DEFAULT_CF_UU"
PREFERENCE_AND_RECENCY_MODULE = "PREFERENCE_AND_RECENCY"
FALLBACK_PREFERENCE_AND_RECENCY_MODULE = "DEFAULT_PREFERENCE_AND_RECENCY"
FALLBACK_MLC_RANK_MODULE = "DEFAULT_MLC_RANK"
MOST_VIEWED_MODULE_NAME = "MOST_VIEWED"
LEAST_VIEWED_MODULE_NAME = "LEAST_VIEWED"
FALLBACK_MOST_VIEWED_MODULE_NAME = "DEFAULT_MOST_VIEWED"
FALLBACK_LEAST_VIEWED_MODULE_NAME = "DEFAULT_LEAST_VIEWED"
TOP_VIEWED_MODULE_NAME = "TOP_VIEWED"
BOTTOM_VIEWED_MODULE_NAME = "BOTTOM_VIEWED"
MLC_RANK_MODULE = "MLC_RANK"
HOMEPAGE_RECENCY_MODULE_NAME = "RECENCY"
DEFAULT_HOMEPAGE_RECENCY_MODULE_NAME = "DEFAULT_RECENCY"
DEFAULT_TOP_VIEWED_MODULE_NAME = "DEFAULT_TOP_VIEWED"
DEFAULT_BOTTOM_VIEWED_MODULE_NAME = "DEFAULT_BOTTOM_VIEWED"
TRENDING_MODULE_NAME = "TRENDING"
DEFAULT_TRENDING_MODULE_NAME = "DEFAULT_TRENDING"
POPULAR_MODULE_NAME = "POPULAR"
DEFAULT_POPULAR_MODULE_NAME = "DEFAULT_POPULAR"
SEASONAL_MODULE_NAME = "SEASONAL"
DEFAULT_SEASONAL_MODULE_NAME = "DEFAULT_SEASONAL"

PAY_TV = "pay_tv"
NO_PAY_TV = "no_pay_tv"

HOMEPAGE_ID_BASED = "homepage_id_based"
ALL_CONTENT_BASED = "all_content_based"
RECORDS = "records"

MAX_USERS = 7000000
ITERATE_CLUSTER_RANGE = 5000
USER_SIMILAR_COUNT = 100000

YYMMDD = "%Y/%m/%d"

# For updating network
ACTOR_REQUIRED_COLUMN = ["content_id", "actor_id"]
CNH_ACTOR_FILENAME = "content_having_actor.pkl"
CNH_DIRECTOR_FILENAME = "content_having_director.pkl"
CNH_TAGS_FILENAME = "content_having_tags.pkl"
VM_RENAME_COLUMN = {
    "tscreated": "created_on",
    "userid": "customer_id",
    "ctrcode": "country_id",
    "regname": "region_name",
    "id1": "video_id1",
    "id2": "video_id2",
    "name1": "video_name1",
    "name2": "video_name2",
}

PREFERENCE_FEATURE_DICT = {
    CATEGORY: CATEGORY_ID,
    SUBCATEGORY: SUBCATEGORY_ID,
    ACTORS: ACTOR_ID,
    DIRECTORS: DIRECTOR_ID,
    TAGS: TAGS_ID,
}

CONTENT_DURATION = "content_duration"
VALUE = "value"

PREF_FEATURES = [
    RATING,
    ATTRIBUTE1,
    CATEGORY,
    SUBCATEGORY,
    ACTORS,
    DIRECTORS,
    TAGS,
    DURATION,
    TOD,
]
UPDATED_ON = "updated_on"
PREVIOUS_TO_PREVIOUS_CLUSTER_ID = "previous_to_previous_cluster_id"
PREVIOUS_CLUSTER_ID = "previous_cluster_id"
tqdm_bar_format = "{desc:<5.5}{percentage:5.0f}%|{bar:70}{r_bar}"
DURATION_REMOVE_LIMIT = 300_000  # in milliseconds == 5 minutes

CONTENT_STATUS = "content_status"
TRUE = "True"
FALSE = "False"
MEAN_USER_ID = "mean_user_id"
NAN = "nan"
LAST = "last"
MODEL_POPULAR = "model_popular"

SUM = "sum"
MODEL_NAME = "model"
RIGHT = "right"

RELATIONSHIP_NAME = "relationship_name"
KEY_UD = "ud_key"
USER_PAYTV_FILENAME = "user_pay_tv.pkl"
NEW_PAYTV = "new_paytv"
NEW = "new"
UNMATCHED = "unmatched"
MATCHED = "matched"

FIRST_QUANTILE = 0.25
THIRD_QUANTILE = 0.75

IS_PAY_TV_NEW = "is_pay_tv_new"
ACTIVE_LOWER = "active"

USER_CLUSTER_INFO = "user_cluster_info"
USER_LOG = "user_log"
HOMEPAGE_CONTENT_DF = "homepage_content_df"
ACTIVE_HOMEPAGE_ID_LIST = "active_homepage_id_list"
MEAN_USER = "mean_user"
CONTENT_DF = "content_df"
CONTENT_TAG_DF = "content_tag_df"
CONTENT_CORE_DF = "content_core_df"
ALL_CONTENT_CORE_SYNOPSIS = "all_content_core_synopsis"
SIMILARITY_DF = "similarity_df"

GENDER_NAN = "gender_nan"

DISTANCE_FROM_MEAN_USER = "distance_from_mean_user"
SIMILAR_USER_COUNT = 10
SCORE_ROUNDOFF = 3

NAN_DUMMY_FEATURE = "_nan"
NON_FEATURES = [
    CUSTOMER_ID,
    MINIBATCH_KMEANS
    ]

S3_PAYTV_PREFIX = "paytv_"
S3_NONPAYTV_PREFIX = "no_paytv_"
CENTROID = "centroid"
