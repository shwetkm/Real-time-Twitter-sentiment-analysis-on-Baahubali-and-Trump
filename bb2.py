# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:26:47 2017

@author: SM00493336
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
consumer_key = 'yBoLvYCXKwvgUrzHkQjYyVejM'
consumer_secret = 'UrjDaVyo5r0UObTvYxdDSNH2Oq77kmcgrigJmk0AWhvmHPJ4z5'
access_token = '260596099-THbHuYA2ASsgJw3UD6qCV9EW1xKXxWKwUnCKe62N'
access_secret = '39JkocbY3n8ZhbD9nVMo6hkmfX3I0l9VktK02RFtq01DE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            txtblb = TextBlob(tweet).sentiment
            print(tweet, txtblb.polarity, txtblb.subjectivity)
            if (txtblb.subjectivity*100 >= 60):
                output = open("bb2.txt","a")
                output.write(str(txtblb.polarity))
                output.write('\n')
                output.close()
                return True           
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['trump'])