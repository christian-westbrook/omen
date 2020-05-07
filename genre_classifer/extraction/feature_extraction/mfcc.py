## Extracts the Mel Frequency Cepstral Coefficient from an audio file

from librosa import feature
from librosa.util import example_audio_file

import librosa

## Extraction function
def mfcc(audioFile, sr=22050, S=None, n_mfcc=20, dct_type=2, norm="ortho", lifter=0):
    return(feature.mfcc(audioFile, sr=sr, S=S, n_mfcc=n_mfcc, dct_type=dct_type, norm=norm, lifter=lifter))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(mfcc(y))