# -*- coding: utf-8 -*-
"""
imshow_ani_test.pyプログラム
plt.imshowとArtistAnimationを組み合わせて
アニメーションを作る骨格となるシンプルなプログラム
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 100
imgs = []
world = np.zeros((n,n), dtype=int)

fig = plt.figure()
w = plt.imshow(world, interpolation="nearest")
imgs.append([w])

for i in range(10):
    world[i][i] = 1
    w = plt.imshow(world, interpolation="nearest")
    imgs.append([w])

ani = animation.ArtistAnimation(fig, imgs, interval=100)
ani.save('./gif/imshow_ani_test.gif', writer = 'pillow', fps = 1000)
plt.show()