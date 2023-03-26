# -*- coding: utf-8 -*-
"""
ri_rev1.pyプログラム
乱数による数値積分プログラム
擬似乱数を使って数値積分を行う
グラフを描画
"""

# モジュールのインポート
import random
import numpy as np
import matplotlib.pyplot as plt

# 定数
SEED = 1    # 乱数の種

# メイン実行部
# 試行回数nの入力
n = int(input("試行回数nを入力してください："))
# 乱数の初期化
random.seed(SEED)
xin_list = []
yin_list = []
xout_list = []
yout_list = []
integral = 0
# 積分値の計算
for i in range(n):
    x = random.random()
    y = random.random()
    if (x * x + y * y) <= 1:    # 円の内部 
        integral += 1
        xin_list.append(x)
        yin_list.append(y)
    else:
        xout_list.append(x)
        yout_list.append(y)

# 結果の出力
res = float(integral) / n
print("積分値I = {0}, 4I = {1}".format(res, 4*res))

x_list = np.linspace(0, 1, 100)
y_list = [ np.sqrt(1 - x**2) for x in x_list ]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, xlabel='$x$', ylabel='$y$', xlim=(0.0, 1.2), ylim=(0.0, 1.2))
ax.grid(visible=True, which='major', color='#666666', linestyle='--')
plt.scatter(xin_list, yin_list, c='red', s=5)
plt.scatter(xout_list, yout_list, c='blue', s=5)
plt.plot(x_list, y_list, lw=1, c='black')

result_text = "I = {0}, 4I = {1}".format(res, 4*res)
fig.text(0.6, 0.8, result_text)

savefile = "./png/ri_rev1.png"
plt.savefig(savefile, format="png", dpi=300)

plt.show()

# ri_rev1.pyの終わり
