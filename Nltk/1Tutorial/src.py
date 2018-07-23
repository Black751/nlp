import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# Get the html code from a page : 
response = urllib.request.urlopen('http://php.net')
html = response.read()
# Clean all the text :
soup = BeautifulSoup(html, "html5lib")
# Get all the words :
text = soup.get_text(strip=True)
tokens = []
for t in text.split():
	tokens.append(t)
# Count the ocurence of each words :
freq = nltk.FreqDist(tokens)
# Remove stopwords : 
stopwords.words("english")
clean_tokens = tokens[:]
for token in tokens:
	if token in stopwords.words("english"):
		clean_tokens.remove(token)
for key, val in freq.items():
	print(str(key) + ':' + str(val))
