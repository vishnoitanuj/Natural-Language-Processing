# lematizing:Synonyms
# Default of lamitization is a noun

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",'a'))
