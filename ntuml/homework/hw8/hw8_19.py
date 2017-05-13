# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:43:04 2017

@author: Fidel
"""

import numpy as np
import matplotlib.pyplot as plt


def k_means(X, k):
    N, d = X.shape
    centres = X[np.random.choice(N, k, replace=False),:]
    converge = False
    while not converge:
        distances = np.zeros((N, k))
        for i in range(k):
            distances[:,i] = np.sum((X-centres[i])**2, axis=1)
        labels = np.argmin(distances, axis=1)
        old_centres = centres.copy()
        for i in range(k):
            centres[i] = np.mean(X[labels==i],axis=0)
        converge = (np.sum(old_centres!=centres) == 0)
        
    error = 0
    for i in range(k):
        error += np.sum((X[labels==i]-centres[i])**2)
    return centres, labels, error/N


samples = np.loadtxt('hw8_nolabel_train.html')
T = 500
k_list = [2,4,6,8,10]
e_in_list = []
for k in k_list:
    total = 0
    for i in range(T):
        total += k_means(samples, k)[2]
    e_in_list.append(total/T)
print(e_in_list)
plt.plot(k_list, e_in_list)