import numpy as np
import multiprocessing as mp
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

# Optimized parallel fitness evaluation
def parallel_fitness(population, distance_matrix):
    with ProcessPoolExecutor(max_workers=mp.cpu_count() // 2) as executor:
        scores = list(executor.map(calculate_fitness, population, [distance_matrix] * len(population)))
    return np.array(scores)

# Tournament selection worker
def tournament_selection_worker(args):
    population, scores, tournament_size = args
    idx = np.random.choice(len(population), tournament_size, replace=False)
    best_idx = idx[np.argmin(scores[idx])]
    return population[best_idx]

# FIXED: No lambda, using a helper function
def select_in_tournament(population, scores, num_tournaments=4, tournament_size=3):
    args = [(population, scores, tournament_size) for _ in range(num_tournaments)]
    with ProcessPoolExecutor(max_workers=mp.cpu_count() // 2) as executor:
        selected = list(executor.map(tournament_selection_worker, args))
    return selected

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
