import random
import string
import time

def generate_random_characters():
    return ''.join(random.choices(string.ascii_letters, k=1000))

def generate_random_numbers():
    return sum(random.choices(range(100), k=1000))

# Timing execution
start_time = time.time()
generate_random_characters()
char_time = time.time() - start_time

start_time = time.time()
generate_random_numbers()
num_time = time.time() - start_time

print(f"Sequential Execution - Characters: {char_time:.6f} seconds")
print(f"Sequential Execution - Numbers: {num_time:.6f} seconds")


