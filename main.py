# main.py

import time
from src.task1_sequential import sequential_sum
from src.task2_threading import threaded_sum
from src.task3_multiprocessing import multiprocessing_sum
from src.task4_performance_analysis import performance_analysis

if __name__ == "__main__":
    N = 10**7  # Large number for summation

    # Sequential Sum
    start_time = time.time()
    total_seq = sequential_sum(N)
    time_seq = time.time() - start_time
    print(f"Sequential Sum: {total_seq}, Time: {time_seq:.5f}s")

    # Threaded Sum
    start_time = time.time()
    total_thread = threaded_sum(N, num_threads=4)
    time_thread = time.time() - start_time
    print(f"Threaded Sum: {total_thread}, Time: {time_thread:.5f}s")

    # Multiprocessing Sum
    start_time = time.time()
    total_process = multiprocessing_sum(N, num_processes=4)
    time_process = time.time() - start_time
    print(f"Multiprocessing Sum: {total_process}, Time: {time_process:.5f}s")

    # Performance Analysis
    performance_analysis(time_seq, time_thread, time_process)
