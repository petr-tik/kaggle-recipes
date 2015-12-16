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

# either do with pd.option_context(string_value, int): ...
# or to_string, which sorts printing in the terminal out

print "\n\n", train_df.ix[18:25].to_string(index = False), "\n\n"


# function that takes a string phrase, checks how many words
# if 3 or more, make bigrams out of it and append 
       


def process(list_of_ingrs):
    ## take a list of ingrs and 
    ## return the a flat list where all >2 word ingrs 
    ## are converted into bigrams   
    processed = []    
    for each_ingr in list_of_ingrs:
        if len(each_ingr.split()) <= 2:
            print "This is a simple ingredient string and it needs no processing", each_ingr 
            processed.append(each_ingr)

        elif len(each_ingr.split()) >= 3:
            print "{} is too long, starting to process it".format(each_ingr)
            # make ngrams - list of tuples
            ngrs = list(ngrams(each_ingr.split(), 2))
            print "This is the list of bigrams", ngrs
            # turn into list of strings
            strings = [' '.join(pair) for pair in ngrs]
            processed.extend(strings)

    return processed


train_df['ingredients processed'] = map(process, train_df['ingredients'])
train_df.to_csv('data/raw_vs_proc_analysis.csv')


