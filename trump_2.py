import tweepy
import pandas as pd
import matplotlib.pyplot as plt
#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Make the graphs prettier
pd.set_option('display.mpl_style', 'default')

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET ='xxxx'
OAUTH_TOKEN = 'xxxx'
OAUTH_TOKEN_SECRET = 'xxxx'


#Use tweepy.OAuthHandler to create an authentication using the given key and secret
auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


#Connect to the Twitter API using the authentication
api = tweepy.API(auth)
#result = api.search(q='trump')

results = []

#Get the first 5000 items based on the search query
for tweet in tweepy.Cursor(api.search, q='trump', geocode="38.47935,-98.525391,2000.37km" , lang="en",since='2016-02-01',until='2016-02-03').items(2000):
    results.append(tweet)

#Latitude : -94.716053 N
#Longitude : 39.29751 - E
# Verify the number of items returned
print len(results)

def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]


    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]

    return DataSet

#Pass the tweets list to the above function to create a DataFrame
DataSet = toDataFrame(results)
#DataSet.head(5)

# 'None' is treated as null here, so I'll remove all the records having 'None' in their 'userTimezone' column
#DataSet = DataSet[DataSet.userLocation.notnull()]
#DataSet = DataSet[DataSet.userTimezone.notnull()]
#DataSet = DataSet.dropna(DataSet.userLocation.notnull(), how='any')
# Let's also check how many records are we left with now
len(DataSet)

#for index, row in DataSet.iterrows():
#	if (row['userLocation']!=""):
		#row['userLocation']="None"
#		print index, row['userLocation']

#for index, row in DataSet.iterrows():
#	print index, row['userLocation']


#print DataSet.userTimezone

DataSet.to_csv('trump/trump_01_03.csv', sep=',',encoding='utf-8')

