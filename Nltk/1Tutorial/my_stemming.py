from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# You can end with not a word 
stemmer = PorterStemmer()

#Y You always finish with a word 
lemmatizer = WordNetLemmatizer()

print(stemmer.stem('stones'))	
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jokes'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purple'))
print('----------------------')
print(lemmatizer.lemmatize('stones'))
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa')) 
print(lemmatizer.lemmatize('purple'))