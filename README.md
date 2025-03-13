# Parallel and Distributed Computing Assignment 🚀

## Assignment Part 1 Overview 🔍
This part evaluates various approaches for parallel computation by calculating the square of numbers using different techniques. The goal is to compare the performance of these methods on large datasets of 10^6 and 10^7 numbers.

## Test Methodology 🧪
I implemented the following methods to compute the square of numbers from a list of random integers:

- **Sequential Execution**: 🐢
  - A simple for loop that computes the square for each number sequentially.
- **Multiprocessing (Individual Processes for Each Number)**: 🔄
  - Spawns a new process for each number to compute its square.
- **Multiprocessing Pool (map)**: 🏊‍♂️
  - Uses a pool of worker processes to apply the square function in parallel to the list.
- **Multiprocessing Pool (apply)**: 📝
  - Similar to map(), but the function is applied to each number sequentially in a separate process.
- **Concurrent.futures ProcessPoolExecutor**: ⚙️
  - Uses the ProcessPoolExecutor from the concurrent.futures module to handle parallel execution.
- **Asynchronous Testing**: ⏱️
  - We tested both synchronous and asynchronous versions of the multiprocessing pool, particularly focusing on the difference between map() (synchronous) and map_async() (asynchronous).

## Test Results 📊

### For 10^6 Numbers:
- **Sequential Execution**: ⏱️
  - Execution time: 0.0543 seconds
  - Execution time was minimal, as expected with a single-threaded approach.
- **Multiprocessing (Individual Processes for Each Number)**: 🚶‍♂️🚶‍♀️
  - Execution time: 0.0883 seconds
  - Slightly faster than the sequential approach, but still incurs overhead due to process creation.
- **Multiprocessing Pool (map)**: 🏆
  - Execution time: 0.0832 seconds
  - Considered the optimal solution for parallelization, significantly faster than sequential execution and multiprocessing with individual processes.
- **Multiprocessing Pool (apply)**: 🐌
  - Execution time: 161.9429 seconds
  - Much slower compared to map(), as it spawns a separate process for each function call, leading to high overhead.
- **ProcessPoolExecutor**: 🐢
  - Execution time: 106.6540 seconds
  - Performed slower than map() and similar to apply(), as it also involves overhead in task management.

### For 10^7 Numbers:
- **Sequential Execution**: ⏳
  - Execution time: 0.5159 seconds
  - Execution time increased linearly with the number of numbers.
- **Multiprocessing (Individual Processes for Each Number)**: 🧵
  - Execution time: 0.7827 seconds
  - Slower compared to map() due to the overhead of spawning a large number of processes.
- **Multiprocessing Pool (map)**: 🚀
  - Execution time: 0.7932 seconds
  - The most efficient solution, handling large datasets well.
- **Multiprocessing Pool (map_async)**: 🚀💤
  - Execution time: 0.7806 seconds
  - No significant performance improvement over map(), but can be beneficial for more complex scenarios where other tasks can be performed while waiting for results.
- **Multiprocessing Pool (apply)**: 🐢💤
  - Execution time: 1676.2731 seconds
  - Extremely slow due to the large overhead in creating separate processes for each number.
- **ProcessPoolExecutor**: 🚶‍♂️
  - Execution time: 1046.5371 seconds
  - Slightly faster than apply() but still slower than map().

## Conclusions 🧠

### Best Method for Large Datasets: 🏆
Multiprocessing Pool (map) is the most efficient method for parallel processing, particularly for handling large datasets (e.g., 10^6 and 10^7 numbers).

### Worst Method for Large Datasets: 👎
Multiprocessing Pool (apply) is inefficient for large numbers due to its high overhead of creating processes for each task.

### Synchronous vs Asynchronous: ⚖️
Asynchronous map_async() did not show a significant performance improvement over synchronous map(), but it can be useful in more complex workflows involving I/O-bound tasks.

## Performance Insights 💡

### Overhead of Process Creation: ⚠️
Methods like individual processes and apply() are highly inefficient for large datasets because they create a separate process for each computation, leading to excessive overhead.

### Parallel Pooling (map and map_async): 🌊
map() offers an efficient way to parallelize tasks without introducing too much overhead. map_async() can be beneficial when tasks are I/O-bound or require non-blocking operations, but in this case, its impact was minimal.

_________________________________________________________________________

## Assignment Part 2 Overview 🔍
