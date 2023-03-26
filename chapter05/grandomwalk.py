# -*- coding: utf-8 -*-
"""
grandomwalk.pyプログラム
ランダムウォークシミュレーション
擬似乱数を使って２次元平面を酔歩する
matplotlibによるグラフ描画機能付き
"""

# モジュールのインポート
import random
import numpy as np
import matplotlib.pyplot as plt

# メイン実行部
# 試行回数nの初期化
n = int(input("試行回数を入力してください："))
# 乱数の初期化
seed = int(input("乱数の種を入力してください："))
random.seed(seed)

# ランダムウォーク
x = 0.0
y = 0.0
# グラフ描画の準備
xlist = [x] # x座標
ylist = [y] # y座標
for i in range(n):
    x += (random.random() - 0.5) * 2
    y += (random.random() - 0.5) * 2
    print("({0:.7f}, {1:.7f})".format(x, y))    # 位置
    xlist.append(x)
    ylist.append(y)

# グラフの表示
plt.plot(xlist, ylist)

savefile = "./png/grandomwalk.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()
# randomwalk.pyの終わり