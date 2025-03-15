# Parallel and Distributed Computing Assignment 🚀

## Assignment Part 2 Overview 🔍
The assignment focuses on optimizing delivery routes using a genetic algorithm (GA) with MPI4PY or Celery for distributed computing. The task involves completing and implementing GA functions like fitness calculation and tournament selection to minimize the total distance in a single vehicle’s route across a city represented by a distance matrix. The assignment also requires parallelizing the GA to run on multiple machines, enhancing its performance, and testing it on a larger scale with more cars and nodes. Finally, performance metrics and improvements are compared before and after parallelization and enhancements.


### 5.d. Explain and Run the Algorithm (5 pts)

#### **Explanation of `genetic_algorithm_trial.py`**
The script `genetic_algorithm_trial.py` implements a **Genetic Algorithm (GA)** to optimize a fleet management routing problem. The algorithm aims to find the shortest possible route for a vehicle to visit multiple locations and return to the starting point. Below is a breakdown of its key components:

1. **Loading the Distance Matrix**
   - The script reads the `city_distances.csv` file into a NumPy array.
   - It preprocesses the distance matrix by replacing infeasible paths (`100000`) with `np.inf` to prevent invalid calculations.

2. **Population Initialization**
   - A population of unique random routes is generated using `generate_unique_population()`, ensuring all routes start from node `0`.
   
3. **Fitness Evaluation**
   - The `calculate_fitness()` function computes the total distance for each route.
   - If a route is infeasible (due to `np.inf` distances), it is assigned a large penalty (`-1e5`).

4. **Tournament Selection**
   - The `select_in_tournament()` function selects individuals for crossover by running small tournaments and picking the best routes.

5. **Crossover and Mutation**
   - `order_crossover()` generates new routes by combining parts of two parent routes.
   - `mutate()` introduces slight modifications by swapping two random locations in a route with a certain probability.

6. **Stagnation Handling**
   - If the best fitness score does not improve for 5 consecutive generations, the population is regenerated to avoid premature convergence.

7. **Main Loop Execution**
   - The GA runs for `200` generations, continuously evolving better solutions.
   - At the end, the script prints the best-found solution and its total travel distance.

---

#### **Running and Timing the Script**
To measure the execution time of `genetic_algorithm_trial.py`, the following Python script was used:

```python
import time

start_time = time.time()  # Start timer

# Run the genetic algorithm script
exec(open("genetic_algorithm_trial.py").read())  

end_time = time.time()  # End timer

print(f"Execution Time: {end_time - start_time:.2f} seconds")
```

**Execution Results:**
After running the script, the best solution (optimal route) and its total distance were displayed. Additionally, the execution time was measured and printed.

This confirms that the genetic algorithm successfully finds an optimized route while adapting through selection, crossover, and mutation.

