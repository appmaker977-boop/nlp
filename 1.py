pip install nltk pandas scikit-learn matplotlib

A
import re

text = "Email: abc@gmail.com Date: 12/05/2026 Phone: 9876543210"

print("Email:", re.findall(r'[\w.-]+@[\w.-]+\.\w+', text))
print("Date:", re.findall(r'\d{2}/\d{2}/\d{4}', text))
print("Phone:", re.findall(r'\d{10}', text))



B
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords', quiet=True)

s = "Students are learning natural language processing"
w = s.lower().split()

print("Tokens:", w)

w = [x for x in w if x not in stopwords.words('english')]
print("Stop words removed:", w)

p = PorterStemmer()
print("Stemming:", [p.stem(x) for x in w])