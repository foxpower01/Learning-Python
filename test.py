# import matplotlib as plt


# list = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
# ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙']
# ['□', '□', '□', '□', '□', '□', '□', '□']
# ['□', '□', '□', '□', '□', '□', '□', '□']
# ['□', '□', '□', '□', '□', '□', '□', '□']
# ['□', '□', '□', '□', '□', '□', '□', '□']
# ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟']
# ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']

# temp = [1, 2, 3, 4, 5]
# print(temp[2:4])

# for i in range(10):
#     print(i)

#     [[2,0], [3,0], [4,0], [5,0], [6,0], [4,0], [3,0], [2,0]],
#     [[1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0], [1,0]],
#     [[0,0], [0,0], [0,0], [0,0], [1,1], [0,0], [0,0], [0,0]], 
#     [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],
#     [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],
#     [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]],
#     [[1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1], [1,1]],
#     [[2,1], [3,1], [4,1], [5,1], [6,1], [4,1], [3,1], [2,1]]

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')


# make data
lbls = ["one", "two", "three", "four"]
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))


def pie_chart(labels, values):
  fig, axes = plt.subplots()
  axes.pie(values, labels=labels)

# plot
# fig, ax = plt.subplots()
# ax.pie(x, colors=colors, radius=3, center=(4, 4),
#        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

# axes.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
pie_chart(lbls, x)
plt.show()