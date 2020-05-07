## Extract the Chroma Frequencies from an audio file

from librosa.feature import chroma_stft
from librosa.util import example_audio_file
import numpy as np
import librosa

## Extraction function
def chromaFreq(audioFile, sr=22050, S=None, norm=np.inf, n_fft=2048, hop_length=512, win_length=None, window='hann', center=True, pad_mode='reflect', tuning=None, n_chroma=12):
    return(chroma_stft(y=audioFile, sr=sr, S=S, norm=norm, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window, center=center, pad_mode=pad_mode, tuning=None, n_chroma=n_chroma))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(chromaFreq(y))