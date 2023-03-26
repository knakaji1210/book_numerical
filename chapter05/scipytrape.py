# -*- coding: utf-8 -*-
"""
scipytrape.pyプログラム
数値積分プログラム
scipyモジュールを使って数値積分を行う
"""

# モジュールのインポート
import math
import numpy as np
from scipy import integrate

# 下請け関数の定義
# fx()関数
def fx(x):
    """積分対象の関数"""
    return math.sqrt(1.0 - x * x)
# fx()関数の終わり

# メイン実行部
integral = (integrate.quad(fx, 0, 1))[0]  # 計算結果のみ取り出す
# 結果の出力
print("積分値I = {0}, 4I = {1}".format(integral, 4*integral))
# scipytrape.pyの終わり
