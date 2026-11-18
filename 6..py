pip install nltk pandas scikit-learn matplotlib

A
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('vader_lexicon', quiet=True)

s = "The movie is good and beautiful"
w = nltk.pos_tag(nltk.word_tokenize(s))

n = [x for x,p in w if p.startswith('NN')]
a = [x for x,p in w if p.startswith('JJ')]

print("Nouns:", n)
print("Adjectives:", a)

sia = SentimentIntensityAnalyzer()
print("Sentiment:", sia.polarity_scores(' '.join(a)))



B
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords', quiet=True)

s = "Python is easy and Python is powerful"
w = [x for x in s.lower().split()
     if x.isalpha() and x not in stopwords.words('english')]

f = Counter(w)

print(f)
plt.bar(f.keys(), f.values())
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()