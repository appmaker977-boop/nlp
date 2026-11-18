import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("spam.csv", encoding='latin-1')

X = df['v2']
y = df['v1']

v = CountVectorizer()
X = v.fit_transform(X)

a,b,c,d = train_test_split(
    X,y,test_size=0.2,random_state=42)

m = MultinomialNB()
m.fit(a,c)

print("Accuracy:", accuracy_score(d,m.predict(b)))

msg = ["Congratulations! You won a prize"]
print("Prediction:", m.predict(v.transform(msg))[0])