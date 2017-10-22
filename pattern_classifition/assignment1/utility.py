# -*- coding: utf-8 -*- 

import json
import codecs

import numpy as numpy
import pandas as pd 

iris_path = './data/iris.data'
adult_train_path = './data/adult.data'
adult_test_path = './data/adult.test'
drive_path = './data/Sensorless_drive_diagnosis.txt'
def loadData(dataName='Iris'):
    if dataName not in ['Iris', 'Adult', 'Drive']:
        print("Data name must be one of 'Iris', 'Adult', 'Drive' ")
        return pd.DataFrame()
    if dataName == 'Iris':
        data = pd.read_csv(iris_path, names=['f1','f2','f3','f4','label'])
        data['label'] = pd.Categorical(data['label']).codes
        X = data[data.columns.drop('label')]
        y = data['label']
        return X, y 
    if dataName == 'Adult':
        cateFeature = ['work', 'education', 'marriage', 'occupation', 'relation', 'race', 'sex', 'native-country', 'label']
        train = pd.read_csv(adult_train_path, names=['age', 'work','fnlwgt','education','edu_num','marriage','occupation'\
        'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','label'])
        test = pd.read_csv(adult_test_path, names=['age', 'work','fnlwgt','education','edu_num','marriage','occupation'\
        'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','label'])
        data = pd.concat([train, test])
        for i in cateFeature:
            data[i] = pd.Categorical(data[i]).codes
        X = data[data.coulmns.drip('label')]
        y = data[label]
        return X, y
    if dataName == 'Drive':
        data = pd.read_csv(drive_path, sep=' ', names=['f' + str(i) for i in range(48)] + ['label'])
        data['label'] = pd.Categorical(data['label']).codes
        X = data[data.columns.drop('label')]
        y = data['label']
        return X, y 
        