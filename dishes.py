import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
import sklearn.model_selection
import sklearn.naive_bayes

dishes = pd.read_json('train.json')

#print(dishes.keys())
cuisine = dishes['cuisine'][:1000]

ingredients = dishes['ingredients'][:1000]

'''def combineAndRemoveSpaces(row): 
	return " ".join([item.replace(' ', '') for item in row])'''
x = []

for row in ingredients:
	cv = CountVectorizer()
	tf_train = cv.fit_transform(row)
	tf_train = tf_train.toarray()
	x.append(tf_train)
x = np.array(x)
print(x.shape)
y = pd.Categorical(cuisine).codes
y = np.array(y,dtype = np.int32)
print(y.shape)
#print(cv.get_feature_names())



'''x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size = 0.2)
model = sklearn.naive_bayes.GaussianNB()
train = model.fit(x_train,y_train)
test = model.score(x_test,y_test)'''

#print(all_words)