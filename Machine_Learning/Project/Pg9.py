# pip install numpy

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("Array a:")
print(a)

b = np.zeros((2, 3))
print("\nArray b (2x3 zeros):")
print(b)

c = np.ones((2, 2))
print("\nArray c (2x2 ones):")
print(c)

d = np.arange(0, 10, 2)
print("\nArray d (arange from 0 to 10, step 2):")
print(d)
