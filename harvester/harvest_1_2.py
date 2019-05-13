import os
import time
global time_new,counter
import tweepy
import re
import json
import sys
import nltk
import json
import sys
#import demjson


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, status):
        str_tweet = str(status)
        print('##############before analysis#################')
        #analysis(str_tweet)
        print(str_tweet)
        print('##################after analysis#####################')
        #print(str_tweet)
        tweet_id = re.findall('id\":(\d+),',str_tweet)
        if(tweet_id != []):
            tweet_id=tweet_id[0]
        user_id = re.findall('user\":\{\"id\":(\d+),',str_tweet)
        with open(path+r'tweetId_try1.txt', 'a') as tweet_id_file:
            tweet_id_file.write(tweet_id+'\n')
        if (user_id != []):
            user_id = user_id[0]
            getting_user_history(user_id)
        #print(os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\past_result_try1.json') / (1024 * 1024))

        with open(path+r'result_try1.json', 'a') as result:
            json.dump(json.loads(str_tweet),result)
            result.write(',\n')
            #print(os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024))
    def on_error(self, status):
        if status == 420:
            #print(420,status)
            pass
        else:
            #print('other',status)
            pass

def getting_data(consumer_key,consumer_secret,access_token,access_token_secret):

    global time_start
    with open(path+r'result_try1.json', 'a') as result:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        #myStream.filter(locations=[141, -39.13, 150, -34])
        myStream.filter(locations=[113, -43, 153, -10])
def getting_user_history(user_id):
    consumer_key = 'OWZY1FlntpHBHs0ZHFIBypL3i'
    consumer_secret = 'YLCgOgytB0FLNUjigQx29d5d0R04mwOFlKSkS7aDdvxSLkfNQ7'
    access_token = '1120935559180865536-ngQ9Q4ewUzqj0iFGKbBHO7FLDd9yqu'
    access_token_secret = '68E9P0iqP6vV0iRaaezIYTTkJuuZNgZ1d0Zo1sE5ou1a5'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    results = api.user_timeline(user_id=user_id,count = 500)
    counter = 0
    location = [113, -43, 153, -10]
    try:
        for i in results:
            str_tweets = str(i)
            coordinates = re.findall('\'coordinates\': {\'type\': \'Point\', \'coordinates\': \[(.+?)\]', str_tweets)
            # print(posttime[0],coordinates)
            if coordinates == []:
                polygon = re.findall('type=\'Polygon\', coordinates=\[(.+?)\]\)', str_tweets)
                if(polygon!=[]):
                    x = float(polygon[0].split(',')[0][2:])
                    y = float(polygon[0].split(',')[1][1:-1])
                    if(location[0]<=x<=location[2] and location[1]<=y<=location[3]):
                        tweet_id = re.findall('id\': (\d+),', str_tweets)
                        if tweet_id!=[]:
                            tweet_id = tweet_id[0]
                        with open(path +r'tweetId_try1.txt', 'r') as tweet_id_file:
                            decisioner1 = 0
                            for i in tweet_id_file:
                                if tweet_id==i:
                                    decisioner1=1
                            if decisioner1==0:
                                with open(path+r'past_result_try1.json','a') as result1:
                                    str_tweets = re.findall('_json=(.*?),\screated_at=datetime\.datetime', str_tweets)
                                    if (str_tweets != []):
                                        str_tweets = str(str_tweets[0])
                                       js = eval(str_tweets)
                                        json.dump(js, result1)
                                        result1.write(',\n')
                                        with open(path+r'tweetId_try1.txt','a') as tweet_id_file:
                                            tweet_id_file.write(tweet_id + '\n')
                                        if(os.path.getsize( path +r'past_result_try1.json') / (1024 * 1024)>15000):
                                            exit()

    except Exception as e:
        print('error getting history----------------',str(e))
        pass
consumer_key_list = []
consumer_key_list.append('EPCx8b0R05KtuAkW5MLm1mSCg')
consumer_key_list.append('Efvd7TxUTAFhWtkwaAv8rkPkS')

consumer_secret_list = []
consumer_secret_list.append('XyMDpYOp58PF7RZBGSH49wfhV19NxUogZGoSp2VLSeswDRuYnV')
consumer_secret_list.append('2SeEWjT2yUpZTBcq8NzNT3HbzTtAxaC6OhslCrrPYj7EpvMyf7')

access_token_list = []
access_token_list.append('1120942584623321088-ovBMrrhmt79H5Kv2p7eHe4nBB2R3gc')
access_token_list.append('1119558033061732352-GZgRSwG2IKrcheRB2hBf5kjlr01fJt')

access_token_secret_list = []
access_token_secret_list.append('dnsbxgp9UvGdfGTkF77p7lGGEhueHKlz4ptJIfADNVK52')
access_token_secret_list.append('OvKCt9VAHpFrGoTki3bsvf2WmpM6uyiIgK8jZDbAjqcPt')

start = time.clock()
decisioner = 0
time_start = []
path = str(sys.argv[1])

with open(path+r'result_try1.json','a') as init:
    pass
while True:
    if decisioner>=len(consumer_key_list):
        decisioner-=len(consumer_key_list)
    try:
        end = time.clock()
        #print('time', end - start, '  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number', decisioner)
        getting_data(consumer_key_list[decisioner], consumer_secret_list[decisioner], access_token_list[decisioner],access_token_secret_list[decisioner])
        #print('time',end-start,'  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number',decisioner)
    except Exception as e:
        #time.sleep(20)
        print('error----------------',str(e))
        end = time.clock()
        #print('time', end - start, '  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number', decisioner)
        decisioner+=1
