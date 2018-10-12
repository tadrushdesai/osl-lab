import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
name=input("please enter a name: ")

# Consume:
CONSUMER_KEY    = 'oJ8TiwhNzVMX6mUlUedkGx8Nh'
CONSUMER_SECRET = 'Pjllzx3EMFl3gpJh2FlyeFYhbxHsoXN3SWGj9YEuBA8SYhkRIV'

# Access:
ACCESS_TOKEN  = '913116198673432576-1GLpj0LtoetuXahit1LE60Q5JwlM2o7'
ACCESS_SECRET = 'LMu3P2wnLCXIgNZjPVgKBsvlpBtDruE03Z6jlDeNjRTkn'
# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api
	
# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name=name, count=10)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

 #We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:10]:
    print(tweet.text)
    print()

# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])
display(data.head(10))

data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
for i in range(0,10,1):
    print(tweets[i].id)
    print(tweets[i].created_at)
    print(tweets[i].source)
    print(tweets[i].favorite_count)
    print(tweets[i].retweet_count)
    print(tweets[i].geo)
    print(tweets[i].coordinates)
    print(tweets[i].entities)
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
display(data.head(10))
fav_max = np.max(data['Likes'])
rt_max  = np.max(data['RTs'])

fav = data[data.Likes == fav_max].index[0]
rt  = data[data.RTs == rt_max].index[0]

# Max FAVs:
print("The tweet with more likes is: \n{}".format(data['Tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))

# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))
tlen = pd.Series(data=data['len'].values, index=data['Date'])
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])
# Lenghts along time:
a=tlen.plot(figsize=(16,4), color='r')
b=tfav.plot(figsize=(16,4), label="Likes", legend=True)
c=tret.plot(figsize=(16,4), label="Retweets", legend=True);
sources = []
for source in data['Source']:
    if source not in sources:
        sources.append(source)

