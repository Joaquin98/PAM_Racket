import pandas as pd
from scipy.spatial import distance_matrix

matrix = pd.read_csv("dis_matrix(10000x10000).txt")
n = 10000
matrix = matrix.iloc[0:n, 0:n]
print(matrix)


matrix.to_csv("matrix.csv", index=False, header=False)
