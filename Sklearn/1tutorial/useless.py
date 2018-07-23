from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(lowercase=True, stop_words="english")

matrix = vectorizer.fit_transform(headlines)

print(matrix.todense())

submissions['full_test'] = submissions["headlines"] + " " + submissions["url"]
full_matrix = vectorizer.fit_transform(submissions["headline"])
print(full_matrix.shape)