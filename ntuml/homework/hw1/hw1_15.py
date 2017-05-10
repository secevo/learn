# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:37:06 2017

@author: Yi
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def sign(x):
    vfunc = np.vectorize(lambda t: 1 if t > 0 else -1)
    return vfunc(x)
    
def load_xy(fname):
    data = np.loadtxt(fname)
    m, _ = data.shape
    x = np.hstack((np.ones((m, 1)), data[:,:-1])) 
    y = data[:,-1]
    return x, y

def PLA_naive(x, y, alpha = 1.0):
    m, n = x.shape 
    w = np.zeros(n)
    steps = 0
    last_mistake = -1
    i = 0
    m_correct = 0
    while m_correct < m:
        if sign(x[i].dot(w)) != y[i]:
            m_correct = 0
            w = w + alpha*y[i]*x[i]
            steps = steps + 1
            last_mistake = i
        else:
           m_correct = m_correct + 1 
        i = i + 1 if i < m - 1 else 0 #cycle
    return w, steps, last_mistake
    
def PLA_random(x, y, alpha = 1.0):
    m, n = x.shape
    w = np.zeros(n)
    steps = 0
    indexs = np.arange(m)
    random.shuffle(indexs)
    pointer = 0
    m_correct = 0
    while m_correct < m:
        i = indexs[pointer]
        if sign(x[i].dot(w)) != y[i]:
            m_correct = 0
            w = w + alpha*y[i]*x[i]
            steps = steps + 1
        else:
           m_correct = m_correct + 1 
        pointer = pointer + 1 if pointer < m - 1 else 0
    return w, steps

if __name__ == '__main__': 
    x, y = load_xy('hw1_15_train.html')
    
    #15
    _,steps,last_mistake = PLA_naive(x, y)
    print('#15:', steps, last_mistake)
    
    #16
    T = 2000
    all_steps = [PLA_random(x, y)[1] for k in range(T)]
    print('#16', np.mean(all_steps))
    plt.figure()
    plt.hist(all_steps)
    plt.show()
    
    #17
    all_steps = [PLA_random(x, y, 0.5)[1] for k in range(T)]
    print('#17',np.mean(all_steps))
    plt.figure()
    plt.hist(all_steps)
    plt.show()