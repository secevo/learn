# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:56:26 2017

@author: Yi
"""

import numpy as np
import math


def lssvm(X, y,la,gamma):
    m, n = X.shape
    K = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            xi = X[i,:]
            xj = X[j,:]
            delta = xi-xj
            K[i,j] = math.exp(-gamma*np.sum(delta**2))
    beta = np.linalg.inv(la*np.eye(m)+K).dot(y)
    return beta, X          
        
def predict(beta, X, x, gamma):
    delta = X - x
    kf = np.exp(-gamma*np.sum(delta**2, axis=1))
    return beta.dot(kf)    
        
    
def error(beta, X, Xtest, y_test, gamma):
    y_predict_list = []
    for i in range(len(y_test)):
        x = Xtest[i,:]
        y_predict = predict(beta, X, x, gamma)
        y_predict_list.append(np.sign(y_predict))
    return np.sum(y_test!=np.array(y_predict_list)) / len(y_test)

data = np.loadtxt('hw2_lssvm_all.html')
X = data[:,:-1]
Y = data[:,-1]    
Xtrain = X[0:400, :]; Ytrain = Y[0:400]
Xtest = X[400:, :]; Ytest = Y[400:]

gammas = (32,2,0.125)
lamdas = (0.001,1,1000)
for gamma in gammas:
    for la in lamdas:
        beta, X = lssvm(Xtrain, Ytrain,la,gamma)
        e_in = error(beta,X,Xtrain,Ytrain,gamma)
        e_out = error(beta,X,Xtest,Ytest,gamma)
        print(gamma,la,e_in,e_out)