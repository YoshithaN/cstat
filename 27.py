import numpy as np
import matplotlib.pyplot as plt

a = np.array([10, 20, 15, 30, 25, 40])

plt.plot(a, marker='o')
plt.title("Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()
plt.show()
