import numpy as np
import matplotlib.pyplot as plt
n = 10
triangle = np.zeros((n, 2 * n - 1), dtype=int)
for i in range(n):
    triangle[i, n - 1 - i] = 1      
    triangle[i, n - 1 + i] = 1     
triangle[-1, :] = 1

plt.imshow(triangle, cmap="gray_r")
plt.axis("off")
plt.show()