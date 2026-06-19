#/PyMusic/core.py
import numpy as np
from scipy.io import wavfile
from .data import SAMPLING_RATE

class Wave:#作曲エンジンの中核となる波形クラス
    def __init__(self, data):#波形データを受け取る
        #波形データはnumpyの配列(float32)で管理。
        self.data = np.array(data, dtype=np.float32, copy=True)

    #Wave型チェック
    def _get_data(self, other):
        if isinstance(other, Wave):#型が同じだったら
            return other.data#メンバ変数(np.array)を返す
        return other#それ以外だったらそのまま返す
    
    def _check_key(self, key):#配列成分をintに変換
        if isinstance(key, slice):
            return slice(
                int(key.start) if key.start is not None else None,
                int(key.stop) if key.stop is not None else None,
                key.step
            )
        return key

#波形データを加工するための演算子オーバーライド達

    #wave[a,b]として使いたい
    def __getitem__(self, key):#配列っぽく操作したい
        key = self._check_key(key)
        return Wave(self.data[key])

##四則演算

    #waveY[a:b] = waveXとして使いたい
    def __setitem__(self, key, value):
        key = self._check_key(key)
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

    def out(self, filename):
        data = self.data

        # (1) 正規化（必須）
        max_val = np.max(np.abs(data))
        if max_val > 1.0:
            data = data / max_val

        # (2) float32に統一
        data = data.astype(np.float32)

        wavfile.write(filename, SAMPLING_RATE, data)

__all__ = ["Wave"]#inport * でWaveクラスだけ見せる