# -*- coding: utf-8 -*-
"""
Created on Fri May 12 07:50:24 2017

@author: Fidel
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

#2
X = np.array([[1, 0], [0, 1], [0, -1], [-1, 0], [0, 2], [0, -2], [-2, 0]])
Y = np.array([-1, -1, -1, 1, 1, 1, 1])
row, col = X.shape
z = np.zeros(X.shape)
z[:, 0] = X[:, 1]**2-2*X[:, 0]+3
z[:, 1] = X[:, 0]**2-2*X[:, 1]-3
pos1 = Y == -1; pos2 = Y == 1
plt.plot(z[pos1, 0], z[pos1, 1], 'x', z[pos2, 0], z[pos2, 1], 'o')
plt.show()
#l1x = [4, 4]; l1y = [-7.5, 1.5]
#l2x = [5, 5]; l2y = [-7.5, 1.5]
#plt.plot(l1x, l1y, '--',l2x, l2y, '--')

#3
clf = SVC(C=1e10, kernel='poly', degree=2, gamma=1, coef0=1, shrinking=False)
clf.fit(X, Y)
print(clf.dual_coef_, clf.intercept_, clf.support_)
