#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import json
import sklearn
from collections import Counter

with open('data/train.json', 'r') as f:
    train_json = f.read()

trainset = json.loads(train_json)

df = pd.read_json('data/train.json')

cuisines = sorted(list(pd.unique(df.cuisine)))


def get_info(df, cuisine):
    # input df and kind of cuisine (to be iterated over)
    # output: number of recipes for that kind, num of all ingredients, 
    # number of unique ingredients, ranking of the most popular ingr, 
    # ingre per recipe, st.dev
    df_examine = df[df.cuisine == cuisine] # take just the columns for that cuisine

    # how many recipes for each cuisine    
    num_recipes = len(df_examine.index)
    
    all_recipes = df_examine['ingredients'].tolist()
    all_ingr_flat = [ingr.lower() for recipe in all_recipes for ingr in recipe]
    c = Counter(all_ingr_flat)    
    ingr_rank = c.most_common(100)
    
    print "{} cuisine: {} recipes using {} ingredients.\n\taverage num of ingredients per recipe: {}".format(cuisine, num_recipes, 
                        len(all_ingr_flat), float(len(all_ingr_flat)/num_recipes))
    print ingr_rank

for x in cuisines:
    get_info(df, x)

