import numpy as np
import time


def read_distance_matrix_from_file(file_path):
    distance_matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [float(element) for element in row]
            distance_matrix.append(row)
    return np.array(distance_matrix)


def assign_clusters(distance_matrix, medoids):
    cluster_indices = np.argmin(distance_matrix[:, medoids], axis=1)
    clusters = [[] for _ in medoids]
    for i, cluster_index in enumerate(cluster_indices):
        clusters[cluster_index].append(i)
    return clusters


def calculate_cost(distance_matrix, clusters, medoids):
    medoid_indices = np.concatenate(
        [np.full(len(cluster), medoids[i]) for i, cluster in enumerate(clusters)])
    # print("dsfsdf", medoid_indices)
    total_cost = np.sum(distance_matrix[np.arange(
        len(distance_matrix)), medoid_indices])
    # print(distance_matrix[np.arange(
    #    len(distance_matrix)), medoid_indices])
    return total_cost


def calculate_silhouette(distance_matrix, clusters):
    n = len(distance_matrix)
    silhouette = 0
    for cluster in clusters:
        for vector in cluster:
            ai = np.mean(distance_matrix[vector, cluster])
            # print(distance_matrix[vector, cluster])
            bi = float('inf')
            for other_cluster in clusters:
                if other_cluster != cluster:
                    bi = min(bi, np.mean(
                        distance_matrix[vector, other_cluster]))
            # print(bi, " ", ai)
            s = (bi - ai) / max(ai, bi)
            silhouette += s
    score = silhouette / n
    return score


def greedy_medoid_selection(distance_matrix, n, k):
    random_index = np.random.randint(n)
    medoids = [random_index]

    while len(medoids) < k:
        remaining_indices = np.array(list(set(range(n)) - set(medoids)))
        remaining_distances = distance_matrix[remaining_indices][:, medoids]

        min_distances = np.min(remaining_distances, axis=1)
        next_medoid = np.argmin(min_distances)
        medoids.append(remaining_indices[next_medoid])

    return medoids


def pam(distance_matrix, k):
    n = len(distance_matrix)

    medoids = greedy_medoid_selection(distance_matrix, n, k)
    clusters = assign_clusters(distance_matrix, medoids)
    total_cost = calculate_cost(distance_matrix, clusters, medoids)

    updated = True
    while updated:
        updated = False
        for i in range(len(medoids)):
            non_medoids = [point for point in range(n) if point not in medoids]
            for non_medoid in non_medoids:
                new_medoids = medoids.copy()
                new_medoids[i] = non_medoid
                new_total_cost = calculate_cost(
                    distance_matrix, clusters, new_medoids)
                if new_total_cost < total_cost:
                    medoids = new_medoids
                    total_cost = new_total_cost
                    updated = True

            if not updated:
                break
        clusters = assign_clusters(distance_matrix, medoids)

    # print(clusters)
    silhouette = calculate_silhouette(distance_matrix, clusters)
    return clusters, medoids, silhouette


file_path = 'matrix.csv'
distance_matrix = read_distance_matrix_from_file(file_path)
k_values = range(2, 6)
max_avg_silhouette = -2
start_time = time.time()
for k in k_values:
    clusters, medoids, silhouette = pam(distance_matrix, k)
    print(f"K is {k}, and silhouette is {silhouette}")
    if silhouette > max_avg_silhouette:
        max_avg_silhouette = silhouette
        best_k = k
        best_clusters = clusters
        best_medoids = medoids

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")
print(f"Best k is: {best_k}")
print(f"Silhouette is: {max_avg_silhouette}")
for i in range(best_k):
    print(f"Cluster {i} has {len(best_clusters[i])} vectors")
