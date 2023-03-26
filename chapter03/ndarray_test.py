import numpy as np

a = np.arange(20).reshape(4,5)

print(a)
print(a[1:-1,1:-1])
print(a[1:-1, 2:])
print(a[1:-1, 0:-2])
print(a[2:, 1:-1])
print(a[0:-2, 1:-1])