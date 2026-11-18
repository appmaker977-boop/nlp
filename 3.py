pip install nltk pandas scikit-learn matplotlib

A
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
import nltk

nltk.download('wordnet', quiet=True)

p = PorterStemmer()
l = LancasterStemmer()
w = WordNetLemmatizer()

words = ['playing', 'studies', 'running']

for x in words:
    print(x, p.stem(x), l.stem(x), w.lemmatize(x, 'v'))



B
import re

s = "The colors in my studyroom are blue, green, and yellow."

words = re.findall(r'[^, ]+', s)
sep = re.findall(r'[, ]+', s)

print([words, sep])