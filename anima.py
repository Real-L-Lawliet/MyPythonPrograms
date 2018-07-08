import sklearn
import scipy
import numpy as np 
import pandas as pd
import sklearn.linear_model
import sklearn.ensemble
import pickle
import pylab as pl
import scipy.misc as smp

with open("C:/Users/Sourav/Downloads/cifar-100-python/train",'rb') as fo:
	di = pickle.load(fo,encoding='latin1')



print(di["data"].shape)

'''pl.matshow(di["data"])

pl.show()'''

x=np.array(di["data"])

img = np.reshape(x[0],(3,32,32))
img = smp.toimage(img).convert('LA')
img.convert('L')
img = np.array(img)

y=np.array(di["coarse_labels"])

x_train,x_test,y_train,y_test, = sklearn.model_selection.train_test_split(x,y,test_size=0.2)

clf = sklearn.ensemble.RandomForestClassifier(n_jobs=1,random_state=0)

clf.fit(x_train,y_train)

print('Train -> ',clf.score(x_train,y_train))
print('Test -> ',clf.score(x_test,y_test))

print(clf.feature_importances_)
