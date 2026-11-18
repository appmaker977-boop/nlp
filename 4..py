pip install nltk pandas scikit-learn matplotlib

A
import re

s = input("Enter sheep talk: ")

if re.fullmatch(r'baa+', s):
    print("Accepted")
else:
    print("Rejected")



B
import nltk

s = "The little boy plays cricket"
w = nltk.pos_tag(nltk.word_tokenize(s))

g = "NP: {<DT>?<JJ>*<NN>}"
p = nltk.RegexpParser(g)

print(p.parse(w))