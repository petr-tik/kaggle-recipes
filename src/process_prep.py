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
    a. for every list of ingredients
    b. filter every member of list if it has more than 2 spaces i.e. 3 words or not
    c. for 3 word ingredients 

"""
 
stop = stopwords.words('english') + list(string.punctuation)

# open the train json and read it into a python object
# read the data in and export the ingredient column into a list
train_df = pd.read_json('data/train.json')

print train_df



def long_to_ngram(string):
    ## take a string of >2 words and turn it into a strings of bigrams 
    



def process(list_of_ingrs):
    ## take a list of ingrs and return the same list where all >2 word ingrs 
    ## are converted into bigrams
    for ingr in list_of_ingrs:
        if len(ingr.split() > 2):
            # assign new variable
            new_ingr = ingr            
            # delete old, long ingredient
            del list_of_ingrs[ingr]
            # split the long ingr string and make a list of its bigrams            
            new_ingr = [list(ngrams(new_ingr.split(),2))]
            
    
            list_of_ingrs.append(new_ingr)



    return list_of_ingrs

three_word_ingr = [ingr for ingr in all_ingr_raw if len(ingr.split()) > 2]

# make a list of sublists of bigram tuples for each string from above 
raw_three_word_ngrams = [list(ngrams(phrase.split(),2)) for phrase in three_word_ingr]
# turn tuples into strings and flatten the list
proc_three_word_ngrams = [' '.join(pair) for sublist in raw_three_word_ngrams for pair in sublist]
# join all ingredient strings of 2 words or less with the flat list of all bigrams out of >3 word strings

