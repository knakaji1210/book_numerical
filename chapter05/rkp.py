# -*- coding: utf-8 -*-
"""
rkp.pyプログラム
ナップサック問題をランダム検索で解くプログラム
"""

# モジュールのインポート
import random

# グローバル変数
weights = [87, 66, 70, 25, 33, 24, 89, 63, 23, 54]  # 重さ
values  = [96, 55, 21, 58, 41, 81, 8, 99, 59, 62]   # 価値
N = len(weights)    # 荷物の個数
SEED = 32767        # 乱数の種
R = 10              # 実験の繰り返し回数

# 下請け関数の定義
# solvekp()関数
def solvekp(p, weightlimit, nlimit, N):
    """問題を解く"""
    maxvalue = 0    # 合計価値の最大値
    mweight = 0   # maxvalue時の重さ
    bestp = [0 for i in range(N)]
    for i in range(nlimit):
        rsetp(p, N) # 乱数による荷物の詰め合わせ
        weight = calcw(p, N)
        if weight <= weightlimit:   # 制限重量以内
            value = calcval(p, N)   # 評価値の計算
        else:
            value = 0   # 重量オーバー
        if value > maxvalue:        # 最良解を更新
            maxvalue = value
            mweight = weight
            for j in range(N):
                bestp[j] = p[j]
    print("最大価値: {0}, 重量：{1}".format(maxvalue, mweight))
    print(bestp)
# solvekp()関数の終わり

# calcw()関数
def calcw(p, N):
    """重量の計算"""
    w = 0
    for i in range(N):
        w += weights[i] * p[i]
    return w
# calcw()関数の終わり

# calcval()関数
def calcval(p, N):
    """評価値の計算"""
    v = 0
    for i in range(N):
        v += values[i] * p[i]
    return v
# calcw()関数の終わり

# rsetp()関数
def rsetp(p, N):
    """乱数による荷物の詰め合わせ"""
    for i in range(N):
        p[i] = int(random.random() * 2) # 0か1のランダム
# rsetp()関数の終わり

# メイン実行部
p = [0 for i in range(N)]   # 問題の答え
# 制限重量の入力
weightlimit = int(input("制限重量を入力してください："))
# 試行回数の入力
nlimit = int(input("試行回数を入力してください："))
# 乱数の初期化
random.seed(SEED)
# 問題を解く
# 実験の繰り返し
for i in range(R):
    solvekp(p, weightlimit, nlimit, N)
# rkp.pyの終わり