# tests.py
import random
from multiprocessing import Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor
from square import square

def generate_numbers(n):
    """Generates a list of n random numbers between 1 and 100."""
    return [random.randint(1, 100) for _ in range(n)]

def sequential_square(numbers):
    """Computes squares sequentially."""
    return [square(n) for n in numbers]

def pool_square_map_async(numbers):
    """Asynchronous multiprocessing using pool.map_async()"""
    with Pool(cpu_count()) as pool:
        result = pool.map_async(square, numbers)  # Runs in background
        return result.get()  # Waits for completion and collects results

def multiprocessing_square(numbers):
    """Computes squares using multiprocessing with a fixed number of workers."""
    num_workers = min(cpu_count(), len(numbers) // 10000)  # Use CPU count or limit workers
    with Pool(num_workers) as pool:
        return pool.map(square, numbers)  # Efficiently map numbers to available processes

def pool_square_map(numbers):
    """Uses multiprocessing pool with map()."""
    with Pool(cpu_count()) as pool:
        return pool.map(square, numbers)

def pool_square_apply(numbers):
    """Uses multiprocessing pool with apply()."""
    with Pool(cpu_count()) as pool:
        return [pool.apply(square, (n,)) for n in numbers]

def process_pool_executor(numbers):
    """Uses ProcessPoolExecutor to compute squares."""
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        return list(executor.map(square, numbers))
