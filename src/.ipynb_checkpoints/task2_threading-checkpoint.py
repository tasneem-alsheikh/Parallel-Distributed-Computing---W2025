# src/task2_threading.py

import threading

def partial_sum(start, end, result, index):
    """Computes the sum of a given range and stores it in the result list."""
    result[index] = sum(range(start, end + 1))

def threaded_sum(n, num_threads=4):
    """Splits the summation into multiple threads and computes the total sum."""
    threads = []
    result = [0] * num_threads
    chunk_size = n // num_threads

    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        thread = threading.Thread(target=partial_sum, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result)
