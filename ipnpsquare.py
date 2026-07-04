import numpy as np
import matplotlib.pyplot as plt

n = 10
square = np.zeros((n, n), dtype=int)

square[0, :] = 1
square[-1, :] = 1
square[:, 0] = 1
square[:, -1] = 1

plt.imshow(square, cmap="gray_r")
plt.axis("off")
plt.show()