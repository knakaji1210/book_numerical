# -*- coding: utf-8 -*-
"""
randomex.pyプログラム
randomモジュールの使用例
"""

# モジュールのインポート
import random

# メイン実行部
# SEEDの入力
seed = float(input("SEEDを入力してください: "))
# 乱数の初期化
random.seed(seed)
# 乱数の出力
for i in range(20):
    print(random.random())
# randomex.pyの終わり