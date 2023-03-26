# -*- coding: utf-8 -*-
"""
ri.pyプログラム
乱数による数値積分プログラム
擬似乱数を使って数値積分を行う
"""

# モジュールのインポート
import random

# 定数
SEED = 1    # 乱数の種
R = 10      # 実験の繰り返し回数

# メイン実行部
# 試行回数nの入力
n = int(input("試行回数nを入力してください："))
# 乱数の初期化
random.seed(SEED)
# 積分実験の繰り返し
for r in range(R):
    integral = 0
    # 積分値の計算
    for i in range(n):
        x = random.random()
        y = random.random()
        if (x * x + y * y) <= 1:    # 円の内部 
            integral += 1
    # 結果の出力
    res = float(integral) / n
    print("積分値I = {0}, 4I = {1}".format(res, 4*res))
# ri.pyの終わり
