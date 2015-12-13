#!/usr/bin/env python

import nltk
import sklearn
import json
import pandas as pd
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer

"""
create a model function that takes a training set of the appropriate form and
trains a model on it. 

Create a testing function, that reads the test json and tests each model on 
i.randomised half of test json
ii. full test json
iii. full test json + additional 10% (wrt test set size) 
from original raw trainset

Train 2 separate models on raw and processed training datasets. 

test and produce a results table.

"""

train_df = df.read_json('data/train.json')
vectorizer = CountVectorizer(analyzer = 'word')
vectorizer.fit()


x_train 


# make an array of train target variables
y_train = np.array(train_df['cuisine'])
