#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tfidf module

# Import Basic Module
import json, os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def dummy_fun(doc):
    return doc

class tfidf:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = sorted(data)
        self.tfidf = TfidfVectorizer(analyzer='word', tokenizer=dummy_fun, preprocessor=dummy_fun, token_pattern=None)  
        # self.tfidf = TfidfVectorizer(tokenizer=lambda x : x.split(" "), min_df=1, max_df=1)

    def getRawdata(self):
        return self.WORD_TOKEN_ALLTHREAD

    def weightTfIdf(self):
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        print("[Process] fit transform and weight all words")
        return WORD

    def getIDF(self):
        return self.tfidf.idf_

    def getVocabulary(self):
        print("[Process] Get Vocabulary")
        return self.tfidf.vocabulary_

    def getFeature(self):
        print("[Process] Get Features")
        return self.tfidf.get_feature_names()
    
    def getRank(self):
        response = self.weightTfIdf()
        feature_names = self.getFeature()
        # doc_size = 1
        doc_size = len(self.WORD_TOKEN_ALLTHREAD)
        # print("[Total] Weight size" + str(doc_size))
        WORD_TARGET_ALL = []
        for doc in range(doc_size):
            feature_index = response[doc, :].nonzero()[1]
            # print(feature_index)
            WORD_TARGET_ALL.append(sorted([[feature_names[x],[response[doc, x]]] for x in feature_index]))
            # if doc == 100 : break
        print("[Process] Get Rank of Words")
        return WORD_TARGET_ALL, 600