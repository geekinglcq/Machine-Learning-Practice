# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd
from utility import loadData

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, KFold




def tuneParameter(X, y, scoring):
    parameters = {
        'penalty': ['l1', 'l2'],
        'C': [0.1, 1, 5, 10]
    }
    grid = GridSearchCV(LogisticRegression(), param_grid=parameters, \
    cv=3, scoring=scoring, refit=scoring[0], n_jobs=12)
    grid.fit(X, y)
    columns = ['param_' + i for i in parameters] + ['mean_test_' + i, 'mean_train_'+ i for i in scoring]
    return grid.best_estimator_, pd.DataFrame(grid.cv_results_)[columns]



def main(dataset='Iris'):
    if dataset == 'Iris':
        # Iris
        X, y = loadData('Iris')
        res = tuneParameter(X, y, ['accuracy'])
        return res
        print(res)
    else:
    # Drive
        X, y = loadData('Drive')  
        return tuneParameter(X, y, ['f1_micro', 'accuracy', 'f1_macro' ])
        print(res)
    
    
