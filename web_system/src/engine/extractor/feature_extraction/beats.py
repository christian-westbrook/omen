## Extract the beats and tempo from an audio file

from librosa.beat import beat_track
from librosa.util import example_audio_file
import librosa

## Extraction function (returns tempo, beats)
def beats(audioFile, sr=22050, onset_envelope=None, hop_length=512, start_bpm=120.0, tightness=100, trim=True, bpm=None, prior=None, units='frames'):
    return(beat_track(y=audioFile, sr=sr, onset_envelope=onset_envelope, hop_length=hop_length, start_bpm=start_bpm, tightness=tightness, trim=trim, bpm=bpm, prior=prior, units=units))

## If this file is run stand-alone, test the extraction against the example audio file
if __name__ == "__main__":
    y, sampleRate = librosa.load(example_audio_file())
    print(beats(y))
    