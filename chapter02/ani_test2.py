# Animation Test

import matplotlib.pyplot as plt
from matplotlib import animation


fig_title = "XXX"
plot_lim = 30

fig = plt.figure()
ax = fig.add_subplot(111, title=fig_title, xlabel='X', ylabel='Y',
        xlim=[-plot_lim, plot_lim], ylim=[-plot_lim , plot_lim])
ax.grid(axis='both', color="gray", lw=0.5)

# この部分がani_testで関数にしていたところ
# これはfigの下に持ってこないとNG
# そうすると格好悪いので、defして上に持って行っている。それがani_test
x, y = 0, 0
x_list = [0]
y_list = [0]
imgs = []

while x < 10:
    x += 0.5
    y += 1
    x_list.append(x)
    y_list.append(y)
    img = plt.plot(x_list, y_list, ".", color="cyan")
    imgs.append(img)   
    print(x_list)
# ここまで

ani = animation.ArtistAnimation(fig, imgs, interval=10)
ani.save('./gif/ani_test2.gif', writer = 'pillow', fps = 30)

plt.show()
plt.close()
