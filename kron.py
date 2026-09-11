import numpy as np
A = np.array([[1, 4],
              [9, 2]])

B = np.array([[6, 12],
              [3, 8]])

K = np.kron(A, B)
print("Kronecker Product:")
print(K)

