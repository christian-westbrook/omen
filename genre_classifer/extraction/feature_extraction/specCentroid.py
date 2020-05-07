## Extract the Spectral Centroid from an audio file

from librosa.feature import spectral_centroid
from librosa.util import example_audio_file
import librosa

## Extraction function
def specCentroid(audioFile, sr=22050, S=None, n_fft=2048, hop_length=512, freq=None, win_length=None, window='hann', center=True, pad_mode='reflect'):
    return(spectral_centroid(y=audioFile, sr=sr, S=S, n_fft=n_fft, hop_length=hop_length, freq=freq, win_length=win_length, window=window, center=center, pad_mode=pad_mode))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(specCentroid(y))