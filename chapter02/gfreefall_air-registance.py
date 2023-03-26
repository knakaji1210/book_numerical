# -*- coding: utf-8 -*-
"""
gfreefal_air-registance.pyプログラム
自由落下のシミュレーション（Euler version）
自由落下の運動方程式を数値的に解く
matplotlibによるグラフ描画機能付き
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数
g = 9.80665   # 重力加速度
k = 3 * 10e-5

# メイン実行部
t = 0.0         # 時刻t
dt = 0.001  # 時刻の刻み幅

# 係数の入力
v = float(input('初速度v0を入力してください: '))
x = float(input('初期高度x0を入力してください: '))
print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))        # 現在時刻と現在の位置
# グラフデータに現在位置を追加
tlist = [t]
xlist = [x]

# 自由落下の計算
while x >= 0:               # 地面に達するまで計算
    t += dt                 # 時刻の更新
    v += g * dt  - k *  v   # 速度の計算
    x -= v * dt             # 位置の更新
    print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))    # 現在時刻と現在の位置
    # グラフデータに現在位置を追加
    tlist.append(t)
    xlist.append(x)

# グラフの描画
plt.plot(tlist, xlist)  # グラフをプロット

savefile = "./png/gfreefall_air-registance.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()
# gfreefal_air-registance.pyプログラムの終わり