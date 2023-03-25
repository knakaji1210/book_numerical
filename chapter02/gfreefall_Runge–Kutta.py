# -*- coding: utf-8 -*-
"""
gfreefall_Runge–Kutta.pyプログラム
自由落下のシミュレーション（Runge–Kutta version）
自由落下の運動方程式を数値的に解く
matplotlibによるグラフ描画機能付き
理論式との比較も追加
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数
g = 9.80665   # 重力加速度

# メイン実行部
t = 0.0         # 時刻t
dt = 0.01  # 時刻の刻み幅

# 係数の入力
v0 = float(input('初速度v0を入力してください: '))
x0 = float(input('初期高度x0を入力してください: '))
v = v0
x = x0
print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))        # 現在時刻と現在の位置
# グラフデータに現在位置を追加
tlist = [t]
xlist = [x0]
xtlist = [x0]
difflist = [0]

# 自由落下の計算
while x >= 0:           # 地面に達するまで計算
    t += dt        # 時刻の更新
    k1 = v*dt
    l1 = -g*dt
    k2 = (v + l1/2)*dt
    l2 = -g*dt
    k3 = (v + l2/2)*dt
    l3 = -g*dt
    k4 = (v + l3)*dt
    l4 = -g*dt
    v += (1/6)*(l1 + 2*l2 + 2*l3 + l4)    # 速度の計算
    x += (1/6)*(k1 + 2*k2 + 2*k3 + k4)   # 位置の更新
    xt = x0 + v0*t - (1/2)*g*t**2   # 理論式による位置の計算
    diff = x - xt
    print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))    # 現在時刻と現在の位置
    tlist.append(t)
    xlist.append(x)
    xtlist.append(xt)
    difflist.append(diff)

ylim = 2*np.max(np.abs(difflist))

# グラフの描画
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(tlist, xlist, label="Runge–Kutta")  # グラフをプロット
ax1.plot(tlist, xtlist, linestyle="dashed", label="Theory")  # グラフをプロット
ax2.plot(tlist, difflist, label="Difference")  # グラフをプロット
ax1.legend()
ax1.grid()
ax2.legend()
ax2.set_ylim(-ylim,ylim)
ax2.grid()
plt.show()
# freefall_Runge–Kutta.pyプログラムの終わり