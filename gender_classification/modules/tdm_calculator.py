# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class TDM_Calculator:

    def tokenize(self, text):
        return text.split(" ")

    def extract_features(self, df_train):
        f_corpus = " ".join(df_train[df_train.gender == 'f']['path'].values)
        m_corpus = " ".join(df_train[df_train.gender == 'm']['path'].values)
        corpus = [f_corpus, m_corpus]
        vectorizer = TfidfVectorizer(tokenizer=self.tokenize, min_df=2)
        tfidf_result = vectorizer.fit_transform(corpus)
        dense = tfidf_result.todense()
        tdm = pd.DataFrame(dense).T
        tdm.columns = ['f', 'm']
        tdm.index = vectorizer.get_feature_names()
        return tdm
