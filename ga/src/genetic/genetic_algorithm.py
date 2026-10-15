import random
from genetic.fitness import calculate_all_distance_fitness_function
from genetic.genetic_ops import mutation, generate_unique_children

def genetic_algorithm(
    mutation_rate, count_of_best, permutation,
    mode, child_generation_rate,
    count_of_generation, count_of_cities, distances,
):
    # For analytics
    mutation_1, mutation_2, mutation_3, mutation_4 = [], [], [], []
    mutation_counts = []
    m1 = m2 = m3 = m4 = 0
    counter = 0

    # For analytics
    best_fitness = []
    average_fitness = []
    number_of_best_individuals = []
    number_of_children = []

    while_cycle_index = 0
    children = []

    while True:
        # Adjust mutation rate based on cycle index
        if while_cycle_index <= 0.1 * len(permutation):
            mutation_rate = max(0, 5 - int(5 * (while_cycle_index / len(permutation))))
        elif while_cycle_index <= 0.2 * len(permutation):
            mutation_rate = max(0, 4 - int(4 * (while_cycle_index / len(permutation))))
        elif while_cycle_index <= 0.4 * len(permutation):
            mutation_rate = max(0, 3 - int(3 * (while_cycle_index / len(permutation))))
        elif while_cycle_index <= 0.7 * len(permutation):
            mutation_rate = max(0, 2 - int(2 * (while_cycle_index / len(permutation))))
        elif while_cycle_index <= 0.9 * len(permutation):
            mutation_rate = max(0, 1 - int(1 * (while_cycle_index / len(permutation))))

        while_cycle_index += 1

        # Calculate fitness for each permutation
        way_km = []
        for i in range(len(permutation)):
            way_km.append(calculate_all_distance_fitness_function(permutation[i], distances))

        temp = []
        temp_perm = permutation.copy()
        temp_way_km = way_km.copy()

        # Adjust count of best based on cycle index
        if while_cycle_index <= 0.9 * len(permutation):
            count_of_best = 23
        elif while_cycle_index <= 0.8 * len(permutation):
            count_of_best = 19
        elif while_cycle_index <= 0.7 * len(permutation):
            count_of_best = 17
        elif while_cycle_index <= 0.5 * len(permutation):
            count_of_best = 13
        elif while_cycle_index <= 0.4 * len(permutation):
            count_of_best = 9
        elif while_cycle_index <= 0.2 * len(permutation):
            count_of_best = 7
        elif while_cycle_index <= 0.1 * len(permutation):
            count_of_best = 5

        # mode:
        # 0 - Selection of N best (elitism): N best individuals are selected based on the value of the fitness function.
        # 1 - Tournament selection: the best individual is selected from random groups.
        # 2 - Hybrid: first, n best individuals (about 1/3 of the population) are selected by fitness,
        #     then the rest are selected stochastically, with the probability of selection depending on their ranking.
        #     This approach helps maintain diversity and is especially useful for smaller populations.
        if mode == 0:
            while len(temp) < count_of_best:
                min_element = temp_way_km[0]

                for num in temp_way_km:
                    if num < min_element:
                        min_element = num

                min_element_index = temp_way_km.index(min_element)
                if temp_perm[min_element_index] not in temp:
                    temp.append(temp_perm[min_element_index])

                temp_way_km.pop(min_element_index)
                temp_perm.pop(min_element_index)

            best_permutation_output = temp
        elif mode == 1:
            while len(temp) < count_of_best:
                individuals = random.sample(permutation, 5)

                fit = []
                for individual in individuals:
                    fit.append(calculate_all_distance_fitness_function(individual, distances))

                index_of_best = fit.index(min(fit))
                best_individual = individuals[index_of_best]

                if best_individual not in temp:
                    temp.append(best_individual)
            best_permutation_output = temp
        elif mode == 2:
            sorted_permutation = zip(permutation, way_km)
            sorted_permutation = sorted(sorted_permutation, key=lambda x: x[1])
            # First add the top n (about a third of the population) by fitness function value
            best_append = round(count_of_cities / 3)

            for i in range(best_append):
                temp.append(sorted_permutation[i][0])
            sorted_permutation = sorted_permutation[best_append:]

            # The remaining ones are selected stochastically: the probability of selection depends on the position in the sorted list (the worse, the higher the chance)
            sorted_permutation = list(reversed(sorted_permutation))

            total_sum = sum(range(1, len(sorted_permutation) + 1))
            probability = [(i + 1) / total_sum for i in range(len(sorted_permutation ))]
            while len(temp) < count_of_best:
                w_index = random.choices(range(len(sorted_permutation)), weights=probability, k=1)[0]
                if sorted_permutation[w_index][0] not in temp:
                    temp.append(sorted_permutation[w_index][0])
            best_permutation_output = temp

        # For analytics
        number_of_best_individuals.append(len(best_permutation_output))

        children = []
        # Selection of offspring is now realised through different combinations of best and random parents.
        # This approach gives diversity, but can create many similar offspring and duplication.
        # More "classic" options:
        # - Randomly select pairs of parents from best_permutation_output (or the whole population) for crossover.
        # - Use tournament or roulette selection to select parents.
        # - Limit the number of offspring from one pair.
        # - Check uniqueness of offspring before adding.

        # This approach more rapid, but need more iterations to find the best path:
        parents_pool = best_permutation_output
        while len(children) < child_generation_rate * len(best_permutation_output):
            parent1 = random.choice(parents_pool)
            parent2 = random.choice(parents_pool)
            if parent1 == parent2:
                continue
            child = generate_unique_children(parent1, parent2, parents_pool + children, count_of_cities)
            if child not in children:
                children.append(child)

        # For analytics
        number_of_children.append(len(children))

        # Mutate children
        for i in range(len(children)):
            result = mutation(children[i], mutation_rate,
                            m1, m2, m3, m4, counter,
                        mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4)
            children[i], m1, m2, m3, m4, counter, mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4 = result
        
        # For analytics
        best_fitness.append(calculate_all_distance_fitness_function(best_permutation_output[0], distances))
        average_fitness.append(sum(way_km) / len(way_km))

        # Combine best permutations and children and go to new generation
        permutation = best_permutation_output + children

        if while_cycle_index >= count_of_generation:  # afeter n generation out of loop
            return (best_permutation_output, number_of_best_individuals, number_of_children, 
                   best_fitness, average_fitness, mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4)