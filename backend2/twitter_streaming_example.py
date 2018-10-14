# coding: utf-8
import os
import base64
import json
import tweepy
import boto3

kinesis = boto3.client('kinesis')


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.text:
            record = {
                "id": status.id,
                "created_at": str(status.created_at),
                "text": status.text
            }
            data=base64.urlsafe_b64encode(
                json.dumps(record).encode()).decode()
            data += "|" ## delimiter
            
            response = kinesis.put_record(
                StreamName='twitterStream',
                Data=data,
                PartitionKey='key'
            )
            print("Sending: {}".format(record["text"].strip()[:50]))


consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['Trump'], languages=["en"])
