
import numpy as np
import pandas as pd

from utility import loadData
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, KFold


def tuneParameter(X, y, scoring):
    parameters = {
        'gamma': [1, 0.5, 0.1, 0.5, 0.01],
        'C': [0.1, 1, 5, 10]
    }
    grid = GridSearchCV(SVC(), param_grid=parameters, \
    cv=3, scoring=scoring, refit=scoring[0], n_jobs=12)
    grid.fit(X, y)
    columns = ['param_' + i for i in parameters] + [ 'mean_train_'+ i for i in scoring] + ['mean_test_' + i for i in scoring]
    return grid.best_estimator_, pd.DataFrame(grid.cv_results_)[columns]



def main(dataset='Iris'):
    if dataset == 'Iris':
        # Iris
        X, y = loadData('Iris')
        model, res = tuneParameter(X, y, ['accuracy'])
        print(res)
        return model, res
    else:
    # Drive
        X, y = loadData('Drive')
        model, res = tuneParameter(X, y, ['f1_micro', 'accuracy', 'f1_macro' ])
        print(res)


