import pandas as pd

import librosa
import numpy as np
import sklearn

# Preprocessing
from sklearn.preprocessing import MinMaxScaler

# Keras
import keras
import tensorflow as tf
from keras import models
from keras import layers
from tensorflow.keras.models import save_model, load_model

import warnings
warnings.filterwarnings('ignore')

import extractor.singleExtract as SE

# Load scaler and fit to data available (Important)
scaler = MinMaxScaler()
training_features = pd.read_csv('./classifier/final_features.csv')
data = training_features.drop(['number'], axis=1)
training_data = scaler.fit_transform(np.array(data.iloc[:, 1:], dtype = float))
# This fits the scaler to training data, and the scaler object is used on new data to scale it similarly to training data
    
