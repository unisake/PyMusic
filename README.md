# pyで作曲してみる

## clone
```sh
git clone https://github.com/unisake/PyMusic.git
```

## ライブラリ

- numpy #配列高速計算
- skapy #wav入出力

```sh
python -m venv venv
venv\Scripts\activate
```
`(venv) PS C:\...`になるはず
```sh
#(venv) PS C:\...で
pip install numpy scipy
pip list #確認
```
## 作曲操作の定義

波形A,B,C... → DAW → 出力波形X

## 基本ステータス
`./PyMusic/const.py`
### 拍
```py
BPM = 120 #一分間の拍数
SAMPLING_RATE = 44100 #一秒間のサンプリング数

beat = SAMPLING_RATE * 60 // BPM #一拍のサンプリング数
```
### 音階
root(根音)を決めて、そこからの度数(移動量)を、
ベクトルで表現。
```py
major = [0,2,4,5,7,9,11] #半音 = 1,全音 = 半音 * 2 = 2
Cmajor = Scale("C", major, 4) #(root, scale, base_octave)
Cmajor[1]  # C4
Cmajor[2]  # D4
Cmajor[5,1]#G +1 octave
Cmajor[5,1,+1]  # G#5
```

## 波形の入手方法
`./PyMusic/get_wave.py`
### 基本波形を生成
```py
wave = triangle_wave(size,Cmajor[1]) #三角波
wave = square_wave(size,Cmajor[2]) #矩形波
wave = sine_wave(size,Cmajor[5,1]) #サイン波
wave = null_wave(size) #空データ(重要)
```
組み込み変数みたいにソフト側で用意されてる波形

### 外部波形をインポート
```py
wave = import("example.wav")
```
録音した物やエクスポートしたwavを読み込む措置

## 波形の合成
`/PyMusic/core.py`
### 演算子で合成・増幅等を行う
```py
#置き換え
wave_y[a,b] = wave_x
#加算合成
wave_y[a,b] += wave_x
#位相反転
-wave_x
#減算合成
wave_y[a,b] -= wave_x
#増幅(音量を上げる)
wave_x * val
#減衰(音量を下げる)
wave_x -= wave_x * val
```
### 具体的な使用例
```py

```

### 完成したwaveデータをwavで出力
```py
wabe[start,end].out(wav) #今後の拡張でデータ形式を増やす余地
```
