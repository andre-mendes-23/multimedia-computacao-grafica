import numpy as np

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
mat3 = [[9, 10], [11, 12]]

arr_3d = np.array([mat1, mat2, mat3])
print(arr_3d.shape) # (3, 2, 2)

mat = np.array([[1, 2], [3, 4]])
print(mat[0, 0]) # 1
print(mat[1, 1]) # 4
print(mat[:, 0]) # [1, 3]