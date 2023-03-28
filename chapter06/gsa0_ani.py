# -*- coding: utf-8 -*-
"""
gsa0_ani.pyプログラム
シンプルなエージェントシミュレーション
２次元平面で動作するエージェント
結果をグラフ描画する

アニメーションを保存するように変更（230328）
"""

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation    # gifアニメーションのために追加

# 定数
TIMELIMIT = 100 # シミュレーション打ち切り時刻

# クラス定義
# Agentクラス
class Agent:
    """エージェントを表現するクラスの定義"""
    def __init__(self, cat):    # コンストラクタ
        self.category = cat
        self.x = 0  # x座標の初期値
        self.y = 0  # y座標の初期値
        self.dx = 0  # x座標の増分の初期値
        self.dy = 1  # y座標の増分の初期値
    def calcnext(self): # 次時刻の状態の計算
        if self.category == 0:
            self.cat0()  # カテゴリ0の計算
        else:   # 合致するカテゴリがない
            print("ERROR カテゴリがありません\n")
    def cat0(self): # カテゴリ0の計算メソッド
        # 内部状態の更新
        self.dx = self.reverse(self.dx)
        self.dy = self.reverse(self.dy)
        # 内部状態によって次の座標を決定
        self.x += self.dx
        self.y += self.dy
    def reverse(self, i):    # cat0()関数の下請け関数
        if i == 0:
            return 1
        else:
            return 0
    def putstate(self): # 状態の出力
        print(self.x, self.y)
# agentクラスの定義の終わり

# 下請け関数の定義
# calcn()関数
def calcn(a):
    """次時刻の状態を計算"""
    for i in range(len(a)):
        a[i].calcnext()
        a[i].putstate()
        # グラフデータに現在位置を追加
        xlist.append(a[i].x)
        ylist.append(a[i].y)
# calcn()関数の終わり

# メイン実行部
# 初期化
a = [Agent(0)]  # カテゴリ0のエージェントを生成

# グラフデータの初期化
xlist = []
ylist = []

imgs = []             # gifアニメーションのために追加
fig = plt.figure()    # gifアニメーションのために追加

# エージェントシミュレーション
for t in range (TIMELIMIT):
    calcn(a)    # 次時刻の状態を計算
    # グラフの表示
#    plt.clf()   # グラフ領域のクリア・・・これがあるとgifアニメーションがダメになる
    plt.axis([0, 60, 0, 60])    # 描画領域の設定
    img = plt.plot(xlist, ylist, ".", c="b") # グラフをプロット
    imgs.append(img)    # gifアニメーションのために追加
#    plt.pause(0.01)    # これがあるとgifアニメーションがダメになる
    xlist.clear()
    ylist.clear()

ani = animation.ArtistAnimation(fig, imgs, interval=100)          # gifアニメーションのために追加
ani.save('./gif/gsa0_ani.gif', writer = 'pillow', fps = 1000)     # gifアニメーションのために追加

plt.show()
# gsa0_ani.pyの終わり