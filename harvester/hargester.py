import os
import time
global time_new,counter
import tweepy
import random
import re
import json
import sys
#import demjson
import nltk
import json
# import sys
import nltk
import json
from nltk.corpus import wordnet as wn
import re
import os
import csv
from textblob import TextBlob
import couchdb
import pickle
#import fiona
from sentiment_model import vectorizer,remove_nonalphabet,remove_stopword,lemmatization,word_lower
from sklearn.feature_extraction import DictVectorizer
#from shapely.geometry import shape, Point
def get_city(twit):
    """ get coordinates for twitter inside VIC and ignore other place  """

    if twit['place'] == None:
        return None
    else:
        # place[0]: city  place[-1]: state
        place = [i.lstrip() for i in twit['place']['full_name'].split(',')]

    if place[0] == 'Launceston':
        return ('Hobart', city_coordinate['Hobart'])

    elif place[0] in city_list:
        # get coordinates by averaging the boundary box for other small regions inside VIC
        return (place[0], city_coordinate[place[0]])
    else:
        return None

def analysis(twit):
        # coordinates = get_coordinates(twit)
    location = get_city(twit)
    if location and (twit["retweeted"] == False):  # check location exist and remove replicate
            # polygon matching for assign the coordinate to corresponding area used for Aurin
            # reference: https://gis.stackexchange.com/questions/208546/check-if-a-point-falls-within-a-multipolygon-with-python
            # point = Point(coordinates)
            # code = None
            # if coordinates == [144.9631, -37.8136]:
            #     code = 206041122
            # else:
            #     for multi in polygon:
            #         point.within(shape(multi['geometry']))
            #         code = multi['properties']['SA2_Code_2011']

            # process tweet to predict
            twit_text = re.sub("http\S+", "", twit['text'])  # remove url
            blob = TextBlob(twit_text)
            word_list = []
            word_list.append(list(blob.words))
            twit_text = remove_nonalphabet(word_list)
            twit_text = remove_stopword(twit_text)
            twit_text = lemmatization(twit_text)
            twit_text = word_lower(twit_text)
            twit_dict = []
            twit_dict.append({i: twit_text[0].count(i) for i in set(twit_text[0])})
            print(twit_dict)
            test_ = vectorizer.transform(twit_dict)
            classify_result = classifier.predict(test_)

            # tag twitter: identify wrath twitter
            if classify_result == "negative" and blob.sentiment.polarity < -0.5 and blob.sentiment.subjectivity > 0.5:
                wrath = True
            elif len(set(twit_text[0]).intersection(wrath_word)) > 0:
                wrath = True
            else:
                wrath = False

            doc = {
                '_id': str(twit['id']),
                'created_at': twit['created_at'],
                'coordinates': location[1],
                'city': location[0],
                'text': twit_text,
                'wrath': wrath
            }

            try:
                db_proceed.save(doc)
            except:
                pass

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, status):
        """get real-time tweet and store it"""
        str_tweet = str(status)
        random_num = random.randint(0,2)
        if random_num == 0:
            # print(str_tweet)
            tweet_id = re.findall('id\":(\d+),', str_tweet)
            if (tweet_id != []):
                tweet_id = tweet_id[0]
            user_id = re.findall('user\":\{\"id\":(\d+),', str_tweet)
            with open(path + r'tweetId_try1.txt', 'a') as tweet_id_file:
                tweet_id_file.write(tweet_id + '\n')
            if (user_id != []):
                user_id = user_id[0]
                getting_user_history(user_id)
            # print(os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\past_result_try1.json') / (1024 * 1024))

            with open(path + r'result_try1.json', 'a') as result:
                json.dump(json.loads(str_tweet), result)
                result.write(',\n')
                print('before analysis')
                str_tweet=str_tweet.replace('false','False')
                str_tweet=str_tweet.replace('null','None')
                str_tweet=str_tweet.replace('true','True')
                analysis(eval(str_tweet))
                print('analysis end')
                # print(os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024))

    def on_error(self, status):
        if status == 420:
            # print(420,status)
            pass
        else:
            # print('other',status)
            pass


def getting_data(consumer_key, consumer_secret, access_token, access_token_secret):
    """create listener to listen real-time tweets and filter it according to location"""
    global time_start
    with open(path + r'result_try1.json', 'a') as result:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        # myStream.filter(locations=[141, -39.13, 150, -34])
        myStream.filter(locations=[113, -43, 153, -10])
def getting_user_history(user_id):
    """getting a users past tweets and filer it and store it"""
    print('start getting history')
    consumer_key = 'OWZY1FlntpHBHs0ZHFIBypL3i'
    consumer_secret = 'YLCgOgytB0FLNUjigQx29d5d0R04mwOFlKSkS7aDdvxSLkfNQ7'
    access_token = '1120935559180865536-ngQ9Q4ewUzqj0iFGKbBHO7FLDd9yqu'
    access_token_secret = '68E9P0iqP6vV0iRaaezIYTTkJuuZNgZ1d0Zo1sE5ou1a5'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    results = api.user_timeline(user_id=user_id, count=500)
    counter = 0
    location = [113, -43, 153, -10]
    try:
        for i in results:
            str_tweets = str(i)

            coordinates = re.findall('\'coordinates\': {\'type\': \'Point\', \'coordinates\': \[(.+?)\]', str_tweets)
            # print(posttime[0],coordinates)
            if coordinates == []:
                polygon = re.findall('type=\'Polygon\', coordinates=\[(.+?)\]\)', str_tweets)
                if (polygon != []):
                    x = float(polygon[0].split(',')[0][2:])
                    y = float(polygon[0].split(',')[1][1:-1])
                    if (location[0] <= x <= location[2] and location[1] <= y <= location[3]):
                        tweet_id = re.findall('id\': (\d+),', str_tweets)
                        if tweet_id != []:
                            tweet_id = tweet_id[0]
                        with open(path + r'tweetId_try1.txt', 'r') as tweet_id_file:
                            decisioner1 = 0
                            for i in tweet_id_file:
                                if tweet_id == i[:-1]:
                                    decisioner1 = 1
                            if decisioner1 == 0:
                                with open(path+r'past_result_try1.json','a') as result1:
                                    str_tweets = re.findall('_json=(.*?),\screated_at=datetime\.datetime', str_tweets)
                                    if (str_tweets != []):
                                        str_tweets = str(str_tweets[0])
                                        print('------------------------------')

                                        str_tweets=str_tweets.replace('false','False')
                                        str_tweets=str_tweets.replace('null','None')
                                        str_tweets=str_tweets.replace('true','True')
                                        js = eval(str_tweets)
                                        analysis(js)
                                        print('================================')
                                        json.dump(js, result1)
                                        result1.write(',\n')
                                        with open(path+r'tweetId_try1.txt','a') as tweet_id_file:
                                            tweet_id_file.write(tweet_id + '\n')
                                        if(os.path.getsize( path +r'past_result_try1.json') / (1024 * 1024)>15000):
                                            exit()
    except Exception as e:
        print(str(e))
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
row_address = ''
processed_address = sys.argv[2]
city_list = set(['Launceston','Melbourne','Sydney','Adelaide','Perth','Brisbane','Darwin','Canberra'])
city_coordinate = {}
with open (path+'capital.csv','r') as f:
    reader = csv.reader(f)
    header = next(reader,None)
    for lng,lat,city in reader:
        city_coordinate[city] = [float(lng),float(lat)]


with open(path+'sentiment_model.pkl', 'rb') as file:
    classifier = pickle.load(file)

#raw_couch = couchdb.Server(raw_address)
processed_couch = couchdb.Server(processed_address)
#backup_couch = couchdb.Server(backup_address)

try:
    db_proceed = processed_couch['processed_tweets']
except:
    db_proceed = processed_couch.create('processed_tweets')
with open(path+"wrath_word.csv",'r') as f:
    file = csv.reader(f)
    wrath_word = set(list(file)[0])
while True:
    """if one of account going down, just try to use next one."""
    if decisioner >= len(consumer_key_list):
        decisioner -= len(consumer_key_list)
    try:
        end = time.clock()
        # print('time', end - start, '  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number', decisioner)
        getting_data(consumer_key_list[decisioner], consumer_secret_list[decisioner], access_token_list[decisioner],
                     access_token_secret_list[decisioner])
        # print('time',end-start,'  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number',decisioner)
    except Exception as e:
        # time.sleep(20)
        print(str(e))
        end = time.clock()
        # print('time', end - start, '  file size  ',os.path.getsize(r'E:\home work\semester2\cloud computing\ass2\data\result_try1.json') / (1024 * 1024),'account number', decisioner)
        decisioner += 1


