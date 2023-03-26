# -*- coding: utf-8 -*-
"""
laplace.pyプログラム
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
"""

# モジュールのインポート
import math

# 定数
lim = 1000      # 反復回数の上限
n = 101         # x軸方向の分割数
m = 101         # x軸方向の分割数

# 下請け関数の定義
# iteration()関数
def iteration(u):
    """1回分の反復計算"""
    u_next = [[0 for i in range(n)] for j in range(m)]  # 次ステップのuij
    # 次のステップの値を計算
    for i in range(1, n-1):
        for j in range(1, m-1):
            u_next[i][j] = (u[i][j-1] + u[i-1][j] + u[i+1][j] + u[i][j+1]) / 4

    # uijの更新
    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i][j] = u_next[i][j]
# iteration()関数の終わり

# メイン実行部
u = [[0 for i in range(n)] for j in range(m)]  # uijの初期化
for i in range(m):
    u[0][i] = math.sin(2 * math.pi * i / (m-1))

# 反復法の計算
for i in range(lim):
    iteration(u)
#    print(u)

# 結果の出力
print(u)
# laplace.pyプログラムの終わり