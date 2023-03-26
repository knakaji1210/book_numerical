# -*- coding: utf-8 -*-
"""
godefreefall_with-error.pyプログラム
自由落下のシミュレーション
自由落下の運動方程式を数値的に解く
SciPyのodeモジュールを利用する
matplotlibによるグラフ描画機能付き
理論式との比較も追加
"""

# モジュールのインポート
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定数
g = 9.80665   # 重力加速度

# 下請け関数の定義
# f()関数
def f(x, t):
    """微分方程式の右辺を与える"""
    return [x[1], -g]
# f()関数の終わり

# メイン実行部
# 係数の入力
v0 = float(input('初速度v0を入力してください: '))
x0 = float(input('初期高度x0を入力してください: '))

# 自由落下の計算
xv0 = [x0, v0]                     # 初期条件の設定
t = np.arange(0, 4.53, 0.01)    # 0~4.53秒までを0.01秒刻みで計算
x = odeint(f, xv0, t)            # 計算の本体
xt = [x0 + v0*tim - (1/2)*g*tim**2 for tim in t]    # 理論式による位置の計算

xList = []

for xvalue in x:
    xList.append(xvalue[0])

diff = [xn - xt for (xn, xt) in zip(xList, xt)]
ylim = 2*np.max(np.abs(diff))

# グラフの描画
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(t, xList, label="SciPy ODE")  # グラフをプロット
ax1.plot(t, xt, linestyle="dashed", label="Theory")  # グラフをプロット
ax2.plot(t, diff, label="Difference")  # グラフをプロット
ax1.legend()
ax1.grid()
ax2.legend()
ax2.set_ylim(-ylim,ylim)
ax2.grid()

savefile = "./png/godefreefall_with_error.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()

# godefreefall_with-error.pyプログラムの終わり