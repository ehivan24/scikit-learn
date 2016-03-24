'''
Created on Feb 25, 2015

@author: edwingsantos
'''


import numpy as np
import matplotlib as plt
from sklearn import datasets, svm
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


dataSet = datasets.load_iris()

model = svm.SVC(gamma=0.001)

model.fit(dataSet.data, dataSet.target)

expected = dataSet.target
predicted = model.predict(dataSet.data)

print metrics.classification_report(expected, predicted)
print metrics.confusion_matrix(expected, predicted)


if __name__ == '__main__':
    pass