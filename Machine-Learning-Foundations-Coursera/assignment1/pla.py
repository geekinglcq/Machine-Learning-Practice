# -*- coding: utf-8 -*- 

import time

import numpy as np
import pandas as pd

trainFile = './hw1_18_train.dat'
testFile = './hw1_18_test.dat'

def readData(dir='./hw1_15_train.dat'):
    data = pd.read_csv(dir, sep=' |\t', header=None, engine='python')
    data.rename(columns={data.columns[-1]:'y'}, inplace=True)
    X = data[[i for i in range(data.shape[1] - 1)]]
    X = X.assign(x0 = 1)
    return X, data['y']
    
    
def predict(x, w):
    """
    x, w are numpy array, return 1 or -1
    """
    res = x.dot(w)
    if res > 0:
        return 1
    else:
        return -1

def pla(X, y, learningRate=1.0, maxIter=1e8):
    w = np.zeros(X.shape[1])
    errors = 1
    itercnt = 0
    updates = 0
    while(errors > 0 and updates < maxIter):
        errors = 0
        itercnt += 1
        for i, row in X.iterrows():
            if predict(row, w) != y[i]:
                errors += 1
                w += learningRate * y[i] * row
                updates += 1
        
    return w, itercnt, updates

def shuffledPla(X, y, mu=1):
    updates = []
    for i in range(2000):
        if (i % 100 == 0):
            print(i)
        tX = X.sample(frac=1.0, random_state=i)
        ty = y.sample(frac=1.0, random_state=i)
        updates.append(pla(tX, y, learningRate=mu)[-1])
    return updates

def testAlg(X, y, w):
    errors = 0
    for i, r in X.iterrows():
        if predict(r, w) != y[i]:
            errors += 1
    return errors

def pocketPla(X, y, update=50, mu=1):
    w = np.zeros(X.shape[1])
    errors = testAlg(X, y, w)
    itcnt = 0

    t = int(time.time())
    while(itcnt < update):    
        if errors == 0:
            break
        tX = X.sample(frac=1.0, random_state=itcnt+t)
        ty = y.sample(frac=1.0, random_state=itcnt+t)
        tw = w
        # Run naive PLA until current w is better than pocket w
        for it, row in tX.iterrows():
            if predict(row, tw) != ty[it]:
                tw = tw + mu * ty[it] * row
                terror = testAlg(X, y, tw)
                itcnt += 1            
                if terror < errors:
    
                    w = tw
                    errors = terror
                    break

    return w
             