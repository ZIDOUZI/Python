import numpy as np

matrix = np.random.rand(5, 5)

M = matrix.max()
m = matrix.min()

for i in range(5):
    for j in range(5):
        matrix[i][j] = (matrix[i][j] - m) / (M - m)

print(matrix)