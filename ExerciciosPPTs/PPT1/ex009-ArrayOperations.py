import numpy as np

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([1, 0, -3, 1])

# addition
print(arr_a + arr_b) # array([2, 2, 0, 5])

# subtraction
print(arr_a - arr_b) # array([0, 2, 6, 3])

# multiplication
print(arr_a * arr_b) # array([ 1, 0, -9, 4])

# division
print(arr_b / arr_a) # array([ 1. , 0. , -1. , 0.25])

# exponent
print(arr_b ** arr_a) # array([1, 0, -27, 1])

arr = np.array([1, 2, 3, 4])
new = 2*arr
print(new) # [2, 4, 6, 8]