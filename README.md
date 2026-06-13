# pyで作曲してみる

## ライブラリ

- numpy #配列高速計算
- skapy #wav入出力

```sh
python -m venv venv
venv\Scripts\activate
```
`(venv) PS C:\...`
```sh
pip install numpy scipy
pip list
```
## 作曲操作の定義

波形A,B,C... → DAW → 出力波形X

## 波形の入手方法

### 基本波形を生成
```py
#※引数は音階の英語表記
wave = triangle_wave(C1) #三角波
wave = square_wave(D1) #矩形波
wave = sine_wave(E1) #サイン波
wave = null_wave() #空データ(重要)
```
組み込み変数みたいにソフト側で用意されてる波形

### 外部波形をインポート
```py
wave = import("example.wav")
```
録音した物やエクスポートしたwavを読み込む措置

### 演算子で合成・増幅等を行う

```py
#置き換え
wave_y[a,b] = wave_x
#加算合成
wave_y[a,b] += wave_x
#移送反転
-wave_x
#減算合成
wave_y[a,b] -= wave_x
#増幅
wave_x * val
#音量を下げる
wave_x -= wave_x * val
```

### 完成したwaveデータをwavで出力
```py
wabe[start,end].out(wav) #今後の拡張でデータ形式を増やす余地
```
