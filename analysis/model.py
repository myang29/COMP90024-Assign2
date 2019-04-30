import nltk
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import GridSearchCV
from collections import Counter
from sklearn.metrics import accuracy_score,f1_score
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
import re
from sklearn.metrics import accuracy_score,f1_score


positive_tweets = nltk.corpus.twitter_samples.tokenized("positive_tweets.json")
negative_tweets = nltk.corpus.twitter_samples.tokenized("negative_tweets.json")


stop_word = list(stopwords.words())

# remove nonalphabetic by regular expression
def remove_nonalphabet(tweet_corpus):
    for tweet in tweet_corpus:
        for i in range(len(tweet)):
            token = re.sub('[^a-zA-Z]',"",tweet[i])
            tweet[i] = token

        while '' in tweet:     # remove tokens contain only non-alphabet words
            tweet.remove('')
    return tweet_corpus

# remove stopword 
def remove_stopword(tweet_corpus):
    new_corpus = []
    for tweet in tweet_corpus:
        token = []
        for word in tweet:
            if word.lower() not in stop_word:
                token.append(word)
        new_corpus.append(token)
    return new_corpus


positive_tweets = remove_nonalphabet(positive_tweets)      
negative_tweets = remove_nonalphabet(negative_tweets)


positive_tweets = remove_stopword(positive_tweets)
negative_tweets = remove_stopword(negative_tweets)

# randomly split train/test set for positive tweets and negative tweets
positive_train,positive_test,negative_train,negative_test = train_test_split(positive_tweets,negative_tweets,test_size = 0.1, train_size = 0.8)

# develop data = dataset - traindata - testdata
positive_set = positive_train + positive_test
positive_develop = [x for x in positive_tweets if x not in positive_set]

negative_set = negative_train + negative_test
negative_develop = [x for x in negative_tweets if x not in negative_set]

tweets_train = positive_train + negative_train
tweets_test = positive_test + negative_test
tweets_develop = positive_develop + negative_develop


# build frequency dictionary
train_dict = []
c = Counter()
for tweet in tweets_train:
    train_dict.append({i:tweet.count(i) for i in set(tweet)})

test_dict = []
c = Counter()
for tweet in tweets_test:
    test_dict.append({i:tweet.count(i) for i in set(tweet)})

develop_dict = []
c = Counter()
for tweet in tweets_develop:
    develop_dict.append({i:tweet.count(i) for i in set(tweet)})

# prepare data for classifier
vectorizer = DictVectorizer()

train_ = vectorizer.fit_transform(train_dict)
test_ = vectorizer.transform(test_dict)
develop_ = vectorizer.transform(develop_dict)


# get label for dataset
def get_target(positive_list,negative_list):
    result = []
    for i in range(len(positive_list)):
        result.append("positive")
    for i in range(len(negative_list)):
        result.append("negative")
    return result
      
train_target = get_target(positive_train,negative_train)
test_target = get_target(positive_test,negative_test)
develop_target = get_target(positive_develop,negative_develop)


# tuning parameters for NB
alphas = np.array([0.0001,0.001,0.01,0.1,1,10])      # alternative parameter for Naive Bayes alpha
clf_NB = MultinomialNB()

grid = GridSearchCV(estimator = clf_NB, param_grid = dict(alpha = alphas),scoring = 'accuracy') # tuning for best alpha
grid.fit(develop_,develop_target)

print("For Naive Bayes tuning parameter alpha:")
best_alpha = grid.best_estimator_.alpha
print("best alpha is %f"%(best_alpha))


# prove optimal alpha is found
for i in alphas:
    clf_NB = MultinomialNB(alpha = i)
    clf_NB.fit(train_,train_target)
    result = clf_NB.score(develop_, develop_target)
    print("alpha = %9.4f has accuracy %f"%(i,result))


#tuning parameters for LR:
parameter_c = np.array([0.0001,0.001,0.01,0.1,1,10])   # alternative parameter for Logistic Regression
Penalty = ['l1','l2']
clf_LR = LogisticRegression()
grid2 = GridSearchCV(estimator = clf_LR, param_grid = dict(C = parameter_c,penalty = Penalty),scoring = 'accuracy')
grid2.fit(develop_,develop_target)

print("\n")
print("For Logistic Regresstion tuning parameter C and Penalty:")
best_c = grid2.best_estimator_.C
best_pen = grid2.best_estimator_.penalty
print("best C is %f, best Penalty is %s"%(best_c,best_pen))

# prove optimal parameters are found
for i in parameter_c:
    for pen in Penalty:
        clf_LR = LogisticRegression(C= i,penalty = pen)
        clf_LR.fit(train_,train_target)
        result = clf_LR.score(develop_, develop_target)
        print("C = %9.4f and penalty = %s show accuracy %f"%(i,pen,result))



clf_NB = MultinomialNB(alpha = best_alpha)
clf_NB.fit(train_,train_target)
NB_result = clf_NB.predict(test_)
print("Naive Bayes:\n")
print("accuracy       :  %f"%(accuracy_score(test_target,NB_result)))
print("macro f-score  :  %f\n"%(f1_score(test_target,NB_result,average = 'macro')))

clf_LR = LogisticRegression(C = best_c,penalty = best_pen)
clf_LR.fit(train_,train_target)
LR_result = clf_LR.predict(test_)

print("Logistic Regression:\n")
print("accuracy       :  %f"%(accuracy_score(test_target,LR_result)))
print("macro f-score  :  %f"%(f1_score(test_target,LR_result,average = 'macro')))