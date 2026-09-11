import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])

A_inv = np.linalg.inv(A)

print("Matrix A:")
print(A)

print("\nInverse of A:")
print(A_inv)

