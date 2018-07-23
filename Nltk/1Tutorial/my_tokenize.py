from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

# Tokenize by sentence 
sentences = sent_tokenize(text)
# Tokenize by word
words = word_tokenize(text);

print(sentences)
print (words)