import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#Perform analytics with different languages.

from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('indian')
nltk.download('punkt')
nltk.download('vader_lexicon')

#Added additional corpora and lexicons which will accept hindi and spanish  text as well

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