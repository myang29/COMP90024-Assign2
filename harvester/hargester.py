import os
import time
global time_new,counter
import tweepy
import re
import json
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, status):
        str_tweet = str(status)
        posttime = re.findall('created_at\":\"(.+?)\"', str_tweet)
        text = re.findall('\"text\":\"(.+?)\",', str_tweet)
        coordinates = re.findall('\"coordinates\":{\"type\":\"Point\",\"coordinates\":\[(.+?)\]', str_tweet)
        with open(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json', 'a') as result:
            if coordinates == []:
                polygon = re.findall('type\":\"Polygon\",\"coordinates\":\[(.+?)\]\}', str_tweet)
                try:
                    tweet = {'time': posttime[0], 'text': text[0], 'polygon': polygon[0], 'coordinates': None}
                    result.write(json.dumps(tweet) + ',\n')
                except:
                    pass
            else:
                try:
                    tweet = {'time': posttime[0], 'text': text[0], 'polygon': None, 'coordinates': coordinates[0]}
                    result.write(json.dumps(tweet) + ',\n')
                except:
                    pass
        print(os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (
                    1024 * 1024))
        if os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024) > 2048:
            exit()
    def on_error(self, status):
        if status == 420:
            print(420,status)
        else:
            print('other',status)

def getting_data(consumer_key,consumer_secret,access_token,access_token_secret):

    global time_start
    with open(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json', 'a') as result:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        #myStream.filter(locations=[141, -39.13, 150, -34])
        myStream.filter(locations=[113, -43, 153, -10])

consumer_key_list = []
consumer_key_list.append('EPCx8b0R05KtuAkW5MLm1mSCg')
consumer_key_list.append('Efvd7TxUTAFhWtkwaAv8rkPkS')
consumer_key_list.append('OWZY1FlntpHBHs0ZHFIBypL3i')
consumer_secret_list = []
consumer_secret_list.append('XyMDpYOp58PF7RZBGSH49wfhV19NxUogZGoSp2VLSeswDRuYnV')
consumer_secret_list.append('2SeEWjT2yUpZTBcq8NzNT3HbzTtAxaC6OhslCrrPYj7EpvMyf7')
consumer_secret_list.append('YLCgOgytB0FLNUjigQx29d5d0R04mwOFlKSkS7aDdvxSLkfNQ7')
access_token_list = []
access_token_list.append('1120942584623321088-ovBMrrhmt79H5Kv2p7eHe4nBB2R3gc')
access_token_list.append('1119558033061732352-GZgRSwG2IKrcheRB2hBf5kjlr01fJt')
access_token_list.append('1120935559180865536-ngQ9Q4ewUzqj0iFGKbBHO7FLDd9yqu')
access_token_secret_list = []
access_token_secret_list.append('dnsbxgp9UvGdfGTkF77p7lGGEhueHKlz4ptJIfADNVK52')
access_token_secret_list.append('OvKCt9VAHpFrGoTki3bsvf2WmpM6uyiIgK8jZDbAjqcPt')
access_token_secret_list.append('68E9P0iqP6vV0iRaaezIYTTkJuuZNgZ1d0Zo1sE5ou1a5')
start = time.clock()
decisioner = 0
time_start = []

with open(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json','a') as init:
    pass
while True:
    if decisioner>=len(consumer_key_list):
        decisioner-=len(consumer_key_list)
    try:
        end = time.clock()
        print('time', end - start, '  file size  ',
              os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),
              'account number', decisioner)
        getting_data(consumer_key_list[decisioner], consumer_secret_list[decisioner], access_token_list[decisioner],access_token_secret_list[decisioner])
        #print('time',end-start,'  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number',decisioner)
    except Exception as e:
        time.sleep(20)
        print(str(e))
        end = time.clock()
        print('time', end - start, '  file size  ',
              os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),
              'account number', decisioner)
        decisioner+=1

    if os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024) > 2048:
        break
