import nltk
import json
from nltk.corpus import wordnet as wn
import re
from textblob import TextBlob
import couchdb

couch = couchdb.Server()
'''
try:
    db_save = couch['wrath_twit']
except:
    db_save = couch.create('wrath_twit')
'''

with open('tinyTwitter.json', "r") as f:
    # read metadata from first row
    # {"total_rows":3877777,"offset":805584,"rows":[
    firstRow = json.loads(f.readline().rstrip()[:-1] + '0}')
    numRows = firstRow['total_rows']
    
    twitLine = f.readline()
    while twitLine:  # while not end of file
        #lineNumber += 1
        # truncate the end of line (\n)
        twitLine = twitLine.rstrip()
        if twitLine[-1] == ',':
            # truncate the last character
            # print('"," detected')
            twitLine = twitLine[:-1]
        if twitLine[0] == ']':
            # ignore the last line ']}'
            break

        # print ("process {} is processing ...".format(rank))
        twit = json.loads(twitLine)
        #print (twit)
        twit_text = re.sub("http\S+","",twit['value']['properties']['text'])
        blob = TextBlob(twit_text)
        #print(blob.classify())
        print(blob.sentiment.polarity)
        break