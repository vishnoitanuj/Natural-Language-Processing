#Form of Data processing
#Take words and take root stem of the word.
#Rid: Ride, ridding

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words = ["Python","pythoner","pythoned","pythonly","pythoning"]
# for w in example_words:
#     print(ps.stem(w))
new_text = "It is very important to be python. We all are pythoned and are pythonly."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
