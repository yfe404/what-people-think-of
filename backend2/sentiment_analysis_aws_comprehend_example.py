# coding: utf-8
import boto3
client = boto3.client('comprehend')
response = client.detect_sentiment(Text="I love sushis", LanguageCode="en")
response
print(response["Sentiment"], response["SentimentScore"])
