# coding: utf-8
from textblob import TextBlob
wiki = TextBlob("John Doe is angry that he never gets good matches on Tinder")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)
