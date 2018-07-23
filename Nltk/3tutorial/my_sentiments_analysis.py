#### NOT WORKING ###


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def word_feats(words):
	return(dict([word, True] for word in words))

# Define stop words
sw = set(stopwords.words('english'))

positive_vocab = ["awesome", "outstanding", "like", "fantastic", "terrific", "good", "nice", "great", ":)"]
negative_vocab = ["bad, terrible", "useless", "hate", ":("]
neutral_vocab = ["movie", "the", "soud", "was", "is", "actors",'did','know','words','not' ]

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)

sentence = "Awesome movie, I liked it!"

# Pre processing
words = word_tokenize(sentence)
filtred_words = []
for word in words:
	if not word in sw:
		filtred_words.append(word)
length = len(filtred_words)

for word in words:
	print(word)
# Anaysis

pos = 0
neg = 0
for word in filtred_words:
	class_result = classifier.classify(word_feats(PorterStemmer().stem(word)))
	if class_result == "neg":
		neg += 1 
	if class_result == "pos":
		pos += 1

print("Positive : " + str(float(pos) / length))
print("Negative : " + str(float(neg) / length))