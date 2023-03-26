# -*- coding: utf-8 -*-
"""
life.pyプログラム
ライフゲーム計算プログラム
２次元セルオートマトンの一種である、ライフゲームのプログラム
初期状態ファイルには初期配置を記述する
% python3 life.py < initlife.txt
"""

# モジュールのインポート
import sys
from tkinter.filedialog import askopenfile # sys.exit()の利用に必要
import numpy as np

# 定数
n = 50       # ライフゲームの世界の大きさ
tmax = 3   # 繰り返しの回数

# 下請け関数の定義
# putworld()関数
def putworld(world):
    """worldの状態の出力"""
    # worldの更新
    for i in range(n):
#        print(i)
        for j in range(n):
            print("{:1d}".format(world[i][j]), end="")
        print()
# putworld()関数の終わり

# initworld()関数
def initworld(world):
    """初期値の読み込み"""
    # 初期値を読み込む
    chrworld = sys.stdin.readlines()
    # 内部表現への変換
    for no, line in enumerate(chrworld):
        line = line.rstrip()
        for i in range(len(line)):
            world[no][i] = int(line[i])
# initworld()関数の終わり

# nextt()関数
def nextt(world):
    """worldの状態の更新"""
    # nextworld = [[0 for i in range(n)] for j in range(n)]   # 次世代のworld
    nextworld = np.zeros((n,n), dtype=int)
    # ルールの適用
    for i in range(1, n-1):
        for j in range(1, n-1):
            nextworld[i][j] = calcnext(world, i, j)
    # worldの更新
    for i in range(n):
        for j in range(n):
            world[i][j] = nextworld[i][j]
# nextt()関数の終わり

# calcnext()関数
def calcnext(world, i, j):
    """1セルの状態の更新"""
    no_of_one = 0   # 周囲にある状態1のセルの数
    # 状態1のセルを数える
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            no_of_one += world[x][y]
    no_of_one -= world[i][j]            # 自分自身はカウントしない
    # 状態の更新
    if no_of_one == 3:
        return 1            # 誕生
    elif no_of_one == 2:
        return world[i][j]  # 存続
    return  0               # 上記以外
# calcnext()関数の終わり

# メイン実行部
# world = [[0 for i in range(n)] for j in range(n)]   # worldの初期化、(n x n)の零行列を作る
world = np.zeros((n,n), dtype=int)
# world[][]への初期値の読み込み
initworld(world)
print("t = 0")      # 初期時刻の出力
putworld(world)     # worldの状態の出力

# 時間発展の計算
for t in range(1, tmax):
    nextt(world)                # 次の時刻に更新
    print("t = {0}".format(t))  # 時刻の出力
    putworld(world)             # worldの状態の出力
# life.pyの終わり
