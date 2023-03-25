# -*- coding: utf-8 -*-
"""
solve.pyプログラム
sympyモジュールを利用して方程式を解く
"""
# モジュールのインポート
from sympy import Symbol, sympify, solve, pprint

# メイン実行部
x = Symbol('x')
f = x**3 + 2 * x**2 - 5 * x -6
f = sympify(f)
pprint(f)
answer = solve(f)
print(answer)