#/PyMusic/data.py
BPM = 120#一分間の拍数
SAMPLING_RATE = 44100#一秒間のサンプリング数

beat = SAMPLING_RATE * 60 // BPM #一拍のサンプリング数

class Scale:
    _A4_FREQ = 440.0
    _A4_MIDI = 69
    _SEMITONES_PER_OCTAVE = 12
    _MAJOR = [0,2,4,5,7,9,11]
    _NOTE = {
        "C": 0,
        "C#": 1,
        "D": 2,
        "D#": 3,
        "E": 4,
        "F": 5,
        "F#": 6,
        "G": 7,
        "G#": 8,
        "A": 9,
        "A#": 10,
        "B": 11,
    }
    
    def __init__(self, root, scale=None, base_octave=4):
        if root not in self._NOTE:
            raise ValueError(
                f"unknown note: {root}"
            )
        self._root = self._NOTE[root]
        self._scale = scale or self._MAJOR
        self._base_octave = base_octave
    def __getitem__(self, key):
        if not isinstance(key, tuple):
            key = (key,)

        degree = key[0]

        #オクターブの指定がない場合は0とする
        octave = key[1] if len(key) >= 2 else 0

        #シャープやフラットの指定がない場合は0とする
        accidental = key[2] if len(key) >= 3 else 0

        #0度は存在しないためエラー
        if degree < 1:
            raise ValueError("degree starts from 1")

        #スケールの長さを超えるとエラー
        if degree > len(self._scale):
            raise ValueError(
                f"degree must be 1-{len(self._scale)}"
            )
        
        semitone = self._scale[degree - 1]

        midi = (
            self._root
            + semitone
            + self._SEMITONES_PER_OCTAVE
              * (self._base_octave + octave + 1)
            + accidental
        )

        return self._A4_FREQ * 2 ** ((midi - self._A4_MIDI) / self._SEMITONES_PER_OCTAVE)

__all__ = ["BPM","SAMPLING_RATE","beat","Scale"]