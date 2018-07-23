import os
import collections
import numpy as np
import sklearn
import sklearn.model_selection
import sklearn.naive_bayes
import pandas as pd
import nltk
import nltk.stem.porter
import nltk.corpus
import sklearn.ensemble
import sklearn.model_selection
import sklearn.naive_bayes
import collections
from sklearn.naive_bayes import MultinomialNB
import tensorflow as tf


df = pd.read_csv('trainmr.csv')
label = [0,1,2,3,4]
#include = [0,1,2,3,4,5]
#print(label)

line = df['Phrase'][:1000]
words = []
new = []

stop_words = set(nltk.corpus.stopwords.words('english'))
porter_stemmer = nltk.stem.porter.PorterStemmer()
#print(len(emails))
for i in line:
	i = i.lower()
	#new = line.lower()
	words = i.split(' ')
	final_sentence = []
	new_sentence = ""
	for word in words:
		if word not in stop_words:
			word_stem = porter_stemmer.stem(word)
			#final_sentence.append(word_stem)
			new_sentence = str(word_stem)
	new.append(new_sentence)
vect = sklearn.feature_extraction.text.CountVectorizer()
tf_train = vect.fit_transform(new)
#print(line.shape)
#print(len(new))
df = df.join(pd.get_dummies(df["Sentiment"]))
df = df.drop(['Sentiment'], axis = 1)
#print(df.head())

for j in range(5):
	x = tf_train
	x = x.toarray()
	ls = [str(i) for i in range(0,293)]
	x = pd.DataFrame(x, columns = ls)
	#print(x.shape)
#print(x.shape)

	y = df[label[j]][:1000]
	#print(y.shape)
#x = x.reshape(-1,1)

	x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.2)
	my_feature_columns = []
	for key in x.keys():
		my_feature_columns.append(tf.contrib.layers.feature_column.real_valued_column(key))
	Classifier = tf.estimator.DNNClassifier(feature_columns = my_feature_columns, hidden_units = [10,10], n_classes = 2)
	def split_train():
		return dict(x_train), y_train
	def split_test():
		return dict(x_test), y_test
	Classifier.train(input_fn = split_train, steps = 200)
	eval_result = Classifier.evaluate(input_fn = split_test, steps = 1)
print(eval_result)
