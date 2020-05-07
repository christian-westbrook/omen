## Extract the RMSE (Root Mean Square Energy) from an audio file

from librosa.feature import rms
from librosa.util import example_audio_file
import numpy as np
import librosa

## Extraction function
def rmse(audioFile, S=None, frame_length=2048, hop_length=512, center=True, pad_mode='reflect'):
    return(rms(y=audioFile, S=S, frame_length=frame_length, hop_length=hop_length, center=center, pad_mode=pad_mode))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(rmse(y))
    