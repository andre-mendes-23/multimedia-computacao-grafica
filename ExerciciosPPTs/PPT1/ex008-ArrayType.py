import numpy as np

print(np.array([1, 2, 3, 4], dtype=np.float32)) # array([ 1.,  2.,  3.,  4.], dtype=float32)

arr = np.array([1, 2, 3, 4])
print(arr.dtype) # dtype('int64')

arr.dtype = np.float32
print(arr) # [1.e-45 0.e+00 3.e-45 0.e+00 4.e-45 0.e+00 6.e-45 0.e+00]

arr = arr.astype(np.float32)
print(arr) # [1. 2. 3. 4.]