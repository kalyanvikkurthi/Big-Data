import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
def sentiment_analysis(text):
    nltk.download("vader_lexicon")
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
    if sentiment["compound"] > 0.05:
        return "Positive"
    elif sentiment["compound"] < -0.05:
        return "Negative"
    else:
        return "Neutral"

result = input("Enter a text string: ")
print("result:", sentiment_analysis(text))