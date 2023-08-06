import re
from collections import OrderedDict
import nltk
import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from offline_results.common.constants import (
    CONTENT_ID,
    COMBINED_FEATURES,
    ADDITIONAL_STOPWORDS,
)
from offline_results.utils import custom_exception, Logging


class SimilarityUtils:
    @staticmethod
    @custom_exception()
    def create_tfidf_df(df):
        nltk.download("stopwords")
        # PREPROCESS THE COMBINED FEATURES
        factory = StopWordRemoverFactory()
        stop_words = stopwords.words("indonesian")
        stopword_sastrawi = factory.get_stop_words()
        stop_words = stop_words + stopword_sastrawi + ADDITIONAL_STOPWORDS

        Logging.info("Preprocessing text data on Combined Features")
        df = df.fillna("")
        df.loc[:, COMBINED_FEATURES] = df[COMBINED_FEATURES].apply(
            lambda x: str.lower(x)
        )
        df.loc[:, COMBINED_FEATURES] = df[COMBINED_FEATURES].apply(
            lambda x: " ".join(re.findall("[\w]+", x))
        )
        df.loc[:, COMBINED_FEATURES] = df[COMBINED_FEATURES].apply(
            lambda x: " ".join(word for word in x.split() if word not in stop_words)
        )

        df[COMBINED_FEATURES] = (
            df[COMBINED_FEATURES]
            .str.split()
            .apply(lambda x: OrderedDict.fromkeys(x).keys())
            .str.join(" ")
        )
        df[COMBINED_FEATURES] = [x.split() for x in df[COMBINED_FEATURES]]
        df[COMBINED_FEATURES] = df[COMBINED_FEATURES].apply(
            lambda x: " ".join(dict.fromkeys(x).keys())
        )

        # BUILD TFIDF MATRIX
        Logging.info("Generate TF-IDF Matrix from Combined Features data")
        text_content = df[COMBINED_FEATURES]
        tfidf_df = None
        if len(text_content) > 0:
            vector = TfidfVectorizer(
                lowercase=True, use_idf=True, norm="l2", smooth_idf=True
            )
            tfidf_matrix = vector.fit_transform(text_content)

            # Transform to TFIDF Dataframe
            tfidf_df = pd.DataFrame(
                tfidf_matrix.toarray(), columns=vector.get_feature_names_out()
            )

            tfidf_df.index = df[CONTENT_ID]
        return tfidf_df

    @staticmethod
    @custom_exception()
    def calculate_cosine_similarity(list_tfidf_df):
        list_dict_similarity = []
        Logging.info("Calculating Cosine Similarity for the contents")
        for tfidf_df in list_tfidf_df:
            cs_matrix = cosine_similarity(tfidf_df)
            cs_df = pd.DataFrame(
                cs_matrix, index=tfidf_df.index, columns=tfidf_df.index
            )
            content_id_list = sorted(list(cs_df.index), reverse=False)
            list_of_similarity = []
            for content_id in content_id_list:
                cosine_similarity_series = cs_df.loc[content_id].sort_index()
                cosine_similarity_series = cosine_similarity_series.apply(
                    lambda x: float("{:.2f}".format(x))
                )
                if isinstance(cosine_similarity_series, pd.DataFrame):
                    cosine_similarity_series = cosine_similarity_series.head(1)
                    cosine_similarity_series = cosine_similarity_series.iloc[0, :]
                    cosine_similarity_series = cosine_similarity_series.sort_values(
                        ascending=False
                    )
                    cosine_similarity_series = cosine_similarity_series.drop(
                        labels=content_id
                    )
                    cosine_similarity_dict = cosine_similarity_series.to_dict()
                    list_of_similarity.append(
                        {k: v for k, v in list(cosine_similarity_dict.items())}
                    )
                else:
                    cosine_similarity_series = cosine_similarity_series.sort_values(
                        ascending=False
                    )
                    cosine_similarity_series = cosine_similarity_series.drop(
                        labels=content_id
                    )
                    cosine_similarity_dict = cosine_similarity_series.to_dict()
                    list_of_similarity.append(
                        {k: v for k, v in list(cosine_similarity_dict.items())}
                    )
            dict_similarity = dict(zip(content_id_list, list_of_similarity))
            list_dict_similarity.append(dict_similarity)
        return list_dict_similarity

    @staticmethod
    @custom_exception()
    def generate_tfidf_matrix(df_new_list):
        list_tfidf_matrix = []
        for df in df_new_list:
            tfidf_matrix = SimilarityUtils.create_tfidf_df(df)
            list_tfidf_matrix.append(tfidf_matrix)

        return list_tfidf_matrix

    @staticmethod
    @custom_exception()
    def fetch_similar_content(cs_df, content_id):
        cosine_similarity_series = cs_df.loc[content_id]
        cosine_similarity_series = cosine_similarity_series.sort_values(
            ascending=False
        )
        cosine_similarity_series = cosine_similarity_series.apply(
            lambda x: float("{:.2f}".format(x))
        )
        cosine_similarity_series = cosine_similarity_series.drop(labels=content_id)
        similarity_result = cosine_similarity_series.to_dict()

        return similarity_result

    @staticmethod
    @custom_exception()
    def calculate_single_cosine_similarity(all_content_tfidf_df):
        Logging.info("Calculating Cosine Similarity for all content")
        cs_matrix = cosine_similarity(all_content_tfidf_df)
        cs_df = pd.DataFrame(
            cs_matrix,
            index=all_content_tfidf_df.index,
            columns=all_content_tfidf_df.index,
        )
        list_of_similarity = []
        content_id_list = list(cs_df.index)
        for content_id in content_id_list:
            similarity_result = SimilarityUtils.fetch_similar_content(cs_df, content_id)
            list_of_similarity.append(similarity_result)
        dict_similarity = dict(zip(content_id_list, list_of_similarity))
        return dict_similarity
