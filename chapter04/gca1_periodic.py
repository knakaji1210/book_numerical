# -*- coding: utf-8 -*-
"""
gca1_periodic.pyプログラム
セルオートマトン（１次元）計算プログラム
ルールと初期状態から、時間発展を計算する
結果をグラフ描画する
使い方 % python3 gcal_periodic.py
周期的境界条件用に変更
"""

# モジュールのインポート
import sys # sys.exit()の利用に必要
import numpy as np
import matplotlib.pyplot as plt

# 定数
n = 256         # セルの最大個数
r = 8           # ルール表の大きさ
tmax = 256      # 繰り返しの回数

# 下請け関数の定義

def setrule(rule, ruleno):
    """ルール表の初期化"""
    # ルール表の書き込み
    for i in range(0, r):
        rule[i] = ruleno % 2    # 剰余
        ruleno = ruleno // 2    # 整数除算、左シフト
    # ルールの出力
    for i in range(r - 1, -1, -1):  # (r-1)から-1まで-1ずつ
        print(rule[i])
# setrule()関数の終わり

# initca()関数
def initca(ca):
    """セルオートマトンへの初期値の読み込み"""
    # 初期値を読み込む
    line = input("caの初期値を入力してください：")
    print()
    # 内部表現への変換
    for no in range(len(line)):
        ca[no] = int(line[no])
# initca()関数の終わり

# putca()関数
def putca(ca):
    """caの状態の出力"""
    # 初期値を読み込む
    for no in range(n-1, -1, -1):
        print("{:1d}".format(ca[no]), end="")   # end="" は改行の抑制d
    print()
# putca()関数の終わり

# nextt()関数
def nextt(ca, rule):
    """caの状態の更新"""
    nextca = [0 for i in range(n)]      # 次世代のca
    # ルールの適用
    nextca[0] = rule[ca[1] * 4 + ca[0] * 2 + ca[n-1]]       # 周期的境界条件
    nextca[n-1] = rule[ca[0] * 4 + ca[n-1] * 2 + ca[n-2]]   # 周期的境界条件
    for i in range(1, n-1):
        nextca[i] = rule[ca[i + 1] * 4 + ca[i] * 2 + ca[i - 1]]
    # caの更新
    for i in range(n):
        ca[i] = nextca[i]
# nextca()関数の終わり

# メイン実行部
outputdata = [[0 for i in range(n)] for j in range(tmax + 1)]
# ルール表の初期化
rule = [0 for i in range(r)]    # ルール表の作成
ruleno = int(input("ルール番号を入力してください："))
print()
if ruleno < 0 or ruleno > 255:
    print("ルール番号が正しくありません（{}）".format(ruleno))
    sys.exit()
setrule(rule, ruleno)   # ルール表をセット

# セルオートマトンへの初期値の読み込み
ca = [0 for i in range(n)]  # セルの並び
initca(ca)  # 初期値読み込み
putca(ca)   # caの状態の出力

for i in range(n):
    outputdata[0][i] = ca[i]

# 時間発展の計算
for t in range(tmax):
    nextt(ca, rule) # 次の時刻に更新
    putca(ca)       # caの状態の出力
    for i in range(n):
        outputdata[t + 1][i] = ca[i]

# グラフ出力
plt.imshow(outputdata)

savefile = "./png/gca1_periodic.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()

# gca1.pyの終わり
