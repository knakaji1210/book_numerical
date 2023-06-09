# -*- coding: utf-8 -*-
"""
numpy_gauss.pyプログラム
NumPyを用いた連立方程式解法プログラム
"""

# モジュールのインポート
import numpy as np

# グローバル変数
a = np.array([
[4, -1, 0, -1, 0, 0, 0, 0, 0],
[-1, 4, -1, 0, -1, 0, 0, 0, 0],
[0, -1, 4, 0, 0, -1, 0, 0, 0],
[-1, 0, 0, 4, -1, 0, -1, 0, 0],
[0, -1, 0, -1, 4, -1, 0, -1, 0],
[0, 0, -1, 0, -1, 4, 0, 0, -1],
[0, 0, 0, -1, 0, 0, 4, -1, 0],
[0, 0, 0, 0, -1, 0, -1, 4, -1],
[0, 0, 0, 0, 0, -1, 0, -1, 4],
])   # 係数行列
b = np.array([0, 0, 0.25, 0, 0, 0.5, 0.25, 0.5, 1.5])   # 方程式右辺

# メイン実行部
x = np.linalg.solve(a, b)     # 方程式を解く
print(x)    # 結果の出力
# numpy_gauss.pyプログラムの終わり