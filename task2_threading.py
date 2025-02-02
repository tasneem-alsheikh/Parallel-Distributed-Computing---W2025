import random
import string
import time
import threading

def generate_random_characters():
    return ''.join(random.choices(string.ascii_letters, k=1000))

def generate_random_numbers():
    return sum(random.choices(range(100), k=1000))

# Threading wrapper functions
def thread_generate_random_characters():
    generate_random_characters()

def thread_generate_random_numbers():
    generate_random_numbers()

start_time = time.time()

char_thread = threading.Thread(target=thread_generate_random_characters)
num_thread = threading.Thread(target=thread_generate_random_numbers)

char_thread.start()
num_thread.start()

char_thread.join()
num_thread.join()

thread_time = time.time() - start_time
print(f"Threading Execution Time: {thread_time:.6f} seconds")
