'''
Created on Jan 25, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

onehot_encoder = DictVectorizer()
vectonizer = CountVectorizer()

instances = [{'city': "New Yotk" },{'city': 'San Francisco'},{'city': 'Chapell hill'} ]

print onehot_encoder.fit_transform(instances).toarray()

print "\n\n\n"

corpus = [
       'UNC played Duke in basketball',
       'Duke lost the basketball game',
       'I ate a sandwich'
        ]


print vectonizer.fit_transform(corpus).todense()
print vectonizer.vocabulary_


print "\n\n\n"

counts = [[0, 1, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0]
          ]

print "Distance between 1 and 2 ", euclidean_distances(counts[0], counts[1])
print "Distance between 1 and 3 ", euclidean_distances(counts[0], counts[2])
print "Distance between 2 and 3 ", euclidean_distances(counts[1], counts[2])

