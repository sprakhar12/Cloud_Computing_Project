import csv
import numpy as np
import pandas as pd
from textblob import TextBlob
import re
from IPython.display import display
import matplotlib 
import matplotlib.pyplot as plt
import sqlite3

# SQLlite connection
conn = sqlite3.connect("Football")
cur = conn.cursor()
cur.execute("select * from patriotsvsraiders")

# List Instantiate
myList = []
Patriot_List = ['#Patriots', '#GoPats', '#Raiders', '#NEvsOAK']
myList2 = []

for i,(row) in enumerate(cur.fetchall()):
   myList.append(list(row))
del myList[-1]

for i in myList:
   for j in Patriot_List:
      if j in i[3]:
         myList2.append(i)
         
#Output total tweets
print len(myList2)

List = np.asarray(myList2)

# Using Pandas DataFrame
df = pd.DataFrame(data=[i for i in List[1:,3]], columns=['tweets'])

# Displaying only first 10 tweets for now
display(df.head(10))

print("-----------------------------")

# Sentimental Analysis over tweets
def evaluate_SentimentAnalysis(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
      
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

df['SA'] = np.array([evaluate_SentimentAnalysis(tweet) for tweet in df['tweets']])

display(df.head(10))

# Sentiment Analysis count on the basis of positve, negative and neutral tweets
# W.R.T Patriots
pos_tweets = [ tweet for index, tweet in enumerate(df['tweets']) if df['SA'][index] > 0]
neu_tweets = [ tweet for index, tweet in enumerate(df['tweets']) if df['SA'][index] == 0]
neg_tweets = [ tweet for index, tweet in enumerate(df['tweets']) if df['SA'][index] < 0]

pos_tweet_calculate = len(pos_tweets)*100/len(df['tweets'])
neu_tweet_calculate = len(neu_tweets)*100/len(df['tweets'])
neg_tweet_calculate = len(neg_tweets)*100/len(df['tweets'])

print("Percentage of positive tweets: {}%".format(pos_tweet_calculate))
print("Percentage of neutral tweets: {}%".format(neu_tweet_calculate))
print("Percentage of negative tweets: {}%".format(neg_tweet_calculate))

# Graph Plotting
n_groups = 1
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.6
 
rects1 = plt.bar(index, pos_tweet_calculate, bar_width,
                 alpha=opacity,
                 color='b',
                 label='positive')
 
rects2 = plt.bar(index + 0.1 + bar_width, neu_tweet_calculate, bar_width,
                 alpha=opacity,
                 color='g',
                 label='neutral')

rects3 = plt.bar(index + 0.1+ bar_width+ 0.1+ bar_width, neg_tweet_calculate, bar_width,
                 alpha=opacity,
                 color='r',
                 label='negative')
plt.xlabel('Sentiments')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis PatriotsvsRaiders Tweets')
plt.xticks(index + bar_width, (''))
minor_ticks = np.arange(0, 100, 20)
plt.yticks(minor_ticks)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('PatriotsVsRaiders.png')
plt.show()


