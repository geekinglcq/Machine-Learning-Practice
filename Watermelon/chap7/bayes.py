# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from math import log 
from pprint import pprint

path = './watermelon3.0.csv'
sample = {'color': 0, 'root': 0, 'sound': 0, 'texture': 0, 'navel': 0, 'touch': 0}

def loadData(path=path):
    return pd.read_csv(path)

def calContProb(data, feature, distrete=True):
    """
    Data - dataframe contain two colunms, the given feature of samples and it label
    """
    if distrete:
        return calContProbDistrete(data, feature)
    else:
        return calContProbContionous(data, feature)

def calContProbDistrete(data, feature):
    """
    Data - dataframe contain two colunms, the given feature of samples and it label
    """
    prob = pd.DataFrame(0, columns=data['label'].unique(), index=data[feature].unique())
    ni = len(data[feature].unique())
    prob = np.zeros((len(data['label'].unique()), len(data[feature].unique())) )

    for i in data['label'].unique():
        nc = len(data[data['label'] == i]) + ni
        for j in data[feature].unique():
            prob[i,j] = (len(data[data['label']==i][data[feature]==j]) + 1) / nc 

    return prob

def calContProbContionous(data, feature):
    #TODOs
    pass

def trainBayes(data):
    prob = {}
    for i in data.columns:
        if i != 'label':
            prob[i] = calContProb(pd.DataFrame(data, columns=['label', i]), i)
        else:
            temp = {}
            for j in data[i].unique():
                temp[j] = (len(data[data[i] == j]) + 1 ) / (len(data) + len(data[i].unique()))  

    return prob, data['label'].unique()

def infer(model, labels, sample):
    res = {}
    for i in labels:
        res[i] = 0
        for j in sample:
            res[i] += log(model[j][i][sample[j]])

    return res

def main():
    """
    Here we simplify the question by ignoring the continuous features. 
    """
    data = loadData(path)
    model, labels = trainBayes(data)
    result = infer(model, labels, sample)
    pprint(result)
