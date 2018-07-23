from sklearn.feature_extraction.text import CountVectorizer


from collections import Counter

headlines = [
    "PretzelBros, airbnb for people who like pretzels, raises $2 million",
    "Top 10 reasons why Go is better than whatever language you use.",
    "Why working at apple stole my soul (I still love it though)",
    "80 things I think you should do immediately if you use python.",
    "Show HN: carjack.me -- Uber meets GTA"
]

vectorizer = CountVectorizer(lowercase=True, stop_words="english")

matrix = vectorizer.fit_transform(headlines)

print(matrix.todense())

submissions['full_test'] = submissions["headline"] + " " + submissions["url"]
full_matrix = vectorizer.fit_transform(submissions["headline"])
print(full_matrix.shape)