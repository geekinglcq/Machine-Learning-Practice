import xgboost as xgb
from xgboost import XGBClassifier
import pandas as pd
from utility import loadData
from sklearn import cross_validation, metrics
from sklearn.datasets import load_svmlight_file
from sklearn.grid_search import GridSearchCV 


def modelfit(alg, X, y,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(X, y)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
            metrics='auc', early_stopping_rounds=early_stopping_rounds)
        alg.set_params(n_estimators=cvresult.shape[0])

    #Fit the algorithm on the data
    alg.fit(X, y,eval_metric='error')

    #Predict training set:
    dtrain_predictions = alg.predict(X)
    dtrain_predprob = alg.predict_proba(X)[:,1]

    #Print model report:
    print("\nModel Report")
    print("Accuracy : %.4g" % metrics.accuracy_score(y, dtrain_predictions))
    print("AUC Score (Train): %f" % metrics.roc_auc_score(y, dtrain_predprob))

def tuneParameter(X, y, scoring, parameters):
    grid = GridSearchCV(XGBClassifier(), param_grid=parameters, \
    cv=3, scoring=scoring[0], refit=scoring[0], n_jobs=12)
    grid.fit(X, y)
    columns = ['param_' + i for i in parameters] + [ 'mean_train_'+ i for i in scoring] + ['mean_test_' + i for i in scoring]
    return grid.best_estimator_, grid.grid_scores_


def format(para):
    for k, v in para.items():
        if type(v) != list:
            para[k] = [v]
    return para

def main(dataset='Iris'):
    parameters = [{
        'gamma': [0, 0.2, 0.4, 0.6, 0.8],
    },{
        'subsample':[0, 0.5, 0.8],
        'reg_alpha':[0.01, 0.1, 1]
    },{
        'max_depth': [3 ,5 ,7, 9],
        'min_child_weight': [1, 3 ,5],
      
    }]
    if dataset == 'Iris':
        # Iris
        X, y = loadData('Iris')
        model,res =tuneParameter(X, y, ['accuracy'], parameters[0])
        para = format(model.get_params())
        para.update(parameters[1])
        print('a')
        model, res2 = tuneParameter(X, y, ['accuracy'], para)
        para = format(model.get_params())
        print('b')
        para.update(parameters[2])
        model, res3 = tuneParameter(X, y, ['accuracy'], para)
        return model, [res, res2, res3]
        
    else:
    # Drive
        if dataset == 'Drive':
            X, y = loadData('Drive')  
        else:
            X, y = loadData('Adult')
        model,res =tuneParameter(X, y, ['accuracy'], parameters[0])
        para = format(model.get_params())
        para.update(parameters[1])
        model, res2 = tuneParameter(X, y, ['f1_macro'], para)
        para = format(model.get_params())
        para.update(parameters[2])
        model, res3 = tuneParameter(X, y, ['f1_macro'], para)
        return model, [res, res2, res3]
