from genre_classifer.feature_extraction import beats, chromaFreq, mfcc, msps, rmse, specBandwidth, specCentroid, specRolloff, zcr

import librosa
import numpy as np
import pandas as pd

import os
import glob
import re

## This extraction function is specifically tuned to work with gztan dataset, but the extension can be changed
def extract(path, extension="wav"):
    
    ## Get all files
    files = glob.glob("{0}/**/*.{1}".format(path, extension), recursive=True)

    ## Extract label, filename. group 1 is label, group 2 is number
    pattern = re.compile(r"(\w+)\.(\w+)\.".format(extension))

    features = []

    ## Iterate over files, extracting features
    for fileName in files:
        m = pattern.search(fileName)
        label = m.group(1)
        number = m.group(2)

        print("Processing: {0}".format(fileName))

        y, sampleRate = librosa.load(fileName)

        feat = np.array([])

        ## identifying information
        feat = np.append(feat, label)
        feat = np.append(feat, number)

        featTempo, featBeats = beats.beats(y, sr=sampleRate)
        ## beats is a list of beat locations, we actually want the number of beats
        featBeats = len(featBeats)
        feat = np.append(feat, featTempo)
        feat = np.append(feat, featBeats)

        ## We want the average value for each chroma across the sample. This results in 12 datapoints
        featChromaFreq = chromaFreq.chromaFreq(y, sr=sampleRate).mean(axis=1)
        feat = np.append(feat, featChromaFreq)

        ## We want the average value for each of the coefficients across the sample. This results in 20 datapoints
        featMfcc = mfcc.mfcc(y, sr=sampleRate).mean(axis=1)
        feat = np.append(feat, featMfcc)

        #featMsps = msps.msps(y, sr=sampleRate)
        #print(featMsps.shape)

        # We want the average energy across the sample. This results in 1 datapoint
        featRmse = rmse.rmse(y).mean()
        feat = np.append(feat, featRmse)

        # We want the average value across the sample. This results in 1 datapoint
        featSpecBandwidth = specBandwidth.specBandwidth(y, sr=sampleRate).mean()
        feat = np.append(feat, featSpecBandwidth)

        # We want the average value across the sample. This results in 1 datapoint
        featSpecCentroid = specCentroid.specCentroid(y, sr=sampleRate).mean()
        feat = np.append(feat, featSpecCentroid)
        
        # We want the average value across the sample. This results in 1 datapoint
        featSpecRolloff = specRolloff.specRolloff(y, sr=sampleRate).mean()
        feat = np.append(feat, featSpecRolloff)

        # This returns the total number of times we cross the axis. this results in 1 datapoint
        featZcr = zcr.zeroCrossingRate(y)
        feat = np.append(feat, featZcr)

        features.append(feat)

    print("Finished processing {0} files.".format(len(files)))
    return(np.array(features))


def saveCsv(features, fileName):
    
    print("Saving csv")

    ## Define headers
    headers = [
        "label",
        "number",
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
    df = pd.DataFrame(data=features, columns=headers)

    ## Save CSV
    df.to_csv(fileName, index=False)

    print("Saved csv as {0}".format(fileName))


def extractFma():

    BATCH_SIZE = 500

    trackDf = pd.read_csv("{0}/data/fma/tracks.csv".format(os.getcwd()))

    files = glob.glob("{0}/data/fma_small/**/*.{1}".format(os.getcwd(), "mp3"), recursive=True)

    pattern = re.compile(r"\d+\\(\w+)\.mp3")

    i = 0

    for j in range(4000, len(files), BATCH_SIZE):

        features = []

        ## Iterate over files, extracting features
        for fileName in files[j:j+BATCH_SIZE]:
            try:
                i += 1

                m = pattern.search(fileName)

                trackNumber = str(int(m.group(1)))
                label = trackDf.loc[trackDf["track_id"] == trackNumber]["genre_top"]
                #print(label)

                print("Processing {1}/{2}: {0}".format(fileName, i, len(files)))

                y, sampleRate = librosa.load(fileName)

                feat = np.array([])

                ## identifying information
                feat = np.append(feat, label)
                feat = np.append(feat, trackNumber)

                featTempo, featBeats = beats.beats(y, sr=sampleRate)
                ## beats is a list of beat locations, we actually want the number of beats
                featBeats = len(featBeats)
                feat = np.append(feat, featTempo)
                feat = np.append(feat, featBeats)

                ## We want the average value for each chroma across the sample. This results in 12 datapoints
                featChromaFreq = chromaFreq.chromaFreq(y, sr=sampleRate).mean(axis=1)
                feat = np.append(feat, featChromaFreq)

                ## We want the average value for each of the coefficients across the sample. This results in 20 datapoints
                featMfcc = mfcc.mfcc(y, sr=sampleRate).mean(axis=1)
                feat = np.append(feat, featMfcc)

                #featMsps = msps.msps(y, sr=sampleRate)
                #print(featMsps.shape)

                # We want the average energy across the sample. This results in 1 datapoint
                featRmse = rmse.rmse(y).mean()
                feat = np.append(feat, featRmse)

                # We want the average value across the sample. This results in 1 datapoint
                featSpecBandwidth = specBandwidth.specBandwidth(y, sr=sampleRate).mean()
                feat = np.append(feat, featSpecBandwidth)

                # We want the average value across the sample. This results in 1 datapoint
                featSpecCentroid = specCentroid.specCentroid(y, sr=sampleRate).mean()
                feat = np.append(feat, featSpecCentroid)
                
                # We want the average value across the sample. This results in 1 datapoint
                featSpecRolloff = specRolloff.specRolloff(y, sr=sampleRate).mean()
                feat = np.append(feat, featSpecRolloff)

                # This returns the total number of times we cross the axis. this results in 1 datapoint
                featZcr = zcr.zeroCrossingRate(y)
                feat = np.append(feat, featZcr)

                features.append(feat)
            except:
                print("error extracting {0}".format(fileName))

        saveCsv(features, "data/features{0}.csv".format(j))


if __name__ == "__main__":
    features = extractFma()
    #extractFma()