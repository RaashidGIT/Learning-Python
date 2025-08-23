# pip install numpy

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("Array a (1D array):")
print(a)

b = np.zeros((2, 3))
print("\nArray b (2x3 array of zeros):")
print(b)

c = np.ones((2, 2))
print("\nArray c (2x2 array of ones):")
print(c)

d = np.arange(0, 10, 2)
print("\nArray d (arange from 0 to 10, step 2):")
print(d)

e = np.arange(6)
print("\nArray e (arange from 0 to 5):")
print(e)

f = e.reshape((2, 3))
print("\nArray f (reshaped e to 2x3):")
print(f)

arr = np.array([1, 2, 3, 4])
print("\nMean of arr:", np.mean(arr))
print("Median of arr:", np.median(arr))
print("Standard Deviation of arr:", np.std(arr))

g = np.random.rand()
print("\nRandom float g (between 0 and 1):")
print(g)

h = np.random.rand(5)
print("\nArray h (1D array of 5 random floats):")
print(h)

i = np.random.rand(2, 3)
print("\nArray i (2x3 array of random floats):")
print(i)

j = np.random.randint(1, 10)
print("\nRandom integer j (between 1 and 9):")
print(j)

k = np.random.randint(0, 100, size=5)
print("\nArray k (1D array of 5 random integers from 0 to 99):")
print(k)

l = np.random.randint(10, 21, size=(3, 3))
print("\nArray l (3x3 array of random integers from 10 to 20):")
print(l)
