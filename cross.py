import numpy as np

A = np.array([7, 9, 13])
B = np.array([4, 2, 1])
inner = np.inner(A, B)
print("Inner product:", inner)
outer = np.outer(A, B)
print("Outer product:\n", outer)
cross = np.cross(A, B)
print("Cross product:", cross)
