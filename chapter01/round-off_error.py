# -*- coding: utf-8 -*-
"""
round-off_error.pyプログラム
計算誤差の例題プログラム
丸め誤差の例題
"""

# メイン実行部
# 10進の0.1の値
print(0.1)

# 0.1を1000000回加える
x = 0.0
for i in range(10**6):
    x = x + 0.1     # 0.1は2進数では循環小数

# 結果出力
print(x)
# round-off_error.pyの終わり