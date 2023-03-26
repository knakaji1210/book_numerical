# -*- coding: utf-8 -*-
"""
randomwalk.pyプログラム
ランダムウォークシミュレーション
擬似乱数を使って２次元平面を酔歩する
"""

# モジュールのインポート
import random

# メイン実行部
# 試行回数nの初期化
n = int(input("試行回数を入力してください："))
# 乱数の初期化
seed = int(input("乱数の種を入力してください："))
random.seed(seed)

# ランダムウォーク
x = 0.0
y = 0.0
for i in range(n):
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    print("({0:.7f}, {1:.7f})".format(x, y))    # 位置
# randomwalk.pyの終わり