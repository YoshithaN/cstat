import numpy as np
n = int(input("Enter the number of terms: "))
phi = (1 + np.sqrt(5)) / 2
psi = (1 - np.sqrt(5)) / 2
fib = np.round((phi ** np.arange(n) - psi ** np.arange(n)) / np.sqrt(5))

print(fib.astype(int))

