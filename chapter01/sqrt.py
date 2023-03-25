# -*- coding: utf-8 -*-
"""
sqrt.pyプログラム
mathモジュールを利用して平方根を求める
"""

# モジュールのインポート
import math

# メイン実行部
# 入力
x = float(input('正の平方根を求めたい値を入力: '))
# 出力
print("sqrt({0:.1f}) = {1:.10f}".format(x, math.sqrt(x)))
# sqrt.pyの終わり