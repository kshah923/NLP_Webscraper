
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Part 1 - Ingesting Results and printing a single file with all results together (see main.py)

df = pd.read_csv(r'/Users/kshah923/Desktop/Notes/FE 595/200companies.csv')

# Part 2 - using VaderSentiment to analyze the 200 company's purposes by sentiment

analyzer = SentimentIntensityAnalyzer()
sentiment = pd.DataFrame([], columns=['Sentiment'])

for i in range(200):
    x = df["Purpose"][i]
    y = analyzer.polarity_scores(x)
    z = y['compound']

    sentiment = sentiment.append({'Sentiment': z}, ignore_index=True)

df = df.join(sentiment)
top10 = df.sort_values(["Sentiment"], ascending=False)
bottom10 = df.sort_values(["Sentiment"])

print("TOP 10", top10.head(10))
print("BOTTOM 10", bottom10.head(10))

final = pd.DataFrame([])
final = final.append(top10.head(10))
final = final.append(pd.Series(), ignore_index=True)
final = final.append(bottom10.head(10), ignore_index=True)

# final.to_csv('VADER_Sentiment.csv')
