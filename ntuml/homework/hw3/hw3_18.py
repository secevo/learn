# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:58:13 2017

@author: Yi
"""

import numpy as np

def sigmoid(s):
    return 1.0 / (1 + np.exp(-s))

def sgd_lr(X ,y, alpha, T):    
    N, d = X.shape    
    w = np.zeros(d)
    for i in range(T):
        n = i % N
        Xn = X[n]
        yn = y[n]
        w = w + alpha*sigmoid(-yn*Xn.dot(w))*(yn*Xn)
    return w

def gd_lr(X ,y, alpha, T):    
    N, d = X.shape    
    w = np.zeros(d)
    for i in range(T):
        delta = np.mean((sigmoid(-y*X.dot(w))*(-y)).reshape(N,1)*X, axis = 0)
        w = w - alpha*delta
    return w

def error(X, y, w):
    N, _ = X.shape
    return np.sum(np.sign(X_test.dot(w))!=y_test) / N
    
data = np.loadtxt('hw3_train.html')
X = data[:,:-1]
y = data[:,-1]
data2 = np.loadtxt('hw3_test.html')
X_test = data2[:,:-1]
y_test = data2[:,-1]
N, _ = X_test.shape

w1 = gd_lr(X, y, 0.001, 2000)
print('#18', w1,error(X_test, y_test, w1))

w2 = gd_lr(X, y, 0.01, 2000)
print('#19', w2,error(X_test, y_test, w2))

w3 = sgd_lr(X, y, 0.001, 2000)
print('#20', w3,error(X_test, y_test, w3))