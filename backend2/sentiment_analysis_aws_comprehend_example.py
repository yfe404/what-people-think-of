# coding: utf-8
import boto3
client = boto3.client('comprehend')
response = client.detect_sentiment(Text="John Doe is angry that he never gets good matches on Tinder", LanguageCode="en")
response
print(response["Sentiment"], response["SentimentScore"])
