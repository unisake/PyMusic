import numpy as np

BPM = 120
SAMPLING_RATE = 44100

class Wave:#DAWエンジンの中核となる波形クラス
    def __init__(self, data):#波形データを受け取る
        self.data = data

#波形データを加工するための演算子オーバーロード

    def __mul__(self, val):#波形データをスカラー倍する
        return Wave(self.data * val)

    def __rmul__(self, val):#スカラー倍の逆演算子
        return self * val

    def __add__(self, val):#波形データを加算する
        if isinstance(val, Wave):
            return Wave(self.data + val.data)
        return Wave(self.data + val)
    
    def out(self):#波形データを出力
        pass

#波形の取得(関数でObjを作る：ファクトリ関数)

def import_wave(FilePath):#ファイルから波形データを取得
    pass

def sine(size, freq):#正弦波を生成
    n = np.arange(size)
    return Wave(np.sin(2*np.pi*freq*n/SAMPLING_RATE))
#np.sin(2 * np.pi * freq * n)だと、周波数がSAMPLING_RATEの整数倍のときに常に0になってしまうため、nをSAMPLING_RATEで割る必要がある。

def square(size, freq):#矩形波を生成
    n = np.arange(size)
    return Wave(np.sign(np.sin(2*np.pi*freq*n/SAMPLING_RATE)))

def triangle(size, freq):#三角波を生成
    n = np.arange(size)
    return Wave(2 * np.abs(2 * (n * freq / SAMPLING_RATE - np.floor(0.5 + n * freq / SAMPLING_RATE))) - 1)

def sawtooth(size, freq):#のこぎり波を生成
    n = np.arange(size)
    return Wave(2 * (n * freq / SAMPLING_RATE - np.floor(0.5 + n * freq / SAMPLING_RATE)) - 1)

def noise(size):
    return Wave(np.random.uniform(-1,1,size))

def null(size):
    return Wave(np.zeros(size))

#今こんな感じ