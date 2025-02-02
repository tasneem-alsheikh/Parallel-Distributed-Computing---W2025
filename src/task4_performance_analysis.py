# Performance metrics calculation
def calculate_speedup(seq_time, parallel_time):
    return seq_time / parallel_time

def calculate_efficiency(speedup, num_threads):
    return speedup / num_threads

# Example times (replace with actual measured times)
sequential_time = 0.05  # Replace with actual value
threading_time = 0.03  # Replace with actual value
multiprocessing_time = 0.02  # Replace with actual value

# Compute metrics
speedup_threading = calculate_speedup(sequential_time, threading_time)
efficiency_threading = calculate_efficiency(speedup_threading, 2)

speedup_multiprocessing = calculate_speedup(sequential_time, multiprocessing_time)
efficiency_multiprocessing = calculate_efficiency(speedup_multiprocessing, 2)

print(f"Threading Speedup: {speedup_threading:.2f}, Efficiency: {efficiency_threading:.2f}")
print(f"Multiprocessing Speedup: {speedup_multiprocessing:.2f}, Efficiency: {efficiency_multiprocessing:.2f}")
