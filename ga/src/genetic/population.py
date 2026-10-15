import random

def generate_permutations(n, count_of_cities):
    permutations = set()
    while len(permutations) <= n:
        permutation = tuple(random.sample(range(count_of_cities), count_of_cities))
        permutations.add(permutation)
    result = []
    for perm in permutations:
        result.append(list(perm))
    return result
