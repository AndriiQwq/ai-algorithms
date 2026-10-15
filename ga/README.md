# TSP Genetic Algorithm

Solving the travelling salesman problem (TSP) using a genetic algorithm.

- Cities are generated randomly on the map.
- A population of random permutations of cities is used to find the shortest route.
- In each generation, crossover and mutation operations are applied to create new routes.
- The best routes are selected based on path length and the rest are replaced by new ones.
- The algorithm is repeated for several generations until the optimal path is found.

Matplotlib is used for visualisation.
Parameters are set in config.ini.

# Usage Examples: 

Configuration: 
```md
- Number of seats: 20 
- Map size: [200, 200] 
- Number of generations: 400 
- Number of nested generations: 250 
- Size of permutations from mutated individuals: 10 
- T = 1600  
- Factor = 0.99
```
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/0d676484-2d62-4579-9c98-3fabc7223a1d" />

Another example: 

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/350c7ea2-e2d3-4b55-9591-e49b5bcdb09c" />
