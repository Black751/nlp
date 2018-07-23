import nltk
from nltk.tokenize import PunktSentenceTokenizer

text = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'

sentences = nltk.sent_tokenize(text)

for sent in sentences:
	print(nltk.pos_tag(nltk.word_tokenize(sent)))