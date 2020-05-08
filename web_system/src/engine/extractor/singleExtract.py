
from extractor.feature_extraction import beats, chromaFreq, mfcc, msps, rmse, specBandwidth, specCentroid, specRolloff, zcr

import librosa
import numpy as np
import pandas as pd

import os
import errno
import re

def extract(path):

    if(not os.path.isfile(path)):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    y, sampleRate = librosa.load(path)

    features = np.array([])

    featTempo, featBeats = beats.beats(y, sr=sampleRate)
    ## beats is a list of beat locations, we actually want the number of beats
    featBeats = len(featBeats)
    features = np.append(features, featTempo)
    features = np.append(features, featBeats)

    ## We want the average value for each chroma across the sample. This results in 12 datapoints
    featChromaFreq = chromaFreq.chromaFreq(y, sr=sampleRate).mean(axis=1)
    features = np.append(features, featChromaFreq)

    ## We want the average value for each of the coefficients across the sample. This results in 20 datapoints
    featMfcc = mfcc.mfcc(y, sr=sampleRate).mean(axis=1)
    features = np.append(features, featMfcc)    

    # We want the average energy across the sample. This results in 1 datapoint
    featRmse = rmse.rmse(y).mean()
    features = np.append(features, featRmse)

    # We want the average value across the sample. This results in 1 datapoint
    featSpecBandwidth = specBandwidth.specBandwidth(y, sr=sampleRate).mean()
    features = np.append(features, featSpecBandwidth)

    # We want the average value across the sample. This results in 1 datapoint
    featSpecCentroid = specCentroid.specCentroid(y, sr=sampleRate).mean()
    features = np.append(features, featSpecCentroid)
    
    # We want the average value across the sample. This results in 1 datapoint
    featSpecRolloff = specRolloff.specRolloff(y, sr=sampleRate).mean()
    features = np.append(features, featSpecRolloff)

    # This returns the total number of times we cross the axis. this results in 1 datapoint
    featZcr = zcr.zeroCrossingRate(y)
    features = np.append(features, featZcr)

    ## Define headers
    headers = [
        "tempo",
        "beats",
        *["chroma_freq_{0}".format(x) for x in range(0, 12)],
        *["mfcc_{0}".format(x) for x in range(0,20)],
        "rmse",
        "spectral_bandwidth",
        "spectral_centroid",
        "spectral_rolloff",
        "zero_crossing_rate"
    ]

    ## Convert to a DataFrame
    df = pd.DataFrame(data=[features], columns=headers)

    return(df)

if __name__ == "__main__":
    print(extract("data\\1foruntoldreasonsoftheskies.mp3"))
