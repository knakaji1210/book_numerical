# -*- coding: utf-8 -*-
"""
gefield_ani.pyプログラム
2次元運動のシミュレーション
電界中の荷電粒子のシミュレーション
matplotlibによるグラフ描画機能付き
アニメーション化バージョン
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math

def particlePosition(t, x, y, vx, vy, qList):
    # 定数
    tLimit = 20                 # シミュレーション打ち切り時間
    rLimit = 0.1                # 距離rの最低値
    dt = 0.01                   # 時刻の刻み幅
 
    xList = [x]
    yList = [y]
    imgs = []

    # 2次元運動の計算
    while t < tLimit:           # 打ち切り時間まで計算
        t += dt                 # 時刻の更新
        rmin = float("inf")     # 距離の最小値を初期化（浮動小数点数float型の無限大inf）
        for qi in qList:
            rx = qi[0][0] - x   # 位置rxの計算
            ry = qi[0][1] - y   # 位置ryの計算
            r = math.sqrt(rx * rx + ry * ry)    # 距離rの計算
            if r < rmin:
                rmin = r        # 距離の最小値を更新
            vx += (rx /r /r /r * qi[1]) * dt    # 速度vxの計算
            vy += (ry /r /r /r * qi[1]) * dt    # 速度vyの計算
        x += vx * dt            # 位置xの更新
        y += vy * dt            # 位置yの更新
        # 現在時刻と現在の位置
        print('時刻：{0:.7f}, 位置x：{1:.7f}, 位置y：{2:.7f}, 速度x：{3:.7f}, 速度y：{4:.7f}'.format(t, x, y, vx, vy))
        # 電荷位置のプロット
        for qi in qList:
            charge = qi[1]
            if charge > 0:
                c = "red"
            if charge < 0:
                c = "blue"
            qimg = plt.plot(qi[0][0], qi[0][1], "o", color =c)
        # グラフデータに現在位置を追加
        xList.append(x)
        yList.append(y)
        img = plt.plot(xList, yList, ".", color="black")
        img += qimg
        imgs.append(img)   
        if rmin < rLimit:
            break   # 電荷に非常に近づいたら終了
    return imgs

# メイン実行部
t = 0.0         # 時刻t
# 定数
qList = (((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0))    # 電荷の位置と値

# 係数の入力
vx0 = float(input('初速度v0xを入力してください: '))
vy0 = float(input('初速度v0yを入力してください: '))
x0 = float(input('初期位置x0を入力してください: '))
y0 = float(input('初期位置y0を入力してください: '))

vx = vx0
vy = vy0
x = x0
y = y0

# 現在時刻と現在の位置
print('時刻：{0:.7f}, 位置x：{1:.7f}, 位置y：{2:.7f}, 速度x：{3:.7f}, 速度y：{4:.7f}'.format(t, x, y, vx, vy))
# グラフデータに現在位置を追加

fig_title = "Two-dimensional motion of charged particles"
plot_lim = 10

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='X', ylabel='Y',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

imgs = particlePosition(t, x, y, vx, vy, qList)

# グラフの表示 & アニメーション
ani = animation.ArtistAnimation(fig, imgs, interval=1)
ani.save('./gif/gefield_ani.gif', writer = 'pillow', fps = 1000)

plt.show()
plt.close()
# gefield_ani.pyプログラムの終わり