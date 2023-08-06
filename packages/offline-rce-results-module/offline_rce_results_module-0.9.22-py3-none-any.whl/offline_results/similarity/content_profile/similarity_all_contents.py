import logging
import time
from pandas import merge

from offline_results.common.constants import (
    CONTENT_CORE_ID,
    LEFT,
    CONTENT_ID,
    COMBINED_FEATURES,
    TITLE,
    SYNOPSIS,
    TAGS_DESCRIPTION,
    CONTENT_CORE_SYNOPSIS,
    INDEX
)
from offline_results.similarity.content_profile.query_utils import QueryUtils
from offline_results.similarity.content_profile.similarity_utils import SimilarityUtils
from offline_results.utils import custom_exception, Logging


class SimilarityAllContents:
    @staticmethod
    @custom_exception()
    def prepare_similarity_based_on_all_content(content_label):
        logging.info("Start calculating 'Content similarity'...")
        dict_content_similarities = None
        start_time = time.time()
        content_df = QueryUtils.get_content_id_title_and_synopsis(content_label)
        content_tag_df = QueryUtils.tag_data(content_label)
        content_core_df = QueryUtils.content_core_data(content_label)
        all_content_core_synopsis = QueryUtils.get_all_synopsys()
        cc_synopsis = merge(
            content_core_df, all_content_core_synopsis, on=CONTENT_CORE_ID, how=LEFT
        )

        tag_content_core_merged_df = merge(
            content_tag_df, cc_synopsis, on=[CONTENT_ID], how=LEFT
        )

        final_df = merge(
            tag_content_core_merged_df, content_df, on=[CONTENT_ID], how=LEFT
        )

        if len(final_df) > 0:
            final_df[SYNOPSIS] = final_df[SYNOPSIS].astype(str)
            final_df[CONTENT_CORE_SYNOPSIS] = final_df[CONTENT_CORE_SYNOPSIS].fillna(
                " "
            )
            final_df[COMBINED_FEATURES] = (
                final_df[TITLE]
                + ","
                + final_df[SYNOPSIS]
                + ","
                + final_df[TAGS_DESCRIPTION]
                + ","
                + final_df[CONTENT_CORE_SYNOPSIS]
            )

            temp_df = final_df[[CONTENT_ID, COMBINED_FEATURES]]

            temp_df = (
                temp_df.drop_duplicates([CONTENT_ID]).reset_index().drop(columns=INDEX)
            )

            tfidf_df = SimilarityUtils.create_tfidf_df(temp_df)

            dict_content_similarities = (
                SimilarityUtils.calculate_single_cosine_similarity(tfidf_df)
            )

        end_time = time.time()

        Logging.info(
            "Total time taken to compute content similarity for all contents : {} seconds".format(
                end_time - start_time
            )
        )

        return dict_content_similarities
