import os
import tweepy
from textblob import TextBlob

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_config = {
    "q": "doctorwho",
    "lang": "en"
}

public_tweets = api.search(**search_config)

for tweet in public_tweets:
    print("==================================================")
    print(tweet.text)
    wiki = TextBlob(tweet.text)
    print(wiki.sentiment.polarity)
