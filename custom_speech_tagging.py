import nltk.tokenize.punkt
import pickle
import codecs
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
text = codecs.open("test.txt","r","utf8").read()
tokenizer.train(text)
out = open("someplain.pk","wb")
pickle.dump(tokenizer, out)
out.close()
