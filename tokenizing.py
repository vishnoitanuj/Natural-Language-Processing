from nltk import sent_tokenize, word_tokenize
example_text = "Hello Mr. Ram, how are you doing? Its a nice weather and Python is a great programming language!!"

for i in word_tokenize(example_text):
    print(i)
'''
for i in sent_tokenize(example_text):
    print(i)
'''
