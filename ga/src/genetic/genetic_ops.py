import random

def crossover(parent1, parent2, count_of_cities):
    index1 = random.randint(1, len(parent1) - 1)
    index2 = random.randint(1, len(parent2) - 1)

    parent1_part = parent1[:index1]
    parent2_part = parent2[index2:]
    result = parent1_part + parent2_part

    result_with_no_dabled_elements = []
    for element in result:
        if element not in result_with_no_dabled_elements:
            result_with_no_dabled_elements.append(element)

    for i in range(count_of_cities):
        if len(result_with_no_dabled_elements) >= count_of_cities:
            break
        if parent1[i] not in result_with_no_dabled_elements:
            result_with_no_dabled_elements.append(parent1[i])
        if len(result_with_no_dabled_elements) >= count_of_cities:
            break
        if parent2[i] not in result_with_no_dabled_elements:
            result_with_no_dabled_elements.append(parent2[i])
        if len(result_with_no_dabled_elements) >= count_of_cities:
            break

    return result_with_no_dabled_elements

def mutation(
    site, mutation_rate,
    m1, m2, m3, m4, counter,
    mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4
):
    if random.random() < 0.015 * mutation_rate:  # swap random sites
        index_1 = random.randint(0, len(site) - 1)
        index_2 = random.randint(0, len(site) - 1)
        temp = site[index_1]
        site[index_1] = site[index_2]
        site[index_2] = temp

        # For analytics
        m1 += 1
        counter += 1
        mutation_counts.append(counter)
        mutation_1.append(m1)
        mutation_2.append(m2)
        mutation_3.append(m3)
        mutation_4.append(m4)

    if random.random() < 0.025 * mutation_rate:  # swap par
        index_1 = random.randint(0, len(site) - 1)
        direction = random.randint(0, 1)

        if direction == 0:
            if index_1 - 1 >= 0:
                index_2 = index_1 - 1
            else:
                index_2 = index_1 + 1
        else:
            if index_1 + 1 <= len(site) - 1:
                index_2 = index_1 + 1
            else:
                index_2 = index_1 - 1

        temp = site[index_1]
        site[index_1] = site[index_2]
        site[index_2] = temp

        # For analytics
        m2 += 1
        counter += 1
        mutation_counts.append(counter)
        mutation_1.append(m1)
        mutation_2.append(m2)
        mutation_3.append(m3)
        mutation_4.append(m4)

    if random.random() < 0.05 * mutation_rate:  # reverse path
        index_1 = random.randint(0, len(site) - 1)
        index_2 = random.randint(0, len(site) - 1)

        if index_1 > index_2:
            index_1, index_2 = index_2, index_1

        site[index_1:index_2 + 1] = reversed(site[index_1:index_2 + 1]) 
        # https://www.geeksforgeeks.org/python-reversed-function/

        # For analytics
        m3 += 1
        counter += 1
        mutation_counts.append(counter)
        mutation_1.append(m1)
        mutation_2.append(m2)
        mutation_3.append(m3)
        mutation_4.append(m4)

    if random.random() < 0.025 * mutation_rate:  # swap to path
        while True:
            index_1 = random.randint(0, len(site) - 1)
            index_2 = random.randint(0, len(site) - 1)
            if abs(index_1 - index_2) > 5:
                break

        direction = random.randint(0, 1)
        dist = site[index_1:index_2 + 1]

        if direction == 0:
            if index_1 - len(dist) >= 0:
                next_first_index = index_1 - len(dist)
                source = site[next_first_index:index_1]
                site[next_first_index:index_1] = dist
                site[index_1:index_2 + 1] = source
        else:
            if index_2 + len(dist) < len(site):
                next_last_index = index_2 + len(dist)
                source = site[index_2 + 1:next_last_index + 1]
                site[index_2 + 1:next_last_index + 1] = dist
                site[index_1:index_2 + 1] = source

        # For analytics
        counter += 1
        m4 += 1
        mutation_counts.append(counter)
        mutation_1.append(m1)
        mutation_2.append(m2)
        mutation_3.append(m3)
        mutation_4.append(m4)

    return site, m1, m2, m3, m4, counter, mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4

def generate_unique_children(parent1, parent2, own_permutation, count_of_cities):
    while True:
        child = crossover(parent1, parent2, count_of_cities)
        if child not in own_permutation:
            return child