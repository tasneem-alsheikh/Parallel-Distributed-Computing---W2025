from tests import (
    generate_numbers, sequential_square, multiprocessing_square, 
    pool_square_map, pool_square_map_async, pool_square_apply, process_pool_executor
)
from utils import time_function

def run_tests(num_count):
    """Runs all square computation tests for a given number count."""
    print(f"\nRunning tests with {num_count} numbers...\n")
    numbers = generate_numbers(num_count)

    print("Sequential Execution:")
    time_function(sequential_square, numbers)

    print("\nMultiprocessing (Individual Processes for Each Number):")
    time_function(multiprocessing_square, numbers)

    print("\nMultiprocessing Pool (map):")
    time_function(pool_square_map, numbers)

    print("\nMultiprocessing Pool (map_async):")
    time_function(pool_square_map_async, numbers)  # Asynchronous test

    print("\nMultiprocessing Pool (apply):")
    time_function(pool_square_apply, numbers)

    print("\nProcessPoolExecutor:")
    time_function(process_pool_executor, numbers)

def main():
    run_tests(10**6)  # 1,000,000 numbers
    run_tests(10**7)  # 10,000,000 numbers

if __name__ == '__main__':
    main()
