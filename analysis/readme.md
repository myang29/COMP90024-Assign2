# Sentiment Analysis
## 1. Introduction

A python based sentiment analysis system which preprocesses raw twitter data from eight Australian Capital city and conducts sentiment analysis by Naive Bayes combined with textblob and keywords.

The sentiment Analysis system contains 5 files:

1. sentiment_model.py:  
   A Naive Bayes and a Logistic Regression Model are trained by nltk positive and negative twitter corpus. After turning parameters, Naive Bayes usually perform better so save trained Naive Bayes Sentiment Model via pickle.

2. sentiment_model.pkl  
   A Naive Bayes sentiment model saved by pickle so that it can be loac in other file.  

3. wrath_word.csv  
   A text file contains keywords which indicates Wrath emotion.

4. capital.csv  
   A csv file with Australian capital cities and its coordinates

5. analysis_new.py  
   preprocess raw twitter data, conduct sentiment analysis, and matching SA2 polygons, and save result to couchDB as Processed_twit (call by harvester process directly).

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