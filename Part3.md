# Report

I found the Sentiment Analysis for the 200 companies 
using both TextBlob and VADER. The TextBlob Scores test
for subjectivity and polarity. Subjectivity measures text
based on its influence of opinion, scoring from 1 being
the most subjective to 0 being the least. I found polarity
to be more useful for my use case as it measures how positive
or negative the overall sentence is from [-1, 1]. I found that
my TextBlob sentiment analysis is very uniform in its rankings
which makes sense as the purpose is being randomly generated.
The highest value was 0.5 while the lowest was -0.6. Words like
static, rich, advanced were contributed to positive sentiment while
reciprocal and didactic were contributed to negative.

I noticed that the sentiment score included a lot of 0's so I 
was a bit skeptical. Therefore, I also tested with the VADER 
Sentiment Analysis. VADER provides users with a positive score,
negative score, and a compounded score. I decided to use the compounded
score for this test. These values were a lot more diverse and 
I believe that is contributed to Vader's advanced Sentiment word
dictionary/rankings. The highest rank was a score of 0.7783 and
included words like innovate & rich. The lowest score was -0.6486
with words like "killer". A majority of the negative sentiment
included the word killer. 
