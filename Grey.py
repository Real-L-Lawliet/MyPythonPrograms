import sklearn
import sklearn.datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection
import sklearn.linear_model
import sklearn.ensemble
import pylab as pl
import sklearn.svm
import tensorflow as tf
from PIL import Image
import os
import random
import gc

targetarr = []
root_dir = 'C:\\Users\\SID\\Desktop\\Python Codes\\DogVCat\\DogVCat_train'
test_dir = 'C:\\Users\\SID\\Desktop\\Python Codes\\DogVCat\\DogVCat_test'
testpaths = [os.path.join(test_dir, f) for f in os.listdir(test_dir)]
filepaths = [os.path.join(root_dir, f) for f in os.listdir(root_dir)]
random.shuffle(filepaths)
random.shuffle(testpaths)
testpaths = testpaths[:5]
filepaths = filepaths[:10]

G = np.empty([40000 * len(filepaths)])
for j in filepaths:
    t = (j.split('\\')[7].split('.')[0])
    targetarr.append(t)
targetarr = np.array(targetarr)
for j in range(len(targetarr)):
    if(targetarr[j]=='cat'):
        targetarr[j] = 0
    else:
        targetarr[j] = 1
count = 0
df = pd.DataFrame()
rgb_i = 0
area = (25,25,225,225)
while(count<len(filepaths)):

    tuplist = []
    c1 = 0
    for i in range(count,len(filepaths)):
        if(c1>=25):
            break
        img = Image.open(filepaths[i])
        cropped_img = img.crop(area)
        cropped_img = cropped_img.convert('L')
        print(count,end = ' ')
        count+=1
        tuplist.append(list(cropped_img.getdata()))
        c1+=1
    len(tuplist[0])
    for tup in tuplist:
        for i in tup:
            G[rgb_i] = i
            rgb_i+=1
    del tuplist
    gc.collect()

y_test = []
for j in testpaths:
    t = (j.split('\\')[7].split('.')[0])
    y_test.append(t)
y_test = np.array(y_test)
for j in range(len(y_test)):
    if(y_test[j]=='cat'):
        y_test[j] = 0
    else:
        y_test[j] = 1
count = 0
Test_G = np.empty([40000 * len(testpaths)])
rgb_i = 0
print('\n\n')
while(count<len(testpaths)):

    tuplist = []
    c1 = 0
    for i in range(count,len(testpaths)):
        if(c1>=25):
            break
        img = Image.open(filepaths[i])
        cropped_img = img.crop(area)
        cropped_img = cropped_img.convert('L')
        print(count,end = ' ')
        count+=1
        tuplist.append(list(cropped_img.getdata()))
        c1+=1
    len(tuplist[0])
    for tup in tuplist:
        for i in tup:
            Test_G[rgb_i] = i
            rgb_i+=1
    del tuplist
    gc.collect()

G = G.reshape(len(filepaths),40000)
Test_G = Test_G.reshape(len(testpaths),40000)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(G, targetarr, test_size=0.2)
clf = sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(G,targetarr)
print('\n\nThe Score is :',clf.score(Test_G,y_test))
