# PAM (Partitioning Around Medoids) Algorithm RACKET

This project implements the Partitioning Around Medoids (PAM) algorithm in Racket. PAM is a clustering algorithm that aims to divide a dataset into a specified number of clusters by selecting representative data points called medoids. It then assigns each data point to the nearest medoid based on a distance metric.

## Table of Contents

- [Auxiliary Functions](#auxiliary-functions)
- [Main PAM Algorithm Functions](#main-pam-algorithm-functions)
- [Tests](#tests)

---

## Auxiliary Functions

### `sum-list`

This function calculates the sum of all the elements in a given list.

### `mean-list`

Calculates the mean (average) of a given list of numbers.

### `minimum` and `mymin`

`minimum` finds the minimum value in a given list. `mymin` is a wrapper that handles empty lists.

### `min-index`

Finds the index of the minimum value in a given list.

### `index-of`

Searches for a given value in a list and returns the index of the first occurrence.

### `argmin-rows`

Takes a matrix (list of lists) as input and returns a list of indices, where each index corresponds to the minimum value in each row of the matrix.

### `zip`

Takes two lists, `l1` and `l2`, and combines corresponding elements from both lists into pairs.

### `matrix-change-row`

Returns a matrix with the `new_value` in the given row.

### `row_value`

Takes a matrix (list of lists) and a list of indices as input. Retrieves the values from the matrix corresponding to the given indices and returns them as a list.

### `while`

Defines a recursive `while` loop construct.

### `min-rows`

Returns a list with the minimums of every row in a matrix.

### `list-subtract`

Subtracts one list from another, removing elements from the first list that appear in the second list.

### `matrix-select-columns`

Selects and returns specified columns from a matrix.

### `filter-indices`

Filters elements from a list based on given indices.

### `matrix-select-rows` and `matrix-select-rows-cols`

Selects and returns specified rows from a matrix, and combinations of rows and columns from a matrix.

### `indices-filter` and `indices-filter-aux`

Filter elements in a list based on given indices.

### `reduce`

A reduce function for applying a binary function cumulatively to the items in a list.

### `sum-matrix`

Calculates the sum of all elements in a matrix.

### `string-filter` and `remove-spaces`

Functions for filtering characters in a string based on a predicate and removing spaces from a string, respectively.

---

## Main PAM Algorithms Functions

### `read-float-matrix-from-file` and `read_distance_matrix_from_file`

Read a CSV matrix from a file and return it as a list of lists, converting elements to floating-point numbers.

### `print-float-matrix`

Prints a floating-point matrix to the standard output.

### `assign_clusters`

Assigns data points to clusters based on the distance matrix and medoids.

### `calculate_cost`

Calculates the total cost of clustering based on the distance matrix, clusters, and medoids.

### `calculate_silhouette`

Calculates the silhouette score for the clustering.

### `greedy_medoid_selection`

Selects initial medoids using a greedy approach.

### `pam`

The main PAM algorithm that iteratively optimizes medoid selection and cluster assignment.

### `main`

Tries different values of `k` and reports the best `k` with the highest silhouette score.

### `elapsed-time`

Measures the elapsed time for running a function and reports statistics.

---

## Tests

The section contains various tests of the implemented functions and showcases the performance of the PAM algorithm on different datasets.

---

**Note:** Ensure you have the necessary input files (e.g., "iris_dist_matrix.csv" and "penguins_dist_matrix.csv") for running the tests.

---

