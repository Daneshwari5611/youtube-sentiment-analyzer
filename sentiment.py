# sentiment.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        score = sia.polarity_scores(comment)['compound']
        if score > 0.05:
            sentiments.append('Positive')
        elif score < -0.05:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    df = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})
    return df
