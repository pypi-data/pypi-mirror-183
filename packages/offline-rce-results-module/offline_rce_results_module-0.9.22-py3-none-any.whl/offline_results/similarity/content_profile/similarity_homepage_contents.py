import time
from typing import Dict, Any

from pandas import DataFrame, merge, concat

from offline_results.common.constants import (
    CONTENT_CORE_ID,
    LEFT,
    CONTENT_ID,
    COMBINED_FEATURES,
    TITLE,
    SYNOPSIS,
    TAGS_DESCRIPTION,
    CONTENT_CORE_SYNOPSIS,
    INDEX,
    HOMEPAGE_ID,
    RECOMMENDED_CONTENT_ID,
    SCORE,
    CONTENT_DF,
    CONTENT_TAG_DF,
    HOMEPAGE_CONTENT_DF,
    CONTENT_CORE_DF,
    ALL_CONTENT_CORE_SYNOPSIS,
)
from offline_results.similarity.content_profile.query_utils import QueryUtils
from offline_results.similarity.content_profile.similarity_utils import SimilarityUtils
from offline_results.utils import custom_exception, Logging


class SimilarityHomepageContents:
    local_cache: Dict[str, Any]

    def __init__(self, content_label):
        SimilarityHomepageContents.local_cache = {
            CONTENT_DF: QueryUtils.get_content_id_title_and_synopsis(content_label),
            CONTENT_TAG_DF: QueryUtils.tag_data(content_label),
            HOMEPAGE_CONTENT_DF: QueryUtils.homepage_data(content_label),
            CONTENT_CORE_DF: QueryUtils.content_core_data(content_label),
            ALL_CONTENT_CORE_SYNOPSIS: QueryUtils.get_all_synopsys(),
        }

    @staticmethod
    @custom_exception()
    def prepare_similarity_based_on_homepage_id(content_label, homepage_id):
        start_time = time.time()

        content_df = QueryUtils.get_content_id_title_and_synopsis(content_label)

        content_tag_df = QueryUtils.tag_data(content_label)

        content_homepage_df = QueryUtils.homepage_data(content_label)

        content_homepage_tag_df = merge(
            content_tag_df, content_homepage_df, on=[CONTENT_ID], how=LEFT
        )

        content_title_synopsis_df = merge(
            content_df, content_homepage_tag_df, on=[CONTENT_ID], how=LEFT
        )

        content_homepage_tag_df = content_title_synopsis_df[
            content_title_synopsis_df[HOMEPAGE_ID] == homepage_id
        ]

        content_core_df = QueryUtils.content_core_data(content_label)

        all_content_core_synopsis = QueryUtils.get_all_synopsys()

        cc_synopsis = merge(
            content_core_df, all_content_core_synopsis, on=[CONTENT_CORE_ID], how=LEFT
        )

        final_df = merge(
            content_homepage_tag_df, cc_synopsis, on=[CONTENT_ID], how=LEFT
        )

        similarity_df = DataFrame()

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

            list_tfidf_df = SimilarityUtils.generate_tfidf_matrix([temp_df])

            list_dict_content_similarities = (
                SimilarityUtils.calculate_cosine_similarity(list_tfidf_df)
            )

            df = DataFrame(list_dict_content_similarities).T
            df[CONTENT_ID] = df.index
            sim_df = (
                DataFrame([*df[0]], df.index)
                .stack()
                .rename_axis([None, RECOMMENDED_CONTENT_ID])
                .reset_index(1, name=SCORE)
            )
            recommendation_df = df[[CONTENT_ID]].join(sim_df)
            recommendation_df[HOMEPAGE_ID] = homepage_id
            similarity_df = concat([similarity_df, recommendation_df], axis=0)

        end_time = time.time()

        Logging.info(
            "Total time taken to compute content similarity homepage ID {} : {} seconds".format(
                homepage_id, end_time - start_time
            )
        )

        return similarity_df
