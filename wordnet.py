#Wordnet : Synonyms, Antonyms and explanation to words. Like Corpus
#Basically a full dictionary
'''
The terms are based on the general sense of the words "lemma" and "synonym".

A lemma is wordnet's version of an entry in a dictionary: A word in canonical form, with a single meaning. E.g., if you wanted to look up "banks" in the dictionary, the canonical form would be "bank" and there would be separate lemmas for the nouns meaning "financial institution" and "side of the river", a separate one for the verb "to bank (on)", etc.

The term synset stands for "set of synonyms". A set of synonyms is a set of words with similar meaning, e.g. ship, skiff, canoe, kayak might all be synonyms for boat. In the nltk, a synset is in fact a set of lemmas with related meaning.
'''


from nltk.corpus import wordnet

# syns = wordnet.synsets("play")
#
# #synsets
# print(syns[0].name())
#
# #just the word
# print(syns[0].lemmas())
#
# #definition
# print(syns[0].definition())
#
# #examples
# print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        #print("l: ",l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms),'\n')
print(set(antonyms))


#Get Semantic similarity between words.
#wup: whoo and Palmer, who wrote paper for semantic similarity between words in 90's

w1 = wordnet.synset("ship.n.01") #not synsets, its for multiple words
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
