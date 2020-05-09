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

def classify(features):
    # Transform input
    X = scaler.transform(features) # Use scaler object fit on training data

    # Load model
    model = load_model('./classifier/final_deploy_model.h5')
    
    # Predict
    prediction = model.predict(X)

    # Append
    predictionIndex = np.argmax(prediction)

    if predictionIndex == 0:
        features['label_Electronic'] = [1.0]
    else:
        features['label_Electronic'] = [0.0]

    if predictionIndex == 1:
        features['label_Experimental'] = [1.0]
    else:
        features['label_Experimental'] = [0.0]

    if predictionIndex == 2:
        features['label_Folk'] = [1.0]
    else:
        features['label_Folk'] = [0.0]

    if predictionIndex == 3:
        features['label_Hip-Hop'] = [1.0]
    else:
        features['label_Hip-Hop'] = [0.0]

    if predictionIndex == 4:
        features['label_Instrumental'] = [1.0]
    else:
        features['label_Instrumental'] = [0.0]

    if predictionIndex == 5:
        features['label_International'] = [1.0]
    else:
        features['label_International'] = [0.0]

    if predictionIndex == 6:
        features['label_Pop'] = [1.0]
    else:
        features['label_Pop'] = [0.0]

    if predictionIndex == 7:
        features['label_Rock'] = [1.0]
    else:
        features['label_Rock'] = [0.0]
    
    # Return
    return features
