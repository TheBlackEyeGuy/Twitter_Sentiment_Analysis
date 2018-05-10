import tweepy
from textblob import TextBlob

consumer_key = input("Enter consumer key : ")
consumer_secret = input("Enter consumer secret : ")

access_token = input("Enter access token : ")
access_token_secret = input("Enter access token secret : ")

#sign in into your twitter account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth = auth.set_access_token(access_token, access_token_secret)

#Use twitter API to get all the access to twitter's data 
api = tweepy.API(auth)

#taking input of interested topic
topic = input("Enter your interested topic : ")

#fetching all tweets related to some input topic
public_tweets = api.search(topic)

#printing all tweets as text and their respective sentiments
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	sentiment_analysis = analysis.sentiment
	print(sentiment_analysis)
