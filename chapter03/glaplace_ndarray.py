# -*- coding: utf-8 -*-
"""
glaplace_ndarray.pyプログラム
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
結果をグラフ表示する
経過時間を計測
numpy.ndarrayを使って高速化
"""

'''
リストのとき
elapsed time = 4.72803 s
ndarrayのとき
elapsed time = 0.04391 s
'''

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
import time

start_time = time.process_time()

# 定数
lim = 1000      # 反復回数の上限
n = 101         # x軸方向の分割数
m = 101       # x軸方向の分割数

# グラフ描画用
x = np.arange(0, n)
y = np.arange(0, m)

# 下請け関数の定義
# iteration()関数
def iteration(u):
    """1回分の反復計算"""
    u[1:-1, 1:-1] = (u[1:-1, 2:] + u[1:-1, 0:-2] + u[2:, 1:-1] + u[0:-2, 1:-1]) / 4
# iteration()関数の終わり

# メイン実行部
u = np.zeros((n, m))    # uijの初期化 np.zerosで置き換え
u[-1, :] = x / (n-1)

# 反復法の計算
for i in range(lim):
    iteration(u)

# 結果の出力
#print(u)

end_time = time.process_time()
elapsed_time = end_time - start_time
print('elapsed time = {0:.5f} s'.format(elapsed_time))

# グラフ描画
X, Y = np.meshgrid(x, y)
fig = plt.figure()
# ax = Axes3D(fig)      # 本に書かれていた古い形式
ax = fig.add_subplot(111, projection="3d")  # 新しい形式
U = np.array(u)
ax.plot_wireframe(X, Y, U)      # wireframe形式
#ax.plot_surface(X, Y, U, cmap=cm.coolwarm)        # surface形式

savefile = "./png/glaplace_ndarray.png"
fig.savefig(savefile, format="png", dpi=300)

plt.show()
# glaplace_ndarray.pyプログラムの終わり