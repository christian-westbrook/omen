import numpy as np
import pandas as pd
import sklearn
from sklearn import *

features = pd.read_csv('./recommender/final_features.csv')
songs = pd.read_csv('./recommender/songs.csv')

data = features.drop(['tempo', 'mfcc_2', 'mfcc_3', 'mfcc_4', 'mfcc_5', 'mfcc_7', 'mfcc_8', 'mfcc_15', 'mfcc_17'], axis=1)

Y = data['number'].copy()
data = data.drop(['number'], axis = 1)

data = pd.get_dummies(data)

xtrain, xtest, ytrain, ytest = model_selection.train_test_split(data, Y, test_size=0.1)

clf = neighbors.NearestNeighbors(n_neighbors=1)
clf.fit(xtrain)

def recommend(song):
    distances, indices = clf.kneighbors(song.iloc[00].drop(labels=['tempo', 'mfcc_2', 'mfcc_3', 'mfcc_4', 'mfcc_5', 'mfcc_7', 'mfcc_8', 'mfcc_15', 'mfcc_17']).to_numpy().reshape(1, -1), n_neighbors=5, return_distance=True)

    import os
    import csv

    with open('reco.csv', 'a+') as csv_file:
        fields = ['track', 'artist', 'genre']
        writer = csv.DictWriter(csv_file, fields)
        writer.writeheader()

    for i in range(5):
        key = ytrain.iloc[indices[0][i]]
        for j in range(songs.shape[0]):
            if songs.iloc[j, 0] == key:
                with open('reco.csv', 'a+') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([songs.iloc[j, 1], songs.iloc[j, 2], songs.iloc[j, 3]])
    recommendations = pd.read_csv('reco.csv')
    os.remove('reco.csv')
    return recommendations
