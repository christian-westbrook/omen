## Extract the Mel-scaled power spectrogram from an audio file

from librosa.feature import melspectrogram
from librosa.util import example_audio_file
import librosa

## Extraction function
def msps(audioFile, sr=22050, S=None, n_fft=2048, hop_length=512, win_length=None, window='hann', center=True, pad_mode='reflect', power=2.0):
    return(melspectrogram(y=audioFile, sr=sr, S=S, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window, center=center, pad_mode=pad_mode, power=power))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(msps(y))