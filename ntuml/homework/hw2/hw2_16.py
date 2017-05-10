# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:08:51 2017

@author: Yi
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def generate_data(size, flips_rate):
    x = np.random.uniform(-1,1,size)
    y = np.sign(np.random.rand(size) - flips_rate) * np.sign(x)
    return x, y 
    
def compute_eout(lamda, mu):
    return lamda*mu+(1-lamda)*(1-mu)
    
def decision_stump(x , y):
    size = x.size   
    sorted_x = np.sort(x)
    pocket_err = 1
    for i in range(size-2):
        s = 1
        theta = (sorted_x[i] + sorted_x[i+1]) / 2
        y_predict = np.sign(x-theta)
        err = np.sum(y!=y_predict) / size
        if err > 0.5:
            err = 1 - err
            s = -1
        if err < pocket_err or (err==pocket_err and random.random()>0.5):
            pocket_s = s
            pocket_theta = theta
            pocket_err = err
    return pocket_s, pocket_theta, pocket_err

def multi_dimensional_decision_stump(X , y):
    m,n = X.shape
    pocket_err = 1
    for i in range(n):
        s,theta,err = decision_stump(X[:,i], y)
        if err < pocket_err or (err==pocket_err and random.random()>0.5):
            pocket_s = s
            pocket_theta = theta
            pocket_err = err
            pocket_feature = i
    return pocket_feature,pocket_s,pocket_theta,pocket_err
    
flips_rate = 0.2
lamda = 1-flips_rate
size = 20
T = 5000

#17
all_e_in=[]
all_e_out=[]
for i in range(T):
    x, y = generate_data(size,flips_rate)
    s,theta,e_in = decision_stump(x, y)
    mu = 0.5 + 0.5 * s * (abs(theta) - 1)
    e_out = compute_eout(lamda, mu)
    all_e_in.append(e_in)
    all_e_out.append(e_out)
print('#17', np.average(all_e_in))
plt.figure()
plt.hist(all_e_in)
plt.show()

#18
print('#18', np.average(all_e_out))
plt.figure()
plt.hist(all_e_out)
plt.show()

#19
data_train = np.loadtxt('hw2_train.html')
X = data_train[:,:-1]
y = data_train[:,-1]
pocket_feature,pocket_s,pocket_theta,pocket_err = multi_dimensional_decision_stump(X, y)
print('#19', pocket_err)

#20
data_test = np.loadtxt('hw2_test.html')
X_test = data_test[:,:-1]
y_test = data_test[:,-1]
m,n = X_test.shape
x_test= X_test[:,pocket_feature]
e_out = np.sum(y_test!=pocket_s*np.sign(x_test-pocket_theta)) / m
print('#20', e_out)

