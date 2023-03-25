# -*- coding: utf-8 -*-
"""
efield.pyプログラム
2次元運動のシミュレーション
電界中の荷電粒子のシミュレーション
"""

# モジュールのインポート
import math

# 定数
qList = (((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0))    # 電荷の位置と値
tLimit = 20                                  # シミュレーション打ち切り時間
rLimit = 0.1                                    # 距離rの最低値
dt = 0.01                                       # 時刻の刻み幅

# メイン実行部
t = 0.0         # 時刻t

# 係数の入力
vx = float(input('初速度v0xを入力してください: '))
vy = float(input('初速度v0yを入力してください: '))
x = float(input('初期位置xを入力してください: '))
y = float(input('初期位置yを入力してください: '))

# 現在時刻と現在の位置
print('時刻：{0:.7f}, 位置x：{1:.7f}, 位置y：{2:.7f}, 速度x：{3:.7f}, 速度y：{4:.7f}'.format(t, x, y, vx, vy))

# 2次元運動の計算
while t < tLimit:           # 打ち切り時間まで計算
    t += dt                 # 時刻の更新
    rmin = float("inf")     # 距離の最小値を初期化（浮動小数点数float型の無限大inf）
    for qi in qList:
        rx = qi[0][0] - x    # 位置rxの計算
        ry = qi[0][1] - y    # 位置ryの計算
        r = math.sqrt(rx * rx + ry * ry)    # 距離rの計算
        if r < rmin:
            rmin = r        # 距離の最小値を更新
        vx += (rx /r /r /r * qi[1]) * dt    # 速度vxの計算
        vy += (ry /r /r /r * qi[1]) * dt    # 速度vyの計算
    x += vx * dt    # 位置xの更新
    y += vy * dt    # 位置yの更新
    # 現在時刻と現在の位置
    print('時刻：{0:.7f}, 位置x：{1:.7f}, 位置y：{2:.7f}, 速度x：{3:.7f}, 速度y：{4:.7f}'.format(t, x, y, vx, vy))
    if rmin < rLimit:
        break   # 電荷に非常に近づいたら終了
# efield.pyプログラムの終わり