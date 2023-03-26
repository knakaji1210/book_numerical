# -*- coding: utf-8 -*-
"""
trape.pyプログラム
数値積分プログラム
台形公式を使って数値積分を行う
"""

# モジュールのインポート
import math

# 定数
SEED = 1    # 乱数の種
R = 10      # 実験の繰り返し回数

# 下請け関数の定義
# fx()関数
def fx(x):
    """積分対象の関数"""
    return math.sqrt(1.0 - x * x)
# fx()関数の終わり

# メイン実行部
# 試行回数nの入力
n = int(input("区間分割数Nを入力してください："))
# 刻み幅の計算
h = 1.0 / n
# 積分値の計算
integral = fx(0.0) / 2.0
for i in range(1, n):
    integral += fx(float(i) / n)
integral += fx(1.0) / 2.0
integral *= h
# 結果の出力
print("積分値I = {0}, 4I = {1}".format(integral, 4*integral))
# trape.pyの終わり
