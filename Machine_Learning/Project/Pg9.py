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

e = np.arange(6)
print("\nArray e:")
print(e)

f = e.reshape((2, 3))
print("\nReshaped e to 2x3:")
print(f)

arr = np.array([1, 2, 3, 4])
print("\nMean of arr:", np.mean(arr))
print("Median of arr:", np.median(arr))
print("Standard Deviation of arr:", np.std(arr))

g = np.random.rand()
print(g)

h = np.random.rand(5)
print(h)

i = np.random.rand(2, 3)
print(i)
