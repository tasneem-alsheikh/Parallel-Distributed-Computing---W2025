# src/task3_multiprocessing.py

import multiprocessing

def partial_sum_mp(start, end, queue):
    """Computes the sum of a given range and puts it in a multiprocessing queue."""
    queue.put(sum(range(start, end + 1)))

def multiprocessing_sum(n, num_processes=4):
    """Splits the summation into multiple processes and computes the total sum."""
    processes = []
    queue = multiprocessing.Queue()
    chunk_size = n // num_processes

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i != num_processes - 1 else n
        process = multiprocessing.Process(target=partial_sum_mp, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return sum(queue.get() for _ in range(num_processes))
