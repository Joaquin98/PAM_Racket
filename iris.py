import pandas as pd
from scipy.spatial import distance_matrix

iris = pd.read_csv("iris_csv.csv")
print(iris)
df = iris.drop('class', axis=1)
matrix = pd.DataFrame(distance_matrix(df.values, df.values),
                      index=df.index, columns=df.index)

matrix.to_csv("iris_dist_matrix.csv", index=False, header=False)
