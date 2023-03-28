import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.arange(0, np.pi * 2, np.pi / 10.0)
y = np.sin(x)

fig = plt.figure()
imgs = []

for i in range(len(x)):
    img = plt.plot(x[:i+1], y[:i+1], 'b-o')
    imgs.append(img)

anim = animation.ArtistAnimation(fig, imgs, interval=100)
anim.save('./gif/anim_test1.gif', writer = 'pillow')
plt.show()