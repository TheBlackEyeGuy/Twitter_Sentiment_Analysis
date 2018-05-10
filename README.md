# Twitter_Sentiment_Analysis

# Overview
This app simply analyses the tweets based on emotions, positivity, negativity, neutrality of tweets expressed in form of vocabulary. It uses twitter api to fetch the tweets and uses it's prebuilt functions/modules to get started for the developers using twitter's data.

# Dependencies
To use this simple application, follow steps in ordered fashion as indicated below :

1. Sign in into your twitter account
2. Set-up twitter app at : [*Twitter Application Manager*](https://apps.twitter.com/)
3. Fill up the details of your app
4. Generate **access_token**, button stacked just below your **consumer_token**
5. Install tweepy, textblob :

 - `pip install -U tweepy`
 - `pip install -U textblob`

6. Download nltk corpora

 - `python3 -m textblob.download_corpora`

7. Finally run `python3 run.py`

###### Credits
Here all the credit goes to @llSourcell whose teaching is true inspiration to me.
