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


#raw_address = 'http://115.146.92.83:8022'
#backup_address = "http://115.146.92.83:8022"
processed_address = 'http://172.26.38.75:9024'
#geo_data = "sa2.json"
#polygon = fiona.open(geo_data)
city_list = set(['Launceston','Melbourne','Sydney','Adelaide','Perth','Brisbane','Darwin','Canberra'])
city_coordinate = {}
with open ('capital.csv','r') as f:
    reader = csv.reader(f)
    header = next(reader,None)
    for lng,lat,city in reader:
        city_coordinate[city] = [float(lng),float(lat)]


with open('sentiment_model.pkl', 'rb') as file:  
    classifier = pickle.load(file)

#raw_couch = couchdb.Server(raw_address)
processed_couch = couchdb.Server(processed_address)
#backup_couch = couchdb.Server(backup_address)

try:
    db_proceed = processed_couch['processed_tweets']
except:
    db_proceed = processed_couch.create('processed_tweets')

# backup db
# try:
#     db_backup = backup_couch['backup_twit']
# except:
#     db_backup = backup_couch.create('backup_twit')

# import keywords for wrath
with open("/data/wrath_word.csv",'r') as f:
    file = csv.reader(f)
    wrath_word = set(list(file)[0])


# def average_bounding_box(box):
#     """Average list of 4 bounding box coordinates to a midpoint."""
#     lng = 0
#     lat = 0
#     for i in range(len(box[0])):
#         lng += box[0][i][0]
#         lat += box[0][i][1]
#     lat /= 4
#     lng /= 4

#     return [lng,lat]


def get_city(twit):
    """ get coordinates for twitter inside VIC and ignore other place  """

    if twit['place'] == None:
        return None
    else:
        # place[0]: city  place[-1]: state
        place = [i.lstrip() for i in twit['place']['full_name'].split(',')]


    if place[0] == 'Launceston':
        return ('Hobart',city_coordinate['Hobart'])

    elif place[0] in city_list:
        # get coordinates by averaging the boundary box for other small regions inside VIC
        return (place[0],city_coordinate[place[0]])
    else:
        return None



#with open("/data/past_result_try1.json", "r") as f:
with open("/data/past_result_try1.json", "r") as f:
    total_line = 0
    twitLine = f.readline()

    while twitLine:  # while not end of file
        total_line += 1
        # truncate the end of line (\n)
        twitLine = twitLine.rstrip()
        if twitLine[-1] == ',':
            # truncate the last character
            twitLine = twitLine[:-1]
        
        twit = json.loads(twitLine)
        #coordinates = get_coordinates(twit)
        location = get_city(twit)
        if location and (twit["retweeted"] == False): # check location exist and remove replicate
            
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
            twit_text = re.sub("http\S+","",twit['text']) # remove url
            blob = TextBlob(twit_text)
            word_list = [] 
            word_list.append(list(blob.words))
            twit_text = remove_nonalphabet(word_list)
            twit_text = remove_stopword(twit_text)
            twit_text = lemmatization(twit_text)
            twit_text = word_lower(twit_text)
            twit_dict = []
            twit_dict.append({i:twit_text[0].count(i) for i in set(twit_text[0])})
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
                    '_id' : str(twit['id']),
                    'created_at' : twit['created_at'],
                    'coordinates': location[1],
                    'city': location[0],
                    'text' : twit_text,
                    'wrath' : wrath
                }

            try:
                db_proceed.save(doc)
            except:
                pass

        else:
            twitLine = f.readline()
            continue

        twitLine = f.readline()
print ("total linenumber is %d" %total_line)