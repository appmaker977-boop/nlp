pip install nltk pandas scikit-learn matplotlib

A
import re

p = input("Enter password: ")

if (len(p) >= 8 and re.search(r'[A-Z]', p)
and re.search(r'[a-z]', p)
and re.search(r'[0-9]', p)
and re.search(r'[@#$%&*]', p)):
    print("Valid Password")
else:
    print("Invalid Password")



B
import nltk

nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

s = "The boy plays cricket"
w = nltk.pos_tag(nltk.word_tokenize(s))

print(w)

g = "NP: {<DT>?<JJ>*<NN>}"
tree = nltk.RegexpParser(g).parse(w)

print(tree)
tree.draw()