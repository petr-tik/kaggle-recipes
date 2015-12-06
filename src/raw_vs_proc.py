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
from collections import OrderedDict



"""
if raw strings are counted separately 'ground black pepper' and 'black pepper' 
will have different counts and it won't correctly represent 
the distribution of ingredients

here 2 ingredient lists are compared: 
1. the original with arbitrarily long ingredient string


2. processed ingredient list 
    where all >=2 word ingredients 'black pepper', 'kosher salt' are untouched
    but all >2 word ingredients are turned into bigrams, so that
    'ground black pepper' -> 'ground black' and 'black pepper'
    this way 'black pepper' instances inside long strings will be counted together with >2 word strings
    
    to process:
    a. first, make a list of >2 word ingr strings from the all_ingredient list
    b. process the >2 word strings by making bigrams out of them
    c. create a processed list with raw =<2 word ingr strings and bigrams from >2 word ingr strings


"""

with open('data/train.json', 'r') as f:
    train_json = f.read()

stop = stopwords.words('english') + list(string.punctuation)

trainset = json.loads(train_json)
# read the data in and export the ingredient column into a list
df = pd.read_json('data/train.json')
all_recipes = df.ingredients.tolist()

# extract all ingridents from all cuisines into one flat list
all_ingr_raw = [ingr.lower() for recipe in all_recipes for ingr in recipe]

# compare 2 lists for most common ingredients - raw unprocessed ingredients vs processed, where
# processed is a 1-2 word ingredients or ngrams of >=3 word ingredients

# take all ingredient strings that have more than 2 whitespaces in them i.e. 3 words
three_word_ingr = [ingr for ingr in all_ingr_raw if len(ingr.split()) > 2]

# make a list of sublists of bigram tuples for each string from above 
raw_three_word_ngrams = [list(ngrams(phrase.split(),2)) for phrase in three_word_ingr]
# turn tuples into strings and flatten the list
proc_three_word_ngrams = [' '.join(pair) for sublist in raw_three_word_ngrams for pair in sublist]
# join all ingredient strings of 2 words or less with the flat list of all bigrams out of >3 word strings
all_ingr_ngrams = [ingr for ingr in all_ingr_raw if len(ingr.split()) <= 2] + proc_three_word_ngrams

# return a sorted (descending in count) set of tuples (ingredient, count)
count_ingr_raw = Counter(all_ingr_raw).most_common()
count_ingr_ngrams = Counter(all_ingr_ngrams).most_common()


#, 'count in processed', 'delta'
df_raw = pd.DataFrame.from_records(count_ingr_raw, columns = ['ingredient', 'count in raw'])

df_proc = pd.DataFrame.from_records(count_ingr_ngrams, columns = ['ingredient', 'count in processed'])

mer_df = pd.merge(df_raw, df_proc, on = 'ingredient', how='outer')

mer_df['absolute difference'] = mer_df['count in processed'] - mer_df['count in raw']

mer_df = mer_df.sort_values(by = 'absolute difference', ascending = False)

mer_df.to_csv('data/raw_vs_proc.csv', encoding = 'utf-8')
