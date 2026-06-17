#/PyMusic/core.py
import numpy as np
from scipy.io import wavfile
from .data import SAMPLING_RATE

class Wave:#作曲エンジンの中核となる波形クラス
    def __init__(self, data):#波形データを受け取る
        #波形データはnumpyの配列で管理。
        self.data = np.asarray(data, dtype=np.float32)

    #型チェック
    def _get_data(self, other):
        if isinstance(other, Wave):#型が同じだったら
            return other.data#メンバ変数(np.array)を返す
        return other#それ以外だったらそのまま返す

#波形データを加工するための演算子オーバーライド達

    #wave[a,b]として使いたい
    def __getitem__(self, key):#配列っぽく操作したい
        return Wave(self.data[key])

##四則演算

    #wave[a:b] = valueとして使いたい
    def __setitem__(self, key, value):
        self.data[key] = self._get_data(value)
    
    #wave_A + wave_Bとして使いたい
    def __add__(self, other):#波形データを加算する
        return Wave(
            self.data + self._get_data(other)
        )

    #wave_A - wave_Bとして使いたい
    def __sub__(self, other):#波形データを減算する
        return Wave(
            self.data - self._get_data(other)
        )

    #wave * valとして使いたい
    def __mul__(self, other):#波形データをスカラー倍する
        return Wave(
            self.data * self._get_data(other)
        )

    #wave / valとして使いたい
    def __truediv__(self, other):
        return Wave(
            self.data / self._get_data(other)
        )

    #スカラー倍の逆演算子も定義しておくと幸せになれる
    #(val * waveとしても使えるようになる)
    def __rmul__(self, other):#スカラー倍の逆演算子
        return self * other
    
    #-waveとして使いたい
    def __neg__(self):
        return Wave(-self.data)
    

##再代入演算

    #wave_Y += wave_X
    def __iadd__(self, other):#波形データを加算して再代入する
            self.data += self._get_data(other)
            return self

    #wave_Y -= wave_X
    def __isub__(self, other):#波形データを減算して再代入する
        self.data -= self._get_data(other)
        return self

    #wave_Y *= wave_X
    def __imul__(self, other):#波形データをスカラー倍して再代入する
        self.data *= self._get_data(other)
        return self

##その他便利機能
    
    #len(wave)で長さ取得
    def __len__(self):
        return len(self.data)
    
    #print(wave)で波形の情報を表示
    def __repr__(self):
        return f"Wave(size={len(self.data)})"   

    #wave.out(filename)で出力したい
    def out(self, filename):#波形データを出力
        wavfile.write(filename, SAMPLING_RATE, self.data)

__all__ = ["Wave"]#inpoert * でWaveクラスだけ見せる