import numpy as np
from .core import Wave
from .const import SAMPLING_RATE
def import_wave(FilePath):#ファイルから波形データを取得
    pass

#波形の取得(関数でObjを作る：ファクトリ関数)
def sine(size, freq):#正弦波を生成して取得
    n = np.arange(size)
    return Wave(np.sin(2*np.pi*freq*n/SAMPLING_RATE))
#np.sin(2 * np.pi * freq * n)だと、周波数がSAMPLING_RATEの整数倍のときに常に0になってしまうため、nをSAMPLING_RATEで割る必要がある。

def square(size, freq):#矩形波を生成して取得
    n = np.arange(size)
    return Wave(np.sign(np.sin(2*np.pi*freq*n/SAMPLING_RATE)))

def triangle(size, freq):#三角波を生成して取得
    n = np.arange(size)
    return Wave(2 * np.abs(2 * (n * freq / SAMPLING_RATE - np.floor(0.5 + n * freq / SAMPLING_RATE))) - 1)

def sawtooth(size, freq):#のこぎり波を生成して取得
    n = np.arange(size)
    return Wave(2 * (n * freq / SAMPLING_RATE - np.floor(0.5 + n * freq / SAMPLING_RATE)) - 1)

def noise(size):#ホワイトノイズを生成して取得
    return Wave(np.random.uniform(-1,1,size))

def null(size):#無音を生成して取得(重要)
    return Wave(np.zeros(size))