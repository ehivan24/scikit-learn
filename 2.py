'''
Created on Jan 22, 2015

@author: edwingsantos
'''

from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split, cross_val_score
import pandas as pd
import matplotlib.pylab as plt

df =  pd.read_csv('winequality-red.csv' , sep=';')
X = df[list(df.columns)[:-1]]
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X,y)

regresor = LinearRegression()
regresor.fit(X_train, y_train)
scores = cross_val_score(regresor, X, y, cv = 5)

y_predictions = regresor.predict(X_test)
print 'R-squared: ', regresor.score(X_test, y_test)

print "Scores: ", scores.mean()

print "citric acid: ", df['citric acid']


plt.scatter(df['alcohol'], df['quality'])
#plt.scatter(df['alcohol'], scores.mean())
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Vs Quality')
plt.show()

print df.describe()

