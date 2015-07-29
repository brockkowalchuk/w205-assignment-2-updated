# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:25:33 2015

@author: brockkowalchuk
"""
import sys
import tweepy
import time
import signal
import datetime
import json
from boto.s3.connection import S3Connection #AMZN Connection
from boto.s3.key import Key #AMZN Key for Bucket

class TweetSerializer:
   out = None #text file pointer
   first = True
   count = 0

   def __init__(self, hashtag):
       self.hashtag = hashtag #incorporate specific hashtag into name of filename

   def start(self):
      self.count += 1
      fname = str(self.hashtag)+"-tweetsText-"+str(self.count)+".txt"
      self.out = open(fname,"w") 
      self.out.write("[\n")
      self.first = True

   def end(self):
      if self.out is not None:
         self.out.write("\n]\n")
         self.out.close()
      self.out = None

   def write(self,tweet):
      if not self.first:
         self.out.write(",\n")
      self.first = False
      self.out.write(tweet.text.encode('utf-8')) #aadd text in utf-8 format
      
#Access TWTR with the following keys and secret passphrases
consumer_key = "...";
consumer_secret = "...";
access_token = "...";
access_token_secret = "...";

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#AMZN AWS Access Requirements
#conn = S3Connection('...' , '...')
#mybucket = 'w205-a2-update'
#bucketobj = conn.get_bucket(mybucket)
#k = Key(bucketobj)

#TWTR Queries
q1 = "#Trump #GOP"
q2 = "#Trump"
q3 = "#GOP"

t1 = TweetSerializer("#Trump #GOP")
t2 = TweetSerializer("#Trump")
t3 = TweetSerializer("#GOP")

def pullTweets(tquery, serializer):
    i = 0 #how many tweets
    tweets_id = None #create variable for Tweet ID
    tweetCursor = tweepy.Cursor(api.search,q=tquery, since="2015-07-19", until="2015-07-20", max_id = tweets_id, lang = "en").items()
    while True:
        try:
            tweet = tweetCursor.next()
            tweets_id = tweet.id
            if i % 1000 == 0:
                serializer.start()
            serializer.write(tweet)
            if i % 1000 == 999:             
                serializer.end()
            i += 1
        except tweepy.TweepError as e:
            print "Received Tweep Error, will sleep for 5 mins...", e
            time.sleep(300)
            tweetCursor = tweepy.Cursor(api.search,q=tquery, since="2015-07-19", until="2015-07-26", max_id = tweets_id, lang = "en").items()
            continue
        except StopIteration:
            break

pullTweets(tquery = q1, serializer = t1)
pullTweets(tquery = q2, serializer = t2)
pullTweets(tquery = q3, serializer = t3)
