from pandas import DataFrame

from offline_results.common.config import (
    HAS_CATEGORY_PREFERENCE,
    HAS_SUBCATEGORY_PREFERENCE,
)
from offline_results.common.constants import (
    TAGS,
    SUBCATEGORY,
    CATEGORY,
    CUSTOMER_ID,
    TOD,
    DURATION,
    CATEGORY_ID,
    SUBCATEGORY_ID,
    HAS_TAG_PREFERENCE,
    HAS_TOD_PREFERENCE,
    HAS_DURATION_PREFERENCE,
    TAGS_ID,
    VALUE,
    CONTENT_DURATION,
)
from offline_results.recommendation.utils import RecommendationUtils
from offline_results.utils import class_custom_exception


class DataGathering(RecommendationUtils):
    def __init__(
        self,
    ):
        self.ubd = DataFrame()
        self.homepage_having_content = DataFrame()
        self.category_pref = DataFrame()
        self.sub_category_pref = DataFrame()
        self.tags_pref = DataFrame()
        self.preferences = DataFrame()
        self.duration_pref = DataFrame()
        self.tod_pref = DataFrame()

    @class_custom_exception()
    def data_gathering(self, is_paytv):
        self.tags_pref = self.user_pref(
            TAGS, HAS_TAG_PREFERENCE, is_paytv, [TAGS_ID, CUSTOMER_ID]
        )
        self.duration_pref = self.user_pref(
            CONTENT_DURATION, HAS_DURATION_PREFERENCE, is_paytv, [VALUE, CUSTOMER_ID]
        )
        self.category_pref = self.user_pref(
            CATEGORY, HAS_CATEGORY_PREFERENCE, is_paytv, [CATEGORY_ID, CUSTOMER_ID]
        )
        self.sub_category_pref = self.user_pref(
            SUBCATEGORY,
            HAS_SUBCATEGORY_PREFERENCE,
            is_paytv,
            [SUBCATEGORY_ID, CUSTOMER_ID],
        )
        self.tod_pref = self.user_pref(
            TOD, HAS_TOD_PREFERENCE, is_paytv, [VALUE, CUSTOMER_ID]
        )
        self.duration_pref.columns = [DURATION, CUSTOMER_ID]
        self.homepage_having_content = self.content_having_homepage(is_paytv)
        self.ubd = self.user_viewed_data_from_s3()


##test code here
# if __name__ =="__main__":
#     ctl= DataGathering()
#     ctl.data_gathering(True)
