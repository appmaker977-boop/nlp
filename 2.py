pip install nltk pandas scikit-learn matplotlib

A
n = int(input("Enter size: "))
a = [int(input()) for i in range(n)]

print(a.count(19) == 2 and a.count(5) >= 3)



B
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

s = "I love natural language processing"
w = [x for x in s.lower().split()
     if x not in stopwords.words('english')]

print("Unigrams:", list(ngrams(w, 1)))
print("Bigrams:", list(ngrams(w, 2)))