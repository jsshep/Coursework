# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:58:20 2015

@author: jonathan.shepard
"""


#Naive Bayes homework with Yelp review text
#Task 1
#Read yelp.csv into a DataFrame.
# access yelp.csv in your data directory and load it into a DataFrame

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

yelp = pd.read_table('yelp.csv', sep=',', header=0)

#Task 2
#Create a new DataFrame that only contains the 5-star and 1-star reviews.
# filter the DataFrame to only rows that have a 5-star or 1-star rating. Using an OR condition

yelp15 = yelp[(yelp.stars == 1) | (yelp.stars == 5)]   

#Task 3
#Split the new DataFrame into training and testing sets, using the review text as the only feature and the star rating as the response.
# define X and y

from sklearn.cross_validation import train_test_split
from sklearn import metrics
X = yelp15.text
y = yelp15.stars

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)

#Task 4
#Use CountVectorizer to create document-term matrices from X_train and X_test.
# import and instantiate the vectorizer

from sklearn.feature_extraction.text import CountVectorizer

# fit and transform X_train, but only transform X_test
vect = CountVectorizer()
vect.fit(X_train)
vect.get_feature_names()
training = vect.transform(X_train)

testing = vect.transform(X_test)

#Task 5
#Use Naive Bayes to predict the star rating for reviews in the testing set, and calculate the accuracy.
# import/instantiate/fit
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
nb = MultinomialNB()
nb.fit(training, y_train)

# make class predictions

y_pred_class = nb.predict(testing)

# calculate accuracy
print metrics.accuracy_score(y_test, y_pred_class)


#Task 6
#Calculate the AUC.
# y_test contains fives and ones, which will confuse the roc_auc_score function
y_test[:10].values

# create y_test_binary, which contains ones and zeros instead

import numpy as np
y_test_binary = np.where(y_test == 5,1,0)

# predict class probabilities
y_pred_prob = nb.predict_proba(testing)[:, 1]
print y_pred_prob

# calculate the AUC using y_test_binary and y_pred_prob
print metrics.roc_auc_score(y_test_binary, y_pred_prob)

#Task 7

#Plot the ROC curve.
import matplotlib.pyplot as plt
%matplotlib inline
# plot ROC curve using y_test_binary and y_pred_prob

fpr, tpr, thresholds = metrics.roc_curve(y_test_binary, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

print(metrics.roc_curve(y_test_binary, y_pred_prob))


#Task 8
#Print the confusion matrix, and calculate the sensitivity and specificity. Comment on the results.

# print the confusion matrix

print metrics.confusion_matrix(y_test_binary, y_pred_class)

# calculate sensitivity
sensitivity = (119.0 / 126.0)

# calculate specificity
specificity = (810.0 / 886.0)

#The model is having a much easier time detecting five-star reviews than one-star reviews.



#Task 9
#Browse through the review text for some of the false positives and false negatives. Based on your knowledge of how Naive Bayes works, do you have any theories about why the model is incorrectly classifying these reviews?


 
Task 10
Let's pretend that you want to balance sensitivity and specificity. You can achieve this by changing the threshold for predicting a 5-star review. What threshold approximately balances sensitivity and specificity?
In [ ]:
# create a list that will store the results of the process below


# loop through the thresholds returned by the metrics.roc_curve function
In [ ]:
# locate the minimum difference (at which sensitivity and specificity are balanced)
Task 11
Let's see how well Naive Bayes performs when all reviews are included, rather than just 1-star and 5-star reviews:
Define X and y using the original DataFrame from step 1. (y should contain 5 different classes.)
Split the data into training and testing sets.
Calculate the testing accuracy of a Naive Bayes model.
Compare the testing accuracy with the null accuracy.
Print the confusion matrix.
Comment on the results.
In [ ]:
# define X and y using the original DataFrame
In [ ]:
# split into training and testing sets
In [ ]:
# create document-term matrices
In [ ]:
# fit a Naive Bayes model
In [ ]:
# make class predictions
In [ ]:
# calculate the testing accuary
In [ ]:
# calculate the null accuracy
In [ ]:
# print the confusion matrix
Comments: