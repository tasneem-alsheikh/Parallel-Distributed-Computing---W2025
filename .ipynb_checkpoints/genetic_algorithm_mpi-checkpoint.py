import numpy as np
import pandas as pd
import time
from mpi4py import MPI
from concurrent.futures import ProcessPoolExecutor

# Vectorized fitness function
def calculate_fitness(route, distance_matrix):
    if len(set(route)) != len(route):  # Check for duplicate nodes
        return -1e5  # Large penalty

    distances = distance_matrix[route[:-1], route[1:]]
    total_distance = np.sum(distances)

    last_leg = distance_matrix[route[-1], route[0]]
    if np.isinf(last_leg):
        return -1e5  # Large penalty
    return total_distance + last_leg

# Adaptive mutation rate function
def adaptive_mutation_rate(generation, num_generations, initial_rate=0.1):
    return initial_rate * (1 - generation / num_generations)

# Elitism function
def elitism(population, fitness_values, num_elites=1):
    elites_idx = np.argsort(fitness_values)[:num_elites]
    elites = [population[i] for i in elites_idx]
    return elites

# 2-opt local search
def two_opt(route, distance_matrix):
    best_route = route
    best_cost = calculate_fitness(route, distance_matrix)
    for i in range(1, len(route) - 2):
        for j in range(i + 1, len(route) - 1):
            new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
            new_cost = calculate_fitness(new_route, distance_matrix)
            if new_cost < best_cost:
                best_route = new_route
                best_cost = new_cost
    return best_route

# Parallel fitness evaluation using mpi4py
def parallel_fitness_mpi(population, distance_matrix):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    population_chunk = np.array_split(population, size)[rank]
    local_scores = np.array([calculate_fitness(route, distance_matrix) for route in population_chunk])
    all_scores = comm.gather(local_scores, root=0)
    if rank == 0:
        return np.concatenate(all_scores)

# Tournament selection worker
def tournament_selection_worker(args):
    population, scores, tournament_size = args
    idx = np.random.choice(len(population), tournament_size, replace=False)
    best_idx = idx[np.argmin(scores[idx])]
    return population[best_idx]

# Parallel tournament selection using mpi4py
def parallel_selection_mpi(population, scores, num_tournaments=4, tournament_size=3):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Randomly select individuals for the tournament
    tournament_indices = np.random.choice(len(population), (num_tournaments, tournament_size), replace=False)
    selected = []
    
    for idx in tournament_indices:
        best_idx = idx[np.argmin(scores[idx])]
        selected.append(population[best_idx])
    
    # Gather selected individuals from all processes
    all_selected = comm.gather(selected, root=0)
    if rank == 0:
        # Flatten the list of selected individuals
        return [indiv for sublist in all_selected for indiv in sublist]
    else:
        return []

# Optimized crossover
def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    
    offspring = np.full(size, -1)  # Faster than using a list with None
    offspring[start:end + 1] = parent1[start:end + 1]
    
    fill_values = [x for x in parent2 if x not in offspring[start:end + 1]]
    offspring[offspring == -1] = fill_values  # Replace -1s with remaining values
    return offspring.tolist()

# Optimized mutation
def mutate(route, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        i, j = np.random.choice(len(route), 2, replace=False)
        route[i], route[j] = route[j], route[i]
    return route

# Faster population generation
def generate_unique_population(population_size, num_nodes):
    return [np.insert(np.random.permutation(np.arange(1, num_nodes)), 0, 0).tolist() for _ in range(population_size)]

# Load the distance matrix
distance_matrix = pd.read_csv('data/city_distances_extended.csv').to_numpy()

# Parameters
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_tournaments = 4  # Number of tournaments to run
mutation_rate = 0.1
num_generations = 200
infeasible_penalty = 1e6  # Penalty for infeasible routes
stagnation_limit = 5  # Number of generations without improvement before regeneration

# Generate initial population: each individual is a route starting at node 0
np.random.seed(42)  # For reproducibility
population = generate_unique_population(population_size, num_nodes)

# Initialize variables for tracking stagnation
best_calculate_fitness = int(1e6)
stagnation_counter = 0

# Start the timer before the GA loop
start_time = time.time()

# Main GA loop
for generation in range(num_generations):
    # Evaluate fitness using parallel fitness evaluation
    calculate_fitness_values = parallel_fitness_mpi(population, distance_matrix)

    # Check for stagnation
    current_best_calculate_fitness = np.min(calculate_fitness_values)
    if current_best_calculate_fitness < best_calculate_fitness:
        best_calculate_fitness = current_best_calculate_fitness
        stagnation_counter = 0
    else:
        stagnation_counter += 1

    # Regenerate population if stagnation limit is reached, keeping the best individual
    if stagnation_counter >= stagnation_limit:
        print(f"Regenerating population at generation {generation} due to stagnation")
        best_individual = population[np.argmin(calculate_fitness_values)]
        population = generate_unique_population(population_size - 1, num_nodes)
        population.append(best_individual)
        stagnation_counter = 0
        continue  # Skip the rest of the loop for this generation

    # Selection, crossover, and mutation
    selected = parallel_selection_mpi(population, calculate_fitness_values)

    # Ensure that selected individuals are pairs (for crossover)
    offspring = []
    for i in range(0, len(selected) - 1, 2):  # Ensure we only pair up valid indices
        parent1, parent2 = selected[i], selected[i + 1]
        route1 = order_crossover(parent1[1:], parent2[1:])
        offspring.append([0] + route1)

    # If there's an odd number of selected individuals, just add the last one directly
    if len(selected) % 2 == 1:
        offspring.append([0] + selected[-1][1:])  # Fixed this line
    
    mutated_offspring = [mutate(route, adaptive_mutation_rate(generation, num_generations, mutation_rate)) for route in offspring]
    
    # Apply local search (2-opt)
    mutated_offspring = [two_opt(route, distance_matrix) for route in mutated_offspring]

    # Elitism: Keep the best solution
    elites = elitism(population, calculate_fitness_values)
    population = elites + mutated_offspring

    # Ensure population uniqueness
    unique_population = set(tuple(ind) for ind in population)
    while len(unique_population) < population_size:
        individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
        unique_population.add(tuple(individual))
    population = [list(individual) for individual in unique_population]

    # Print best fitness
    print(f"Generation {generation}: Best Fitness = {current_best_calculate_fitness}")

# Update fitness values for the final population
calculate_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])

# Output the best solution
best_idx = np.argmin(calculate_fitness_values)
best_solution = population[best_idx]
print("Best Solution:", best_solution)
print("Total Distance:", calculate_fitness(best_solution, distance_matrix))

# End the timer after the GA loop
end_time = time.time()

# Calculate and print the execution time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")
