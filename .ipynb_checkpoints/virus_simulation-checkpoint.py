from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define Parameters
population_size = 100  # Adjust as needed
spread_chance = 0.3
vaccination_rate = np.random.uniform(0.1, 0.5)

# Initialize Population
population = np.zeros(population_size, dtype=int)
if rank == 0:
    infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
    population[infected_indices] = 1

# Broadcast initial population
population = comm.bcast(population, root=0)

# Define virus spread function
def spread_virus(population):
    new_population = population.copy()
    for i in range(len(population)):
        if population[i] == 0 and np.random.rand() < spread_chance:
            new_population[i] = 1
    return new_population

# Simulate virus spread over time
for _ in range(10):
    population = spread_virus(population)
    if rank != 0:
        comm.send(population, dest=0)
    else:
        for i in range(1, size):
            received_data = comm.recv(source=i)
            population += received_data

# Calculate Infection Rate
total_infected = np.sum(population)
infection_rate = total_infected / population_size
print(f"Process {rank} Infection Rate: {infection_rate:.2%}")
