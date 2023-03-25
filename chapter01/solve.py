# -*- coding: utf-8 -*-
"""
solve.pyプログラム
sympyモジュールを利用して方程式を解く
"""
# モジュールのインポート
from sympy import *

# メイン実行部
var('x')
equation = Eq(x**3 + 2 * x**2 - 5 * x -6, 0)
answer = solve(equation)
print(answer)