import numpy as np


a = np.array([1, 2])
b = np.array([3, 4, 5])

print(b[a])

c = b[1:]

print(b)

c[0] = 1

print(b)

print(c)

print(b[1:] is c)

d = b[1:]

print(d is c)

print(c[0].data.obj.data is d[0].data.obj.data)