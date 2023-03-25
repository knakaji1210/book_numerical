# -*- coding: utf-8 -*-
"""
fracex.pyプログラム
fractionsモジュールの例題プログラム
"""

# モジュールのインポート
from fractions import Fraction

# メイン実行部
# 分数計算
print(Fraction(5, 10), Fraction(3, 15))                     # 5/10と3/15の約分
print(Fraction(1, 3) + Fraction(1, 7))                      # 1/3 + 1/7
print(Fraction(5, 3) * Fraction(6, 7) * Fraction(3, 2))    # 5/3 * 6/7 * 3/2
# fracex.py.pyの終わり