import xgboost as xgb
from xgboost import XGBClassifier
import first
import pandas as pd
import data_io as di
from sklearn import cross_validation, metrics
from sklearn.datasets import load_svmlight_file
from sklearn.grid_search import GridSearchCV 
import matplotlib.pylab as plt
%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4