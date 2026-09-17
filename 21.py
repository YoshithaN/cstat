import numpy as np

# Define the matrix
A = np.array([
    [1, 1],
    [1, 0],
    [0, 1]
])

# QR decomposition
Q, R = np.linalg.qr(A)

print("Matrix A:")
print(A)

print("\nMatrix Q:")
print(Q)

print("\nMatrix R:")
print(R)

# Verify A = QR
print("\nQ × R:")
print(np.dot(Q, R))
