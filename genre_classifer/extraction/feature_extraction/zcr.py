## Extracts the zero crossing rate from an audio file

from librosa.feature import zero_crossing_rate
from librosa.util import example_audio_file
import librosa

## Extraction function
def zeroCrossingRate(audioFile, frame_length=2048, hop_length=512, center=True, pad=False):
    return(zero_crossing_rate(audioFile, frame_length=frame_length, hop_length=hop_length, center=center, pad=pad).sum())

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(zeroCrossingRate(y))