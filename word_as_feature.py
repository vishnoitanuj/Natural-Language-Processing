import nltk
import random   #randomize training and testing data
from nltk.corpus import movie_reviews

document = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        document.append((list(movie_reviews.words(fileid)),category))
random.shuffle(document)

#print(document[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
top_words = all_words.most_common()

word_features = list(all_words.keys())[:3000]

def find_features(documents):
    words = set(documents)  #Get Unique set of elements
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev,category) in document]
