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
    c. for 3 word ingredients make bigrams out of them
    d. join the 2 lists together and return new overall list

"""
 
stop = stopwords.words('english') + list(string.punctuation)

# open the train json and read it into a python object
# read the data in and export the ingredient column into a list
train_df = pd.read_json('data/train.json')

print train_df.ingredients[:20]

ne = ["lads lads2 lads3 lads4 lads5", 'random strings from words', 'weird stuff']

# function that takes a string phrase, checks how many words
# if 3 or more, make bigrams out of it and append 
def long_to_ngram(string):
    ## take a string of >2 words and turn it into bigram strings
    if len(string.split()) <= 2:
        # don't do anything with strings with 2 spaces or fewer
        return string
         
    elif len(string.split()) >= 3:
        # make ngrams - list of tuples
        ngrs = list(ngrams(string.split(), 2))
        # turn into list of strings
        strings = [' '.join(pair) for pair in ngrs]
        
        return strings         

def complex_string(string):
    if len(string.split()) <= 2:
        return False
    elif len(string.split()) >= 3:
        return True
 
def simple(string):
    if len(string.split()) <= 2:
        return True
    elif len(string.split()) >= 3:
        return False

def process(list_of_ingrs):
    ## take a list of ingrs and return the same list where all >2 word ingrs 
    ## are converted into bigrams   
    
    up_to_three = filter(simple, list_of_ingrs) 
    three_or_more = filter(complex_string, list_of_ingrs)
    print up_to_three
    print three_or_more    


    return 

#    new_list = [long_to_ngram(ingr) for ingr in list_of_ingrs]
#    flat_list = [item for sublist in new_list for item in sublist if type(sublist) == list]
 #   print "Given the list of ingrs:", list_of_ingrs
  #  print "This is our list of ingredient bigrams", new_list
   # print flat_list

print process(ne)


"""
train_df['ingredients processed'] = map(process, train_df['ingredients'])
train_df.to_csv('data/raw_vs_proc_analysis.csv')

"""
