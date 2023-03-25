# -*- coding: utf-8 -*-
"""
loss_of_trailing-digits.pyプログラム
計算誤差の例題プログラム
情報落ち誤差の例題
"""

# メイン実行部
# 初期設定
x = 1e10
y = 1e-8
temp = 0.0

# y (1e-8) を x (1e10) に10000000回加える
for i in range(10**7):
    x = x + y
# 結果出力
print(x)

# 先に y (1e-8) を10000000回加える
for i in range(10**7):
    temp += y
# 加えた結果を x (1e10) に加える
x = 1e10
x += temp
# 結果出力
print(x)
# loss_of_trailing-digits.pyの終わり