# -*- coding: utf-8 -*-
"""
ex1_2.pyプログラム
章末問題(2)プログラム
"""
# モジュールのインポート
import math

# メイン実行部
# 2次方程式の解の公式
def QuadForm(a, b, c):
    ans1 = (-b - math.sqrt(b**2 - 4 * a* c))/(2 * a)
    ans2 = (-b + math.sqrt(b**2 - 4 * a* c))/(2 * a)
    return ans1, ans2

# 有理化した2次方程式の解の公式
def rationalizedQuadForm(a, b, c):
    ans1 = (-b - math.sqrt(b**2 - 4 * a* c))/(2 * a)
    ans2 = -2 * c / (b + math.sqrt(b**2 - 4 * a* c))
    return ans1, ans2

# 入力
a = float(input('a*x*x + b*x + c = 0の係数a: '))
b = float(input('a*x*x + b*x + c = 0の係数b (> 0): '))
c = float(input('a*x*x + b*x + c = 0の係数c: '))

# 結果出力
D = b**2 - 4*a*c
if D < 0:
    print('実数解は存在しない')
else:
    ans1, ans2 = QuadForm(a, b, c)
    ans3, ans4 = rationalizedQuadForm(a, b, c)
    print('通常の解の公式の場合　　: ', ans1, ans2)
    print('有理化した解の公式の場合: ', ans3, ans4)
# ex1_2.py.pyの終わり