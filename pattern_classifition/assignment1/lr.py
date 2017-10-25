
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
    cv=3, scoring=scoring, refit=scoring[0], n_jobs=4)
    grid.fit(X, y)
    columns = ['param_' + i for i in scoring] + ['mean_test_score', 'mean_train_score']
    return grid.best_estimator_, grid.cv_results_  
    return grid.best_estimator_, pd.DataFrame(grid.cv_results_)[columns]



def main(dataset='Iris'):
    if dataset == 'Iris':
        # Iris
        X, y = loadData('Iris')
        model, res = tuneParameter(X, y, ['accuracy'])
        print(res)
    else:
    # Drive
        X, y = loadData('Drive')  
        model, res = tuneParameter(X, y, ['f1_micro', 'accuracy', 'f1_macro' ])
        print(res)
    
    
