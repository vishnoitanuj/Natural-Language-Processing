from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = "This is an example of stop word filterartion."
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)

filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)
