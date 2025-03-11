from mpi4py import MPI
import numpy as np
import time

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the function to compute squares
def compute_squares(start, end):
    return [x**2 for x in range(start, end)]

# Define the range
n = int(1e8)
chunk_size = n // size
start = rank * chunk_size
end = start + chunk_size if rank != size - 1 else n

# Start timing
start_time = time.time()

# Compute squares
local_squares = compute_squares(start, end)

# Gather results at rank 0
result = comm.gather(local_squares, root=0)

# Print results on rank 0
if rank == 0:
    final_squares = np.concatenate(result)
    print(f"Final array size: {len(final_squares)}")
    print(f"Last square: {final_squares[-1]}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
