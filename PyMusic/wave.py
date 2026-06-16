#/PyMusic/wave.py
import numpy as np
import wave

from .core import Wave
from .data import SAMPLING_RATE

#波形の取得(関数でObjを作る：ファクトリ関数)

def import_wave(FilePath):#ファイルから波形データを取得
    # WAVファイルを開く
    with wave.open(FilePath, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()

        raw = wf.readframes(n_frames)

    # dtype決定（ここ重要）
    if sampwidth == 1:
        dtype = np.uint8  # 8bit WAV
    elif sampwidth == 2:
        dtype = np.int16  # 16bit WAV（一般的）
    elif sampwidth == 4:
        dtype = np.int32
    else:
        raise ValueError("Unsupported sample width")

    audio = np.frombuffer(raw, dtype=dtype)

    # ステレオならmonoにまとめる（簡易処理）
    if n_channels > 1:
        audio = audio.reshape(-1, n_channels)
        audio = audio.mean(axis=1)

    # 正規化（-1〜1に揃える）
    if dtype == np.uint8:
        audio = (audio - 128) / 128.0
    elif dtype == np.int16:
        audio = audio / 32768.0
    elif dtype == np.int32:
        audio = audio / 2147483648.0

    return Wave(audio.astype(np.float32))

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

__all__ = ["import_wave","sine","square","triangle","sawtooth","noise","null"]