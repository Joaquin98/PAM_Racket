import pandas as pd
from scipy.spatial import distance_matrix


penguins = pd.read_csv('penguins.csv')
penguins["bill_length_mm"] = penguins["bill_length_mm"].fillna(
    value=penguins["bill_length_mm"].mean())
penguins["bill_depth_mm"] = penguins["bill_depth_mm"].fillna(
    value=penguins["bill_depth_mm"].mean())
penguins["flipper_length_mm"] = penguins["flipper_length_mm"].fillna(
    value=penguins["flipper_length_mm"].mean())
penguins["body_mass_g"] = penguins["body_mass_g"].fillna(
    value=penguins["body_mass_g"].mean())
penguins["sex"] = penguins["sex"].fillna("FEMALE")

y = penguins["species"]
penguins_main = penguins.iloc[:, 1:]
X = pd.get_dummies(penguins_main, dtype=float)

print(X)
matrix = pd.DataFrame(distance_matrix(X.values, X.values),
                      index=X.index, columns=X.index)

matrix.to_csv("penguins_dist_matrix.csv", index=False, header=False)
