# -*- coding: utf-8 -*-
"""
loss_of_significance.pyプログラム
計算誤差の例題プログラム
桁落ち誤差の例題
"""
# モジュールのインポート
import math

# メイン実行部
# x = 1e15の場合
print('x = 1e15の場合')
x = 1e15
res1 = math.sqrt(x + 1) - math.sqrt(x)          # 通常の計算方法
res2 = 1 / (math.sqrt(x + 1) + math.sqrt(x))    # 分子を有理化した計算方法
# 結果出力
print('通常の計算方法　　　　　: ', res1)
print('分子を有理化した計算方法: ', res2)
print()

# x = 1e16の場合
print('x = 1e16の場合')
x = 1e16
res1 = math.sqrt(x + 1) - math.sqrt(x)          # 通常の計算方法
res2 = 1 / (math.sqrt(x + 1) + math.sqrt(x))    # 分子を有理化した計算方法
# 結果出力
print('通常の計算方法　　　　　: ', res1)
print('分子を有理化した計算方法: ', res2)
# loss_of_significance.pyの終わり