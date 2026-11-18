import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon', quiet=True)

df = pd.read_csv("vaccination_tweets.csv")
sia = SentimentIntensityAnalyzer()

df['score'] = df['text'].fillna('').apply(
    lambda x: sia.polarity_scores(x)['compound'])

df['sentiment'] = df['score'].apply(
    lambda x: 'Positive' if x > 0 else
    ('Negative' if x < 0 else 'Neutral'))

print(df[['text','sentiment']].head())
print(df['sentiment'].value_counts())