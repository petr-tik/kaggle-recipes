#!/usr/bin/env python


import nltk
import sklearn
import json
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter

with open('data/train.json', 'r') as f:
    train_json = f.read()

stop = stopwords.words('english') + list(string.punctuation)

trainset = json.loads(train_json)

df = pd.read_json('data/train.json')
all_recipes = df.ingredients.tolist()

# extract all ingridents from all cuisines into one list
all_ingr_raw = [ingr.lower() for recipe in all_recipes for ingr in recipe]
print "------------------------------------------------------\n\n"
print all_ingr_raw[:50]

# compare 2 lists for most common ingredients - raw unprocessed ingredients vs processed, where
# processed is a 1-2 word ingredients or ngrams of >=3 word ingredients

three_word_ingr = [ingr for ingr in all_ingr_raw if len(ingr.split()) > 2]
print "------------------------------------------------------\n\n"


raw_three_word_ngrams = [list(ngrams(phrase.split(),2)) for phrase in three_word_ingr]
proc_three_word_ngrams = [' '.join(pair) for sublist in raw_three_word_ngrams for pair in sublist]

print proc_three_word_ngrams[:50]

all_ingr_ngrams = [ingr for ingr in all_ingr_raw if len(ingr.split()) <= 2] + proc_three_word_ngrams
print "------------------------------------------------------\n\n"
#print all_ingr_ngrams[:50]

c1 = Counter(all_ingr_raw)    
c2 = Counter(all_ingr_ngrams)
raw_ingr_rank = c1.most_common(100)
ngrams_ingr_rank = c2.most_common(100)

print raw_ingr_rank
print ngrams_ingr_rank

