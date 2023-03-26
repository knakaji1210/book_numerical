# -*- coding: utf-8 -*-
"""
glander.pyプログラム
落下のシミュレーション（Euler version）
逆噴射をする着陸船のシミュレーション
matplotlibによるグラフ描画機能付き
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数
f = 1.5       # 逆噴射の加速度を決定する係数
g = 9.80665   # 重力加速度

# 下請け関数の定義
# retrofire()関数
def retrofire(t, tf):
    """逆噴射の制御を担当する関数"""
    if t >= tf:
        return -f*g # 逆噴射
    else:
        return 0.0  # 逆噴射なし
 # retrofire()関数の終わり

# メイン実行部
t = 0.0         # 時刻t
dt = 0.01  # 時刻の刻み幅

# 係数の入力
v = float(input('初速度v0を入力してください: '))
x0 = float(input('初期高度x0を入力してください: '))
tf = float(input('逆噴射開始時刻tfを入力してください: '))
x = x0  # 初期高度の設定
print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))        # 現在時刻と現在の位置
# グラフデータに現在位置を追加
tlist = [t]
xlist = [x]

# 落下の計算
while (x >= 0) and (x <= x0):    # 地面に達するか初期高度より高くなるまで計算
    t += dt             # 時刻の更新
    v += (g + retrofire(t, tf)) * dt    # 速度の計算
    x -= v * dt    # 位置の更新
    print('時刻：{0:.7f}, 高度：{1:.7f}, 速度：{2:.7f}'.format(t, x, v))    # 現在時刻と現在の位置
    # グラフデータに現在位置を追加
    tlist.append(t)
    xlist.append(x)

# グラフの描画
plt.plot(tlist, xlist)  # グラフをプロット

savefile = "./png/glander.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()
# lander.pyプログラムの終わり