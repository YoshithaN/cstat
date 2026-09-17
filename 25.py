import numpy as np

x = np.array([10, 20, 30, 40, 50])
y = np.array([12, 24, 29, 41, 52])

correlation = np.corrcoef(x, y)[0, 1]

print("Pearson correlation coefficient:", correlation)
