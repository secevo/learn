# -*- coding: utf-8 -*-
"""
Created on Thu May  4 20:17:19 2017

@author: Fidel
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def splitDatasSet(dataSet, feature, value):
    lSet = dataSet[dataSet[:,feature] < value]
    rSet = dataSet[dataSet[:,feature] >= value]
    return lSet, rSet

def creatTree(dataSet):
    feat, val = chooseBestSplit(dataSet)
    if feat == None: return val # leaf
    tree = {}
    tree['feat'] = feat
    tree['val'] = val
    lSet, rSet = splitDatasSet(dataSet, feat, val)
    tree['left'] = creatTree(lSet)
    tree['right'] = creatTree(rSet)
    return tree

def creatDecisionStump(dataSet):
    feat, val = chooseBestSplit(dataSet)
    stump = {}
    stump['feat'] = feat
    stump['val'] = val
    lSet, rSet = splitDatasSet(dataSet, feat, val)
    stump['left'] = classifyLeaf(lSet)
    stump['right'] = classifyLeaf(rSet)
    return stump

def classifyLeaf(dataSet):
    m = dataSet.shape[0]
    return 1 if np.sum(dataSet[:,-1] == 1) >= m / 2 else -1

def gini(dataSet):
    N = dataSet.shape[0]
    p1 = np.sum(dataSet[:,-1]==-1)/N
    p2 = np.sum(dataSet[:,-1]==1)/N
    return 1 - p1**2 - p2 ** 2

def chooseBestSplit(dataSet):
    m, n = dataSet.shape
    # all predict the same
    if np.sum(dataSet[:,-1]==-1)==m:
        return None, -1
    if np.sum(dataSet[:,-1]==1)==m:
        return None, 1

    S =  dataSet.shape[0]*gini(dataSet)

    bestS = np.Inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n-1):
        sortedVal = np.unique(dataSet[:,featIndex])
        for valIndex in range(len(sortedVal)-1):
            val = (sortedVal[valIndex] + sortedVal[valIndex+1]) / 2
            lSet, rSet = splitDatasSet(dataSet, featIndex, val)
            newS = lSet.shape[0]*gini(lSet) + rSet.shape[0]*gini(rSet)
            if newS < bestS:
                bestS = newS
                bestIndex = featIndex
                bestValue = val
    if S==bestS:# all sample the same
        return None, classifyLeaf(dataSet)
    return bestIndex, bestValue

def dt_predict(tree, x):
    p = tree
    while isinstance(p, dict) and p['feat']!=None:
        p = (p['left'] if x[p['feat']] < p['val'] else p['right'])
    else:
        return p

def bagging(dataSet):
    m, n = dataSet.shape
    bag = []
    for i in range(m):
        index = random.randint(0,m-1)
        bag.append(dataSet[index,:])
    return np.array(bag)

def creatRandomForest(dataSet, T):
    rf = []
    for i in range(T):
        bag = bagging(dataSet)
        tree = creatTree(bag)
        rf.append(tree)
    return rf

def creatRandomForest_prune(dataSet, T):
    rf = []
    for i in range(T):
        bag = bagging(dataSet)
        tree = creatDecisionStump(bag)
        rf.append(tree)
    return rf

def rf_predict(rf, x):
    count = 0
    for tree in rf:
        p = dt_predict(tree, x)
        if p==1:
            count=count+1
    if count>len(rf)/2:
        return 1
    return -1

def dt_error(tree, dataSet):
    m, n = dataSet.shape
    count=0
    for i in range(m):
        x = dataSet[i,:-1]
        if dt_predict(tree, x)!=dataSet[i,-1]:
             count = count+1
    return count/m

def rf_error(rf, dataSet):
    m, _ = dataSet.shape
    count=0
    for i in range(m):
        x = dataSet[i,:-1]
        if rf_predict(rf, x)!=dataSet[i,-1]:
             count = count+1
    return count/m

def rf_error_accumulative(rf, dataSet):
    m, _ = dataSet.shape
    error_list = []
    count_list = np.zeros(m)
    for k in range(len(rf)):
        tree = rf[k]
        for i in range(m):
            x = dataSet[i,:-1]
            p = dt_predict(tree, x)
            if p==1:
                count_list[i] = count_list[i]+1
        error = np.sum(np.where(count_list > k/2, 1, -1)!= dataSet[:,-1]) / m
        error_list.append(error)
    return error_list

trainSet = np.loadtxt('hw7_train.html')
tree = creatTree(trainSet)
print('#13 tree:', tree)
print('#14 e_in:', dt_error(tree, trainSet))

testSet = np.loadtxt('hw7_test.html')
print('#15 e_out:', dt_error(tree, testSet))

T = 30000
rf = creatRandomForest(trainSet, T)
e_in_list=[]
for tree in rf:
    e_in = dt_error(tree, trainSet)
    e_in_list.append(e_in)
print('#16 e_in_gt:', np.mean(e_in_list))
plt.figure()
plt.hist(e_in_list)
plt.show()

e_in_Gt_list=rf_error_accumulative(rf, trainSet)
print('#17 e_in_Gt:', e_in_Gt_list[-1])
plt.figure()
plt.plot(e_in_Gt_list)
plt.show()

e_out_Gt_list=rf_error_accumulative(rf, testSet)
print('#18 e_out_Gt:', e_out_Gt_list[-1])
plt.figure()
plt.plot(e_out_Gt_list)
plt.show()

rf_prune = creatRandomForest_prune(trainSet, T)
e_in_Gt_list=rf_error_accumulative(rf_prune, trainSet)
print('#19 e_in_Gt:', e_in_Gt_list[-1])
plt.figure()
plt.plot(e_in_Gt_list)
plt.show()

e_out_list=rf_error_accumulative(rf_prune, testSet)
print('#20 e_out_Gt:', e_out_list[-1])
plt.figure()
plt.plot(e_out_list)
plt.show()
