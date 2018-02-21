import nltk
import random   #randomize training and testing data
from nltk.corpus import movie_reviews

document = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        document.append((list(movie_reviews.words(fileid)),category))

# document = [{(list(movie_reviews.words(fileid)),category)
# for category in movie_reviews.category()
# for fileid in movie_reviews.fileids(category)}]

random.shuffle(document)

#print(document[1])

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
print(all_words["stupid"])
