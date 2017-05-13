# -*- coding: utf-8 -*-
"""
Created on Mon May  8 08:02:07 2017

@author: Fidel
"""
import numpy as np
import heapq
import matplotlib.pyplot as plt

def k_nbor(samples, k, x):
    knn = heapq.nsmallest(k, samples, key=lambda sample: np.sum((sample[:-1]-x)**2))
    return np.sign(np.sum(np.array(knn)[:,-1]))

def uniform(samples, gamma, x):
    return np.sign(np.sum(samples[:,-1]*np.exp(-gamma*np.sum((samples[:,:-1]-x)**2,axis=1))))

def error(samples, k, tests,func):
    count = 0
    for test in tests:
        preditc = func(samples,k,test[:-1])
        if preditc!=test[-1]:
            count = count + 1
    return count/len(tests)

samples = np.loadtxt('hw8_train.html')
tests = np.loadtxt('hw8_test.html')

k_list = [1,3,5,7,9]

e_in_list = []
for k in k_list:
    e_in = error(samples, k, samples,k_nbor)
    e_in_list.append(e_in)
print(e_in_list)
plt.figure()
plt.plot(k_list,e_in_list)
plt.show()

e_out_list = []
for k in k_list:
    e_out = error(samples, k, tests,k_nbor)
    e_out_list.append(e_out)
print(e_out_list)
plt.figure()
plt.plot(k_list,e_out_list)
plt.show()

gamma_list = [0.001,0.1,1,10,100]

e_in_list = []
for gamma in gamma_list:
    e_in = error(samples, gamma, samples,uniform)
    e_in_list.append(e_in)
print(e_in_list)
plt.figure()
plt.plot(gamma_list,e_in_list)
plt.show()

e_out_list = []
for gamma in gamma_list:
    e_out = error(samples, gamma, tests,uniform)
    e_out_list.append(e_out)
print(e_out_list)
plt.figure()
plt.plot(gamma_list,e_out_list)
plt.show()


