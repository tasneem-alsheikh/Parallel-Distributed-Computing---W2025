# src/task4_performance_analysis.py

def performance_analysis(sequential_time, threading_time, multiprocessing_time):
    """Analyzes and prints speedup and efficiency of threading and multiprocessing."""
    
    num_threads = 4
    num_processes = 4

    speedup_threading = sequential_time / threading_time
    speedup_multiprocessing = sequential_time / multiprocessing_time

    efficiency_threading = speedup_threading / num_threads
    efficiency_multiprocessing = speedup_multiprocessing / num_processes

    print("\nPerformance Analysis:")
    print(f"Speedup (Threading): {speedup_threading:.2f}")
    print(f"Speedup (Multiprocessing): {speedup_multiprocessing:.2f}")
    print(f"Efficiency (Threading): {efficiency_threading:.2f}")
    print(f"Efficiency (Multiprocessing): {efficiency_multiprocessing:.2f}")
