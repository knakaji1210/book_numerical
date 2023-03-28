import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

step = np.pi / 10.0
xs = np.arange(0, np.pi * 2, step)
imgs = []

fig = plt.figure()

for i in range(len(xs)):
    lines = []
    for x in xs[0:i+1]:
        y = np.sin(x)
        img = plt.plot([x, x + step], [y, y], 'b-o')
        # lines.append(img) # これだとエラーになる
        lines.extend(img) 
    imgs.append(lines)

anim = animation.ArtistAnimation(fig, imgs, interval=100)
anim.save('./gif/anim_test2.gif', writer = 'pillow')

plt.show()