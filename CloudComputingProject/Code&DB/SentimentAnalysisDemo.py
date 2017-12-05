
# coding: utf-8

# In[2]:

get_ipython().system(u'pip install --user pixiedust_twitterdemo')


# In[3]:

import pixiedust
jarPath = "https://github.com/ibm-watson-data-lab/spark.samples/raw/master/dist/streaming-twitter-assembly-1.6.jar"
pixiedust.installPackage(jarPath)


# In[4]:

get_ipython().run_cell_magic(u'scala', u'', u'import org.apache.spark.streaming._\nimport com.ibm.cds.spark.samples.StreamingTwitter\n\nval demo = com.ibm.cds.spark.samples.StreamingTwitter\ndemo.setConfig("twitter4j.oauth.consumerKey","UqkSGRGVJPgAkNiDsn7HZAl62")\ndemo.setConfig("twitter4j.oauth.consumerSecret", "rQQ8E9dq8hc3L4FbiTlvkdV1BKCg98vi09wEfACWTr2Bplt1gk")\ndemo.setConfig("twitter4j.oauth.accessToken","2416355779-3GtLUxo7UxMbQfDTKEQWQK95UN2Ib7RVC3UhD01")\ndemo.setConfig("twitter4j.oauth.accessTokenSecret", "vnjP3fvfGdTTvJkTfDOobbuHZwSGEH8yuTsViFykYXU5R")\ndemo.setConfig("watson.tone.url","https://gateway.watsonplatform.net/tone-analyzer/api")\ndemo.setConfig("watson.tone.password","MR7DViObD3IW")\ndemo.setConfig("watson.tone.username","7b5c3f47-9545-46fc-a4ef-1d421d727b31")\n\n\ndemo.startTwitterStreaming(sc, Seconds(900))')


# In[5]:

get_ipython().run_cell_magic(u'scala', u'', u'val demo = com.ibm.cds.spark.samples.StreamingTwitter\nval (__sqlContext, __df) = demo.createTwitterDataFrames(sc)')


# In[6]:

tweets=__df
tweets.count()
display(tweets)


# In[8]:

sentimentcount=[]
sentimentcount1=[]
sentimentcount2=[]
#For each sentiment, run a sql query that counts the number of tweets for which the sentiment score is greater than 50%
#Store the data in the array
for i, sentiment in enumerate(tweets.columns[-13:-8]):
    if(sentiment == "Anger"):
        sentimentcount.append(__sqlContext.sql("SELECT count(*) as sentCount FROM tweets where " +sentiment +"=Anger AND " +sentiment +">50")        .collect()[0].sentCount)
    elif(sentiment == "Joy"):
         sentimentcount1.append(__sqlContext.sql("SELECT count(*) as sentCount FROM tweets where " +sentiment +"=Joy AND " +sentiment +">50")        .collect()[0].sentCount)
    elif(sentiment == "Sadness"):
         sentimentcount2.append(__sqlContext.sql("SELECT count(*) as sentCount FROM tweets where " +sentiment +"=Sadness AND " +sentiment +">50")        .collect()[0].sentCount)
    
print (sentimentcount[0])
print (sentimentcount1[0])
print (sentimentcount2[0])


# In[23]:

get_ipython().magic(u'matplotlib inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

n_groups = 1
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.08
opacity = 0.6
 
rects1 = plt.bar(index, sentimentcount[0], bar_width,
                 alpha=opacity,
                 color='b',
                 label='Anger')
 
rects2 = plt.bar(index + 0.1 + bar_width, sentimentcount1[0], bar_width,
                 alpha=opacity,
                 color='g',
                 label='Joy')

rects3 = plt.bar(index + 0.1+ bar_width+ 0.1+ bar_width, sentimentcount2[0], bar_width,
                 alpha=opacity,
                 color='r',
                 label='Sadness')
plt.xlabel('Sentiments')
plt.ylabel('Tweet count')
plt.title('Sentiment Analysis Distribution of tweets with score > 50%',)
plt.xticks(index + bar_width, (''))
minor_ticks = np.arange(0, 1600, 300)
plt.yticks(minor_ticks)
plt.legend()
plt.tight_layout()
plt.show()


# In[ ]:



