import numpy as np
import matplotlib.pyplot as plt

n = 21
circle = np.zeros((n, n), dtype=int)
cx, cy = n // 2, n // 2
r = 8
for i in range(n):
    for j in range(n):
        if abs((i - cx)**2 + (j - cy)**2 - r**2) <= r:
            circle[i, j] = 1

plt.imshow(circle, cmap="gray_r")
plt.axis("off")
plt.show()