import numpy as np

mat = np.array([1, 2], [3, 4])
vec = np.array([1, 2])

# Shape
print(mat.shape) # (2, 2)
print(vec.shape) # (2,)

# Reshape
print(mat.reshape(4,)) # [1, 2, 3, 4]