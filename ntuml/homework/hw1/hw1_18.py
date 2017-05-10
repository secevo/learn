# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:23:46 2017

@author: Yi
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import hw1_15

def test(x, y, w):
    return np.sum(y!=hw1_15.sign(x.dot(w))) / len(y)

def PLA_pocket(x, y, updates=50):
    m, n = x.shape
    w = np.zeros(n)
    pocket_w = w.copy()
    pocket_error = test(x ,y, w)
    indexs = np.arange(m)
    for t in range(updates):
        mistakes = indexs[y!=hw1_15.sign(x.dot(w))]
        if mistakes.size == 0: break
        i = random.choice(mistakes)
        w = w + y[i]*x[i]
        error = test(x ,y, w)
        if error < pocket_error:
            pocket_w = w
            pocket_error = error
    return pocket_w

def PLA_fixed(x, y, updates=50):
    m, n = x.shape
    w = np.zeros(n)
    indexs = np.arange(m)
    for t in range(updates):
        mistakes = indexs[y!=hw1_15.sign(x.dot(w))]
        if mistakes.size == 0: break
        i = random.choice(mistakes)
        w = w + y[i]*x[i]
    return w

if __name__ == '__main__': 
    x, y = hw1_15.load_xy('hw1_18_train.html')
    x_test, y_test = hw1_15.load_xy('hw1_18_test.html')
    
    #18
    T = 200
    all_errors=[]
    for i in range(T):
        w = PLA_pocket(x, y)
        error = test(x_test, y_test, w)
        all_errors.append(error)
    print('#18', np.mean(all_errors))
    plt.figure()
    plt.hist(all_errors)
    plt.show()
    
    #19
    all_errors=[]
    for i in range(T):
        w = PLA_fixed(x, y)
        error = test(x_test, y_test, w)
        all_errors.append(error)
    print('#19',np.mean(all_errors))
    plt.figure()
    plt.hist(all_errors)
    plt.show()
    
    #20
    all_errors=[]
    for i in range(T):
        w = PLA_pocket(x, y, 100)
        error = test(x_test, y_test, w)
        all_errors.append(error)
    print('#20',np.mean(all_errors))
    plt.figure()
    plt.hist(all_errors)
    plt.show()