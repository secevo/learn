# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:01:27 2017

@author: Yi
"""

import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

def load_data(fname):
    data = np.loadtxt(fname)
    X = data[:,1:]
    y = data[:,0]
    return X, y

def error(y_preditc, y):
    return np.sum(y_preditc!=y) / len(y);

X, y = load_data('features.train')
X_test, y_test = load_data('features.test')
y0 = np.where(y==0, 1 ,-1)
y8 = np.where(y==8, 1 ,0)

all_dw = []
logCs = (-6,-4,-2,0,2)
for logC in logCs:
    C = 10**logC
    clf = svm.SVC(C=C, kernel='linear',shrinking=False)    
    clf.fit(X ,y0)
    w = clf.coef_
    dw = np.linalg.norm(w)
    all_dw.append(dw)
    
print('#15:', all_dw)
plt.figure()
plt.plot(logCs, all_dw)
plt.show()

all_e_in=[]
all_sum_alpha=[]
logCs = (-6,-4,-2, 0, 2)
for logC in logCs:
    C = 10**logC
    poly_clf = svm.SVC(C=C, kernel='poly', degree=2, gamma=1, coef0=1, shrinking=False)
    poly_clf.fit(X, y8)
    y_predict = poly_clf.predict(X)
    e_in = error(y_predict, y8)
    sum_alpha = np.sum(np.abs(poly_clf.dual_coef_)) #dual_coef_ = alpha * y
    all_e_in.append(e_in)
    all_sum_alpha.append(sum_alpha)

print('#16:', all_e_in)
plt.figure()
plt.plot(logCs, all_e_in)
plt.show()

print('#17:', all_sum_alpha)
plt.figure()
plt.plot(logCs, all_sum_alpha)
plt.show()

'''
print('#18:')
all_d = []
logCs = (-3, -2,-1,0,1)
for logC in logCs:
    C = 10**logC
    rbf_clf = svm.SVC(C=C, kernel='rbf',shrinking=False, gamma=100)    
    rbf_clf.fit(X ,y0)
    alphas = np.abs(rbf_clf.dual_coef_)    
    for i in range(rbf_clf.dual_coef_.size):
        alpha = alphas[0,i]
        if alpha<C and alpha > 0:
            x = rbf_clf.support_vectors_[i].reshape(1, -1)
            decision_value = rbf_clf.decision_function(x)[0]
            #how to compute w?
            #  |w|^2 = alpha^T * K * alpha
            # d = decision_value / |w|
            d = decision_value / 1
            all_d.append(d)
            break
print(all_d)
plt.figure()
plt.plot(logCs, all_d)
plt.show()
'''    
    
print('#19:')
all_e_out = []
y0_test = np.where(y_test==0, 1 ,-1)
log_gammas = (0,1,2,3,4)
for log_gamma in log_gammas:
    gamma = 10 ** log_gamma
    rbf_clf = svm.SVC(C=0.1, kernel='rbf',shrinking=False, gamma=gamma)    
    rbf_clf.fit(X ,y0)
    y0_test_predict = rbf_clf.predict(X_test)
    e_out = error(y0_test_predict, y0_test)
    all_e_out.append(e_out)
print('#19:', all_e_out)
plt.figure()
plt.plot(log_gammas, all_e_out)
plt.show()

all_e_val =[]
log_gammas = (0,1,2,3,4)
for log_gamma in log_gammas:
    gamma = 10 ** log_gamma
    rbf_clf = svm.SVC(C=0.1, kernel='rbf',shrinking=False, gamma=gamma)
    errors=[]
    for i in range(100):
        indexs = np.random.permutation(y.size)
        X_val = X[indexs[0:1000],:]
        y_val = y0[indexs[0:1000]]
        X_train = X[indexs[1000:],:]
        y_train = y0[indexs[1000:]]
        rbf_clf.fit(X_train, y_train)
        y_predict =rbf_clf.predict(X_val)
        errors.append(error(y_predict, y_val))
    all_e_val.append(np.mean(errors))
print('#20:', all_e_val)
plt.figure()
plt.plot(log_gammas, all_e_val)
plt.show()