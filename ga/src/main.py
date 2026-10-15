from config_manager import ConfigManager
import os
from datetime import datetime
from genetic.cities import generate_cities, calculate_distances
from genetic.population import generate_permutations
from genetic.fitness import find_best_path
from genetic.genetic_algorithm import genetic_algorithm
from visualizer import plot_cities, plot_statistics
from logger import Logger

def main():
    start_time = datetime.now()

    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini'))
    config = ConfigManager()
    config.load_config(config_path)

    logging_enabled = config.get('logging_enabled')
    count_of_cities = config.get('count_of_cities')
    size_of_map = config.get('size_of_map')
    count_of_generation = config.get('count_of_generation')
    best_p_mode = config.get('best_p_mode')
    child_generation_rate = config.get('child_generation_rate')

    # Initialize logger
    logger = Logger(logging_enabled)

    # Generate cities
    cities = generate_cities(count_of_cities, size_of_map)
    logger.log('Generation of cities:')
    logger.log(f'Sites: {str(cities)}\nCount of sites: {str(count_of_cities)}\n')

    distances = calculate_distances(len(cities), len(cities), cities) # rows = len(cities), cols = len(cities)
    count_of_best = 5
    permutation = generate_permutations(count_of_cities * 5, count_of_cities) # size_of_permutations
    mutation_rate = 2

    result = genetic_algorithm(
        mutation_rate, count_of_best, permutation,
        best_p_mode, child_generation_rate,
        count_of_generation, count_of_cities, distances,
    )

    best_permutation_output, number_of_best_individuals, number_of_children, best_fitness, average_fitness, \
    mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4 = result

    best_path, min_number = find_best_path(best_permutation_output, distances)
    print(min_number, best_path)

    end_time = datetime.now()
    logger.log(f'Best permutations and distances: {min_number}\nPath: {best_path}\n')
    logger.log(f'Execution time: {end_time - start_time}\n')
    logger.close()

    plot_cities(cities, best_path)
    plot_statistics(best_fitness, average_fitness,
                    number_of_best_individuals, number_of_children,
                    mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4)

if __name__ == "__main__":
    main()