
# coding: utf-8

# In[402]:


#Imports and setup

import pickle
import numpy as np
import os
import skimage as sk
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt
from enum import Enum

from sklearn.externals import joblib

#Loading the dataset from disk
get_ipython().run_line_magic('matplotlib', 'inline')

#Additional imports, to be moved to a new file later
from sklearn import svm
from scipy import sparse
clf = svm.SVC(gamma=0.001, C=100.)


# In[407]:


def load_img(dirpath, img_width=64, img_height=64, channel_dim = 3, dtype=np.float32):

    #Reading all files from all subdirectories 
    dict_class_label = {} #Map labels to values
    
    #POSSIBLE OPTIMIZATION - use imread_collection
    num_files = sum([len(files) for _, dirs, files in os.walk(dirpath)])
    num_items = 0
    #num_files = num_dirs = 0
    #for _, dirs, files in os.walk(dirpath):
     #   num_files += len(files)
      #  num_dirs  += 1

    X = np.zeros((num_files, img_width, img_height, channel_dim), dtype = dtype) #64x64 thumbnails, preallocating space
    y = np.zeros(num_files,dtype=np.uint8)

    img_dirs = os.listdir(dirpath)

    for label, img_dir in enumerate(img_dirs):
        
        dict_class_label[label] = img_dir
        
        img_files = os.listdir(os.path.join(dirpath, img_dir))    
        #POSSIBLE OPTIMIZATION - Assign labels to y based on number of files
        #Load all images into X
        for i, img_file in enumerate(img_files):
            img_file = os.path.join(dirpath, img_dir, img_file)
            img = imread(img_file)
            img = resize(img, (img_width,img_height),mode='constant')
            X[num_items] = img
            y[num_items] = label
            num_items += 1
            #Finished file load, data type is float at leaf level
            
            #subtract mean
    return X, y, dict_class_label
    
# Load the dataset, perform sensibility checks
X, y, labels = load_img('dataset-resized')


# In[408]:


# Preprocessing - flatten image data
def preprocess(X, y, normalize=False):
    X = np.reshape(X, (X.shape[0],-1))
    y = np.reshape(y, (y.shape[0], -1))

    # Preprocessiong - subtract mean
    if normalize is True:
        X -= np.mean(X, axis = 0)

    #Create sparse matrices out of data
    X = sparse.csr_matrix(X)
    y = y.ravel()
    
    return X, y
#mean_img = np.mean(X, axis = 0)
#plt.imshow(mean_img.reshape((64,64,3)).astype('uint8')) # visualize the mean image


# In[409]:


X, y = preprocess(X, y, normalize=True)
clf.fit(X, y)


# In[390]:


joblib.dump(clf, 'svm.pkl')


# In[412]:


#Prediction routine

X, y, _ = load_img('dataset-test')
X, _ = preprocess(X, y)

clf.predict(X[-1:])

