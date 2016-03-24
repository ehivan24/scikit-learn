'''
Created on Jan 18, 2015

@author: edwingsantos
'''

from __future__ import division

import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import numpy as np
from numpy.linalg import inv
from numpy import dot, transpose


x = [[6],[8],[10],[14],[18],] #diameter
y = [[7],[9],[13],[17.5],[18]] # price 

costFX = [[5],[10],[15],[20], [25]]

costFY = [[13.68],[13.68],[13.68],[13.68],[13.68]]


plt.figure()
plt.title("pizza vs price")
plt.xlabel("Diameter in")
plt.ylabel("price")
plt.plot(x, y, 'ro')

plt.plot(costFX, costFY ,'g^') 
plt.axis([0,25, 0, 25])
plt.grid(True)
#plt.show()

x = [[6],[8],[10],[14],[18]]
y = [[7],[9],[13],[17.5],[18]]

model = LinearRegression()
model.fit(x, y)
print "A 12 in pizza should const $%.2f " %model.predict([12])[0]

print 'Residual sum od the squares %.2f' % np.mean((model.predict(x) - y)**2)

print "varience ", np.var([[6],[8],[10],[14],[18]], ddof=1)

xbar = (6 + 8 + 10 + 14 + 18) /5
varience = ((6 - xbar)**2 + (8 - xbar)**2 + (10 - xbar)**2 + (14 - xbar)**2 + (18 - xbar)**2 ) / 4

print "var ", varience


xbar = (6 + 8 + 10 + 14 + 18) / 5
ybar = (7 + 9 + 13 + 17.5 + 18) / 5
cov = ((6 - xbar) * (7 - ybar) + (8 - xbar) * (9 - ybar) + (10 - xbar) * (13 - ybar) + (14 - xbar) * (17.5 - ybar) + (18 - xbar) * (18 - ybar)) / 4

print "Con ", cov
 
print "Con ", np.cov([6, 8, 10, 14, 18], [7, 9, 13, 17.5, 18])[0][1]

X = [[1, 6, 2], [1, 8, 1], [1, 10, 0], [1, 14, 2], [1, 18, 0]]
Y = [[7], [9], [13], [17.5], [18]]

print dot(inv(dot(transpose(X), X)), dot(transpose(X), Y))


print "####################################"





