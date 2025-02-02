import random
import string
import time
import multiprocessing

def generate_random_characters():
    return ''.join(random.choices(string.ascii_letters, k=1000))

def generate_random_numbers():
    return sum(random.choices(range(100), k=1000))

start_time = time.time()

char_process = multiprocessing.Process(target=generate_random_characters)
num_process = multiprocessing.Process(target=generate_random_numbers)

char_process.start()
num_process.start()

char_process.join()
num_process.join()

process_time = time.time() - start_time
print(f"Multiprocessing Execution Time: {process_time:.6f} seconds")
