# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:04:43 2017

@author: Fidel
"""

import numpy as np
import matplotlib.pyplot as plt

def ridge_regression(X, y, lamda):
    n, d = X.shape
    return np.linalg.inv((X.T.dot(X)+lamda*np.eye(d))).dot(X.T).dot(y)

def error(X, y, w):
    y_predict = np.sign(X.dot(w))
    return np.sum(y!=y_predict) / y.size

def load_xy(fname):
    data = np.loadtxt(fname)
    m, _ = data.shape
    x = np.hstack((np.ones((m, 1)), data[:,:-1])) 
    y = data[:,-1:]
    return x, y

X, y = load_xy('hw4_train.html')
X_test, y_test = load_xy('hw4_test.html')

#13
w = ridge_regression(X, y, 11.26)
e_in = error(X, y, w)
e_out = error(X_test, y_test, w)
print('13#: lamda=11.26','e_in:',e_in, 'e_out:', e_out)

#14
indexs = range(2, -11, -1)
all_lamda = [10**i for i in indexs]
all_w = [ridge_regression(X, y, lamda) for lamda in all_lamda]
all_e_in = [error(X, y, w) for w in all_w]
all_e_out = [error(X_test, y_test, w) for w in all_w]
index14 = np.argmin(all_e_in)
print('14#:','index',indexs[index14], 'e_in',all_e_in[index14], 'e_out',all_e_out[index14])
plt.figure()
plt.plot(indexs, all_e_in)
plt.show()

#15
index15 = np.argmin(all_e_out)
print('15#:','index',indexs[index15], 'e_in', all_e_in[index15], 'e_out',all_e_out[index15])
plt.figure()
plt.plot(indexs, all_e_out)
plt.show()

#16
X_train, y_train = X[:120], y[:120]
X_val, y_val = X[120:], y[120:]

all_w = [ridge_regression(X_train, y_train, lamda) for lamda in all_lamda]
all_e_train = [error(X_train, y_train, w) for w in all_w]
all_e_out = [error(X_test, y_test, w) for w in all_w]
all_e_val = [error(X_val, y_val, w) for w in all_w]
index16 = np.argmin(all_e_train)
print('16#:','index', indexs[index16], 'e_train', all_e_train[index16], 'e_val',all_e_val[index16], 'e_out',all_e_out[index16])
plt.figure()
plt.plot(indexs, all_e_train)
plt.show()

#17
index17 = np.argmin(all_e_val)
print('17#:','index',indexs[index17], 'e_train',all_e_train[index17], 'e_val',all_e_val[index17], 'e_out',all_e_out[index17])
plt.figure()
plt.plot(indexs, all_e_val)
plt.show()

#18
w =  ridge_regression(X, y, 10**indexs[index17])
e_in = error(X, y, w)
e_out = error(X_test, y_test, w)
print('18#:','e_in',e_in, 'e_out',e_out)

#19

X_folds, y_folds = [], []
step = y.size // 5
for j in range(5):
    X_folds.append(X[j*step:(j+1)*step])
    y_folds.append(y[j*step:(j+1)*step])

min_e_cv = 1
all_e_cv = []
for i in range(2, -11, -1):
    lamda = 10**i
    all_e_val = []
    for j in range(5):
        X_val, y_val = X_folds[j], y_folds[j]
        del X_folds[j]
        del y_folds[j]
        X_train = np.vstack(X_folds)
        y_train = np.vstack(y_folds)
        w = ridge_regression(X_train, y_train, lamda)
        X_folds.insert(j,X_val)
        y_folds.insert(j,y_val)
        all_e_val.append(error(X_val, y_val, w))
    e_cv = np.average(all_e_val)
    all_e_cv.append(e_cv)
    if e_cv < min_e_cv:
        min_e_cv = e_cv
        min_e_cv_i = i
print('19#:','index', min_e_cv_i, 'e_cv', min_e_cv)
#20
w =  ridge_regression(X, y, 10**min_e_cv_i)
e_in = error(X, y, w)
e_out = error(X_test, y_test, w)
print('20#:','e_in', e_in, 'e_out',  e_out)