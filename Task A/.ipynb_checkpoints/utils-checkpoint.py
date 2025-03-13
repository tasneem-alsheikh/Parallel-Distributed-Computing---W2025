# utils.py
import time

def time_function(func, *args):
    """Times the execution of a function."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    return result
