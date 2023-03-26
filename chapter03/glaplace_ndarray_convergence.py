# -*- coding: utf-8 -*-
"""
glaplace_ndarray_convergence.pyプログラム
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
結果をグラフ表示する
経過時間を計測
numpy.ndarrayを使って高速化
iterationを設定するのではなく、収束条件を課す方法に変更
"""

'''
norm_target = 1e-5
のとき
繰り返し回数：7049
経過時間：0.56320 s
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
n = 101         # x軸方向の分割数
m = 101         # x軸方向の分割数
norm = 1        #
norm_target = 1e-5
iter = 0   # 反復回数

# グラフ描画用
x = np.arange(0, n)
y = np.arange(0, m)

# 下請け関数の定義
# laplace()関数
def laplace(u, iter):
    """1回分の反復計算"""
    u_next = u.copy()
    u[1:-1, 1:-1] = (u[1:-1, 2:] + u[1:-1, 0:-2] + u[2:, 1:-1] + u[0:-2, 1:-1]) / 4
    norm = np.sum(np.abs(u[:] - u_next[:])) / np.sum(np.abs(u_next[:]))
    u[-1, :] = x / (n-1)    # ディリクレ境界
    #u[0, :] = 1 - x / (n-1) # ディリクレ境界
    # u[0, :] = u[1, :]       # ノイマン境界
    iter += 1
    return norm, iter
# laplace()関数の終わり

# メイン実行部
u = np.zeros((n, m))    # uijの初期化 np.zerosで置き換え
u[-1, :] = x / (n-1)    # ディリクレ境界
# u[0, :] = 1 - x / (n-1)   # ディリクレ境界
#u[0, :] = u[1, :]       # ノイマン境界

# 反復法の計算
while norm > norm_target:
    norm, iter = laplace(u, iter)

# 結果の出力
#print(u)

print("繰り返し回数：{0}".format(iter))

end_time = time.process_time()
elapsed_time = end_time - start_time
print('経過時間：{0:.5f} s'.format(elapsed_time))

# グラフ描画
X, Y = np.meshgrid(x, y)
fig = plt.figure()
# ax = Axes3D(fig)      # 本に書かれていた古い形式
ax = fig.add_subplot(111, projection="3d")  # 新しい形式
U = np.array(u)
ax.plot_wireframe(X, Y, U)      # wireframe形式
#ax.plot_surface(X, Y, U, cmap=cm.coolwarm)        # surface形式

savefile = "./png/glaplace_ndarray_convergence.png"
fig.savefig(savefile, format="png", dpi=300)

plt.show()
# glaplace_ndarray_convergence.pyプログラムの終わり