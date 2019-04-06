#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tokenize module

# Import NLP Module
# import deepcut
from pythainlp.tag import pos_tag as thai_tag
from pythainlp.util import is_thai
from pythainlp.tokenize import dict_word_tokenize
from nltk import pos_tag as eng_tag
# My Module
from ..corpus.customwords import customwords

class tokenize:
    def __init__(self, data=[]):
        self.DATA = data
        self.customwords = customwords()

    def run(self):
        customdict, statuscustom = self.customwords.target(customtype="tokenize")
        tokenwords_thai, tokenwords_eng, statusrun = [], [], 600
        # Wordcut
        try:
            for word in self.DATA:
                if isthai(word, check_all=True)['thai'] > 0:
                    # tokenword = deepcut.tokenize(word, custom_dict=customdict)
                    tokenword = dict_word_tokenize(word,customdict, engine='newmm')
                    if tokenword: tokenwords_thai += [word.replace(' ', '') for word in tokenword if word not in [' ','']]
                else: 
                    if not word.isdigit(): tokenwords_eng.append(word)
        except:
            print("[Error] Wordcut Function")
            statusrun = 601
        tokenwords_thai = set(tokenwords_thai)
        tokenwords_eng = set(tokenwords_eng)
        # POS Tag
        try:
            poswordsthai = thai_tag(tokenwords_thai, engine='artagger', corpus='orchid')
            poswordsthai_noun = [item[0] for item in poswordsthai if (item[1] == "NCMN" and item[0])]

            poswordseng = eng_tag(tokenwords_eng)
            poswordseng_noun = [item[0] for item in poswordseng if (item[1] not in ["IN"]and item[0])]
            poswords_noun = poswordsthai_noun + poswordseng_noun
        except:
            print("[Error] POS Tag Function")
            poswords_noun = tokenwords_thai + tokenwords_eng
            statusrun = 402
        tokenwords = set(poswords_noun)
        return tokenwords, statusrun


if __name__ == "__main__":
    tokenize(data=['Apple สวัสดี now has Mr.']).run()