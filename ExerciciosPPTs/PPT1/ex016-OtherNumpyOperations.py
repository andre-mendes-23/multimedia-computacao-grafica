import numpy as np
from numpy import linalg

A = np.array([[1, 2], [3, 4]])

print(linalg.det(A)) # -2.0
print(linalg.inv(A)) 
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])