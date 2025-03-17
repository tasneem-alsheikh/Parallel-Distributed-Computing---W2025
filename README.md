# DSAI 3202 – Parallel and Distributed Computing
## Assignment 1 – Part 2/2: Navigating the City

This project focuses on developing a genetic algorithm to optimize delivery routes in a city using Python and MPI4PY. The goal is to minimize the total distance traveled by a fleet of delivery vehicles while ensuring each delivery node is visited exactly once.

### Objectives
- Develop Python programs that run genetic algorithms in a distributed fashion using MPI4PY.
- Optimize the routes for a fleet of delivery vehicles in a city.

### Tools and Concepts
- **Python**: Programming language.
- **MPI4PY**: Package for parallel computing.

### Deliverables
- Code implementing the genetic algorithm.
- A README file explaining the program and results.

### The Genetic Algorithm
Genetic algorithms (GAs) are inspired by natural selection and are used to solve optimization problems by evolving a population of candidate solutions over time. Key components include:
- **Representation**: Encoding solutions as individuals.
- **Fitness Function**: Evaluating solution quality.
- **Selection**: Choosing individuals for reproduction.
- **Crossover**: Combining genetic information.
- **Mutation**: Introducing random changes.
- **Termination Condition**: Stopping criterion.

### 5. Fleet Management Using Genetic Algorithms
- **Objective**: Minimize the total distance traveled by all vehicles while visiting each node exactly once.
- **City Layout**: Represented as a graph with 20 nodes. Distances are given in `city_distances.csv`.
- **Constraints**: Each vehicle starts and ends at the depot (node 0).

### Files
- `genetic_algorithms_functions.py`: Functions for the genetic algorithm.
- `genetic_algorithm_trial.py`: Script to run the genetic algorithm trial.
- `city_distances.csv`: Distance matrix between nodes.
- `city_distances_extended.csv`: Distance matrix between nodes.

### Q&A 5.d

**Q: Explain the program outlined in the script `genetic_algorithm_trial.py`.**

A: The script `genetic_algorithm_trial.py` implements a genetic algorithm to optimize the route for a single delivery vehicle in a city. It initializes a population of routes, evaluates their fitness, and iteratively improves the population through selection, crossover, and mutation. The goal is to minimize the total distance traveled while ensuring each node is visited exactly once. The algorithm runs for a fixed number of generations or until a satisfactory solution is found.

**Q: Run and time the execution of this script.**

A: The script was executed, and the best solution found had a total distance of 1224.0 units. The execution time was approximately 60.94 seconds. The algorithm regenerated the population multiple times due to stagnation, indicating that it struggled to find better solutions after a certain point.

- **Total Distance**: 1224.0 units
- **Execution Time**: 60.94 seconds


________________________________________________________________________________________________________________________________________________________________________________


### 6. Parallelize the code 

### Q&A 6

**Define the parts to be distributed and parallelized, explain your choices.**
- **Fitness Evaluation:** Each individual’s fitness is computed in parallel to speed up evaluation. This reduces bottlenecks in large populations.
- **Selection:** Tournament selection runs in parallel, allowing multiple selection rounds to occur simultaneously. This improves efficiency.
- **Crossover and Mutation:** Offspring generation (crossover & mutation) is handled in parallel, ensuring faster population evolution.

**Run your code and compute the performance metrics.**

A: 
- **Total Distance**: 1224.0 units
- **Execution Time**: 33.32946848869324 seconds
- **Performance Metrics**: Speedup: 60.94 / 33.32946848869324 = 1.8284, Efficiency: (60.94 / 33.32946848869324) / num_processors = 0.9142


________________________________________________________________________________________________________________________________________________________________________________


### 7. Enhance the algorithm 

### Q&A 7

**Proposed Improvements:**
**Adaptive Crossover Rate**: Adjust the crossover rate based on the generation number, favoring exploration early on and focusing more on exploitation later.
**Diversity Maintenance**: Introduce techniques like fitness sharing or crowding to preserve genetic diversity and avoid premature convergence.
**Parallelize 2-opt Search**: Parallelize the 2-opt local search by applying it across multiple machines to speed up refinement.
**Dynamic Stagnation Check**: Instead of a fixed stagnation limit, dynamically adjust it based on population diversity and fitness changes.
**Efficient Elite Retention**: Implement truncation selection to keep only the best individuals in the population, optimizing elite retention.

**Run your code and compute the performance metrics.**

A: 
**Total Distance**: 1131.0
**Execution Time**: 31.834239721298218 seconds
- **Performance Metrics**: Speedup: 1.91, Efficiency: 0.955

________________________________________________________________________________________________________________________________________________________________________________


### 8. Large scale problem 

### Q&A 8

**Run the program using the extended city map: city_distances_extended.csv**

A:
**Best Solution**: [0, 81, 99, 98, 63, 52, 75, 59, 69, 77, 1, 21, 83, 95, 50, 11, 72, 65, 20, 55, 96, 46, 60, 16, 97, 91, 33, 23, 25, 82, 9, 26, 88, 40, 5, 32, 43, 28, 79, 57, 18, 90, 74, 86, 89, 93, 2, 70, 42, 44, 58, 80, 45, 54, 36, 29, 14, 68, 92, 41, 31, 38, 49, 30, 37, 35, 6, 66, 78, 19, 13, 51, 7, 4, 53, 17, 73, 22, 12, 34, 10, 15, 84, 27, 39, 62, 48, 61, 8, 94, 67, 47, 85, 71, 56, 76, 24, 3, 87, 64]
**Total Distance**: 205131.0
**Execution Time**: 89.06501793861389 seconds


**How would you add more cars to the problem?**
A:
To add more cars (vehicles) to the problem, I would treat each car as a separate route within the population. This essentially turns the problem into a "multiple traveling salesman problem" (mTSP). I’d need to adjust the algorithm so that it optimizes the routes for multiple vehicles at once, ensuring each vehicle starts at the depot and covers a different subset of cities without overlapping. I would modify the fitness function to account for the multiple vehicles and distribute the cities among the cars accordingly.





