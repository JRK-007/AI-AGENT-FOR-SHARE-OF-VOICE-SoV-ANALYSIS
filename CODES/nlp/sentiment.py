from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    if not isinstance(text, str):
        return 0
    score = sia.polarity_scores(text)
    return score["compound"]
