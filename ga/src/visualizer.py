import matplotlib.pyplot as plt

def plot_cities(sites, best_path):
    connections = []
    for i in range(len(best_path) - 1):
        connections.append([best_path[i], best_path[i + 1]])
    connections.append([best_path[-1], best_path[0]])

    if connections is None:
        connections = []
    plt.figure(figsize=(8, 8))
    plt.xlim(0, 200)
    plt.ylim(0, 200)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().add_patch(plt.Rectangle((0, 0), 200, 200, fill=None, edgecolor='black'))

    for i in range(len(sites)):
        if i == best_path:
            plt.plot(sites[i][0], sites[i][1], 'go', markersize=15)
        else:
            plt.plot(sites[i][0], sites[i][1], 'ro')
        plt.text(sites[i][0], sites[i][1], f'({sites[i][0]}, {sites[i][1]})', fontsize=9, ha='right')

    plt.title('Map')
    plt.grid()

    for i, connection in enumerate(connections):
        plt.plot(
            [sites[connection[0]][0], sites[connection[1]][0]],
            [sites[connection[0]][1], sites[connection[1]][1]],
            'b-'
        )

        mid_x = (sites[connection[0]][0] + sites[connection[1]][0]) / 2
        mid_y = (sites[connection[0]][1] + sites[connection[1]][1]) / 2
        plt.text(mid_x, mid_y, str(i + 1), fontsize=10, ha='center', va='bottom')

    plt.show()



def plot_statistics(
    best_fitness, average_fitness,
    number_of_best_individuals, number_of_children,
    mutation_counts, mutation_1, mutation_2, mutation_3, mutation_4
):
    generations = list(range(len(best_fitness)))

    # Graph of best and average adaptability
    plt.plot(generations, best_fitness, label='Best Fitness')
    plt.plot(generations, average_fitness, label='Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('The development of fitness through the process of evolution')
    plt.legend()
    plt.show()

    # Graph of the number of best individuals and offspring
    plt.plot(generations, number_of_best_individuals, label='Number Of Best Individuals')
    plt.plot(generations, number_of_children, label='Number Of Children')
    plt.xlabel('Generation')
    plt.ylabel('Numbers')
    plt.title('Investigation of the number of progeny and best individuals per evolution')
    plt.legend()
    plt.show()

    # Graph of mutations
    plt.plot(mutation_counts, mutation_1, label='Mutation 1 (swap random)', color='green')
    plt.plot(mutation_counts, mutation_2, label='Mutation 2 (swap par)', color='blue')
    plt.plot(mutation_counts, mutation_3, label='Mutation 3 (reverse path)', color='red')
    plt.plot(mutation_counts, mutation_4, label='Mutation 4 (swap to path)', color='orange')
    plt.xlabel('Mutation Counts')
    plt.ylabel('Mutation Count Types')
    plt.title('Mutation Counts Over Time')
    plt.legend()
    plt.show()