 #!/usr/bin/env python

import nltk
import sklearn
import json
import pandas as pd
import string
import re
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
 

# open the train json and read it into a python object
train_df = pd.read_json('data/train.json')

# either do with pd.option_context(string_value, int): ...
# or to_string, which sorts printing in the terminal out

print "\n\n", train_df.ix[18:25].to_string(index = False), "\n\n"

# takes a a list of ingredient strings, 
# returns a list of lowercase, alphanumeric only strings with bigrams for all
# strings with more than 2 words 
       
def process(list_of_ingrs):
    ## take a list of ingrs and 
    ## return the a flat list where all >2 word ingrs 
    ## are converted into bigrams   
    processed = []    
    for each_ingr in list_of_ingrs:
        #  match a regexp pattern getting rid of copyright, trademark chars   
        print re.findall('\w+\w?', each_ingr)        
        # each_ingr = re.compile()        
        
        # lowercase each string
        # each_ingr = each_ingr.lower()
        if len(each_ingr.split()) <= 2:
            print "{} \nis a simple ingredient string and it needs no bigramising".format(each_ingr)
            
            

            processed.append(each_ingr)

        elif len(each_ingr.split()) >= 3:
            print "{} \n\t\tis too long\n...\nstarting to process it".format(each_ingr)
            # make ngrams - list of tuples
            ngrs = list(ngrams(each_ingr.split(), 2))
            print "This is the list of bigrams", ngrs
            # turn into list of strings
            strings = [' '.join(pair) for pair in ngrs]
            processed.extend(strings)

    return processed


train_df['ingredients bigramised'] = map(process, train_df['ingredients'])
print train_df[:30]

