# Kevin Shah
# Assignment 3
# April 5, 2021

import pandas as pd
from textblob import TextBlob

# Part 1 - Ingesting Results and printing a single file with all results together

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
print(df)
# df.to_csv('200companies.csv')

# Part 2 - using TextBlob to analyze the 200 company's purposes by sentiment

sentiment = pd.DataFrame([], columns=['Sentiment'])

if __name__ == "__main__":
    for i in range(200):
        x = df["Purpose"][i]
        y = TextBlob(x).sentiment.polarity

        sentiment = sentiment.append({'Sentiment': y}, ignore_index=True)

df = df.join(sentiment)
top10 = df.sort_values(["Sentiment"], ascending=False)
bottom10 = df.sort_values(["Sentiment"])

print("TOP 10", top10.head(10))
print("BOTTOM 10", bottom10.head(10))

final = pd.DataFrame([])
final = final.append(top10.head(10))
final = final.append(pd.Series(), ignore_index=True)
final = final.append(bottom10.head(10), ignore_index=True)

# final.to_csv('TextBlob_Sentiment.csv')
