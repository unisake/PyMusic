#/PyMusic/data.py
BPM = 120#一分間の拍数
SAMPLING_RATE = 96000#一秒間のサンプリング数

beat = int(SAMPLING_RATE * 60 / BPM) #一拍のサンプリング数

class Scale:#音階インスタンスを作って周波数を出力したいクラス
    ##もろもろ定数たち
    _A4_FREQ = 440.0 #基準はラの音
    _A4_MIDI = 69 #ラのMIDI番号
    _scale_offsetS_PER_OCTAVE = 12 #一オクターブ == 12平均律
    _MAJOR = [0,2,4,5,7,9,11] #スケールのデフォ値はメジャー
    _NOTE = {#MIDIノートを列挙(実は根音Cからの移動量ベクトル)
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
    
    def __init__(self, root, scale=None, base_octave=None):#コントラクタ(根音,スケール,基準オクターブ)
        if root not in self._NOTE:#根音が無かったらエラー
            raise ValueError(
                f"unknown note: {root}"
            )
        self._root = self._NOTE[root]#MIDIスケール(どの音なのかを)でroot取得して代入
        self._scale = scale or self._MAJOR#代入、無かったらデフォ値(メジャースケール)を代入
        self._base_octave = 4 if base_octave is None else base_octave#代入、無かったらデフォ値(メジャースケール)を代入
    def __getitem__(self, key):#インスタンスを配列[a,b,c]で扱う
        if not isinstance(key, tuple):
            key = (key,)

        degree = key[0] #a：根音からの移動量

        #b：オクターブ指定(オクターブの指定がない場合は0とする)
        octave = key[1] if len(key) >= 2 else 0

        #c：半音指定(シャープやフラットの指定がない場合は0とする)
        accidental = key[2] if len(key) >= 3 else 0

        #音楽界隈に0度は存在しないためエラー
        if degree < 1:#0はインドが発明したからね
            raise ValueError("degree starts from 1")#西洋音楽理論には無いのさ

        #スケールの長さを超えるとエラー
        if degree > len(self._scale):
            raise ValueError(
                f"degree must be 1-{len(self._scale)}"
            )
        
        #根音からの移動量を計算
        scale_offset = self._scale[degree - 1]#度数表現を配列に直してる

        midi = (
            self._root#基準点(根音)
            + scale_offset#移動量
            + self._scale_offsetS_PER_OCTAVE#12平均律
              * (self._base_octave + octave + 1)
            + accidental#半音指定
        )

        #実際に周波数を計算して出力
        return self._A4_FREQ * 2 ** ((midi - self._A4_MIDI) / self._scale_offsetS_PER_OCTAVE)

__all__ = ["BPM","SAMPLING_RATE","beat","Scale"]