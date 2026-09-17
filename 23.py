import numpy as np

a = np.array([1, 4, 9, 16, 25])

n = 2

result = np.diff(a, n)

print("Original array:", a)
print("2nd order difference:", result)
