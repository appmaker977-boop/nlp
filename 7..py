pip install nltk pandas scikit-learn matplotlib

A
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('wordnet', quiet=True)

s = "The boys are playing games"
w = nltk.pos_tag(nltk.word_tokenize(s))
l = WordNetLemmatizer()

for x,p in w:
    pos = 'v' if p.startswith('V') else 'n'
    print(x, "->", l.lemmatize(x, pos))



B
from nltk.util import ngrams
from collections import Counter

docs = ["I love NLP", "I love Python", "NLP is easy"]

b = []
for d in docs:
    b += list(ngrams(d.lower().split(), 2))

f = Counter(b)

print("Total Bigrams:", len(b))
print("Unique Bigrams:", len(f))
print("Top 5:", f.most_common(5))