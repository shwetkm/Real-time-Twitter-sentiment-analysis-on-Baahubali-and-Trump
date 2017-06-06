# -*- coding: utf-8 -*-



import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = 'Your_consumer_key'
consumer_secret = 'Consumer_secret_key'
access_token = 'Your_access_token_key'
access_secret = 'Access_scret_key'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('bahubali.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['BaahubaliMovie','baahubali2trailer','Baahubali2trailer','BB2Storm','Baahubali2Trailer'])