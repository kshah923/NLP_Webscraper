
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df1 = pd.read_csv(r'/Users/kshah923/Desktop/Notes/FE 595/Webscraper.csv')
df1 = df1.drop(df1.columns[[0]], axis=1)

df2 = pd.read_csv(r'/Users/kshah923/Desktop/Notes/FE 595/companies_list.csv')
df2 = df2.drop(df2.columns[[0]], axis=1)
df2 = df2.rename(columns={'0': 'Name', '1': 'Purpose'})

df3 = pd.read_csv(r'/Users/kshah923/Desktop/Notes/FE 595/HTML_Scapper_FForner.csv')
df3 = df3.drop(df3.columns[[0]], axis=1)
df3 = df3.rename(columns={'NAME_company': 'Name', 'PURPOSE_company': 'Purpose'})

df4 = pd.read_csv(r'/Users/kshah923/Desktop/Notes/FE 595/hw2.csv')

frames = [df1, df2, df3, df4]
df = pd.concat(frames, ignore_index=True)

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
