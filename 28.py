import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

np.savetxt("array.csv", a, delimiter=",", fmt="%d")

print("NumPy array converted to CSV successfully.")
