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
from sklearn.feature_extraction import text

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



