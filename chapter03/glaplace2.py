# -*- coding: utf-8 -*-
"""
glaplace2.pyプログラムその２
境界条件として領域D2を対象とする
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
結果をグラフ表示する
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

# 定数
lim = 1000      # 反復回数の上限
n = 101         # x軸方向の分割数
m = 101       # x軸方向の分割数

# 下請け関数の定義
# iteration()関数
def iteration(u):
    """
    1回分の反復計算
    D2領域の計算用
    """
    u_next = [[0 for i in range(n)] for j in range(m)]  # 次ステップのuij
    # 次のステップの値を計算
    # 下1/4の計算
    for i in range(int(n/4), int((n-1)*3 / 4)):
        for j in range(1, int((m-1) / 4)):
            u_next[i][j] = (u[i][j-1] + u[i-1][j] + u[i+1][j] + u[i][j+1]) / 4

    # 中央1/2の計算
    for i in range(1, n-1):
        for j in range(int((m-1) / 4), int((m-1)*3 / 4)):
            u_next[i][j] = (u[i][j-1] + u[i-1][j] + u[i+1][j] + u[i][j+1]) / 4

    # 上1/4の計算
    for i in range(int(n/4), int((n-1)*3 / 4)):
        for j in range(int((m-1)*3 / 4), m-1):
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
#    u[m-1][i] = math.cos(2 * math.pi * i / (m-1))

# 以下は図3.2 & 3.3用
#    u[0][i] = i / m        # 図3.2 & 3.3
#    u[m-1][i] = (m-i) / m  # 図3.2
#for i in range(n):
#    u[i][m-1] = (m-i) /m   # 図3.3 これの時、lim=1000では足りない

# 反復法の計算
for i in range(lim):
    iteration(u)

# 結果の出力
#print(u)

# グラフ描画
x = np.arange(0, n)
y = np.arange(0, m)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
# ax = Axes3D(fig)      # 本に書かれていた古い形式
ax = fig.add_subplot(111, projection="3d")  # 新しい形式
U = np.array(u)
ax.plot_wireframe(X, Y, U)      # wireframe形式
#ax.plot_surface(X, Y, U, cmap=cm.coolwarm)        # surface形式

savefile = "./png/glaplace2.png"
fig.savefig(savefile, format="png", dpi=300)

plt.show()
# glaplace2.pyプログラムの終わり