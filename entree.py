"""
# Data Science 1 Project: Rule Mining
by Lily Djami
"""

import os
import pandas as pd

def prepare_entree_dataset():
    dir = "./datasets/entree/data/"
    cols = [i for i in range(0, 2)]
    data = []
    for file in os.listdir(dir):
        if file.endswith(".txt") and file!="features.txt":
            #print(file)
            df = pd.read_csv(dir+file, sep='\t', names=cols, engine='python')
            #print(df)
            data.append(df)
    
    res = pd.concat(data)
    res = res.drop([0], axis=1)
    res.to_csv("datasets\entree\entree.csv", sep=" ", index=False)
    
def read_entree_dataset():
    dir = "./datasets/entree/"
    cols = [i for i in range(0, 30)]
    res = pd.read_csv(dir+"entree.csv", sep=" ", names=cols, engine='python')
    res.fillna("-", inplace=True)
    res.applymap(str)
    return res
