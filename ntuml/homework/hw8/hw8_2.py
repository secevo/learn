# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:03:33 2017

@author: Fidel
"""

hidden = []

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        #print ("sum(%s)=%s" % (partial, target))
        hidden.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        subset_sum(numbers, target, partial + [n]) 
        
#numbers = [i+1 for i in range(36)]
#print(numbers)
N = 36
subset_sum(range(2,37),N)

maxi = 0; mini = 1000
for i in range(len(hidden)):
    num = hidden[i]
    wnum = 10 * (num[0]-1)
    for j in range(len(num)-1):
        wnum += num[j]*(num[j+1]-1)
    wnum +=  num[len(num)-1]
    if maxi < wnum:
        maxi = wnum
        max_hidden = num
    if mini > wnum:
        mini = wnum
        min_hidden = num
print('最多情况: ', maxi, max_hidden, '\n最少情况: ', mini, min_hidden)
