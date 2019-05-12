# Sentiment Analysis
## 1. Introduction

A python based sentiment analysis system which preprocesses raw data, conducts sentiment analysis by Naive Bayes combined with textblob and keywords, and matches twitter which inside the VIC state by corresponding SA2 polygon.

The sentiment Analysis system contains 5 files:

1. sentiment_model.py:  
   A Naive Bayes and a Logistic Regression Model are trained by nltk positive and negative twitter corpus. After turning parameters, Naive Bayes usually perform better so save trained Naive Bayes Sentiment Model via pickle.

2. sentiment_model.pkl  
   A Naive Bayes sentiment model saved by pickle so that it can be loac in other file.  

3. wrath_word.csv  
   A text file contains keywords which indicates Wrath emotion.

4. sa2.json  
   A json file of SA2 polygon used for matching the twitter location by corresponding SA2 Code.

5. analysis.py  
   preprocess raw twitter data, conduct sentiment analysis, and matching SA2 polygons, and save result to couchDB as Processed_twit

## 2. Prerequisites
```
#install python 3.6  
sudo apt-get intall python3.6
```
```
#install nltk  
pip3 install nltk
```
```
#install sklearn  
pip3 install sklearn
```
```
#install numpy  
pip3 install numpy
```
```
#intall pickle  
pip3 install pickle
```
```
#install textblob  
pip3 install textblob
```
```
#install couchdb  
pip3 install couchdb
```
For polygon matching algorithm:
```
#install fiona  
pip3 install fiona
```
```
#install shapely  
pip3 install shapely
```