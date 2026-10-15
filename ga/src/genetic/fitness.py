def calculate_all_distance_fitness_function(path, distances_table):
    distance = 0
    for i in range(len(path) - 1):
        distance += distances_table[path[i]][path[i + 1]]
    distance += distances_table[path[0]][path[-1]]
    return distance

def find_best_path(permutations, distances):
    min_number = float('inf')
    best_path = None
    for p in permutations:
        dist = calculate_all_distance_fitness_function(p, distances)
        if dist < min_number:
            min_number = dist
            best_path = p
    return best_path, min_number
