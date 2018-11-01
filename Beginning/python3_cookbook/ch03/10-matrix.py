# 3.10 矩阵与线性代数运算

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)

# Return transpose
print(m.T)

# Return inverse
print(m.I)

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
print(v)
print(m * v)

import numpy.linalg

# Determinant
numpy.linalg.det(m)

# Eigenvalues
numpy.linalg.eigvals(m)

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
