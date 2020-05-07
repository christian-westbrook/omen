## Extract the Spectral Bandwidth from an audio file

from librosa.feature import spectral_rolloff
from librosa.util import example_audio_file
import librosa

## Extraction function
def specRolloff(audioFile, sr=22050, S=None, n_fft=2048, hop_length=512, win_length=None, window='hann', center=True, pad_mode='reflect', freq=None, roll_percent=0.85):
    return(spectral_rolloff(y=audioFile, sr=sr, S=S, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window, center=center, pad_mode=pad_mode, freq=freq, roll_percent=roll_percent))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(specRolloff(y))
    