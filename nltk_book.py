'''
Created on Jan 26, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass
import nltk 
#nltk.download() # used onece to download all the corpus


from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer


from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print lemmatizer.lemmatize('gathering', 'v')
print lemmatizer.lemmatize('gathering', 'n')


print stemmer.stem('gathering')

wordnet_tags = ['n', 'v']

corpus = [
          'He ate the sandwiches',
          'Every sandwich was eaten by him'
          ]

stemmer = PorterStemmer()

print 'Stemmed: ', [[stemmer.stem(token) for token in word_tokenize(document)] for document in corpus]

def lemmatize(token, tag):
    if tag[0].lower in ['n', 'v']:
        return lemmatizer.lemmatize(token, tag[0].lower())
    return token

lemmatizer = WordNetLemmatizer()
tagged_corpus = [pos_tag(word_tokenize(document)) for document in corpus ]

print 'Lemmatized: ', [[lemmatize(token, tag) for token, tag in document] for document in tagged_corpus]

print "\n\n####################################\n\n"

from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The dog ate a sandwich, the wizard transfigured a sandwich, and I ate a sandwich']

vectorize  = CountVectorizer(stop_words='english')

print vectorize.fit_transform(corpus).todense()


print "####################################\n\n"

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['The dog ate a sandwich, , and I ate a sandwich',
          'the wizard transfigured a sandwich']

vectorize =  TfidfVectorizer(stop_words='english')
print vectorize.fit_transform(corpus).todense()

print "####################################\n\n"


from sklearn.feature_extraction.text import HashingVectorizer

corpus = ['the', 'ate', 'bacon', 'cat']

vectorizer = HashingVectorizer(n_features=6)
print vectorizer.transform(corpus).todense()




