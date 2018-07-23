from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stop_words = set(stopwords.words('english'))
words = word_tokenize(data)
word_filtered = []

for w in words:
	if w not in stop_words:
		word_filtered.append(w)

print(word_filtered)
