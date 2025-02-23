# Temperature Monitoring System 🌡️

## Overview 📝

This is a Python program designed to simulate a temperature monitoring system. The program simulates temperature readings from multiple sensors, calculates average temperatures, and displays this information in real-time in the console. It utilizes multithreading for concurrent execution and thread synchronization for safe data access. ⚙️

## Features ✨

- 🌡️ Simulates temperature readings from 3 sensors.
- 🔢 Computes and updates the average temperature of each sensor.
- 📺 Displays the latest temperature and the average temperature every 5 seconds.
- 🧵 Uses **daemon threads** for sensor simulation and temperature processing.
- 🔒 Ensures thread synchronization using `RLock` and `Queue`.

## How to Run 🚀

1. Clone the repository to your local machine:
    ```bash
    git clone <repo-url>
    cd lab4
    ```

2. Run the program:
    ```bash
    python main.py
    ```

3. The program will continuously update the temperature readings and averages every 5 seconds. 🔄

## Synchronization Metrics Used 🔑

1. **RLock (Reentrant Lock)** 🔐:
   - Used to synchronize access to the global shared data structures: `latest_temperatures` and `temperature_averages`. The lock ensures that no two threads can modify these structures at the same time, preventing data corruption. 🔄

2. **Queue** 🗳️:
   - Used for safe communication between threads. The `Queue` is used to transfer temperature readings from the sensor simulation threads to the data processing thread in a thread-safe manner. 🏃‍♂️💨

3. **Daemon Threads** 🧵:
   - Threads were set as daemons (`daemon=True`) to allow them to run in the background without blocking the main program. This is especially useful for long-running processes like sensor simulation and display updates. 🌌

## Why Did the Professor Not Ask You to Compute Metrics? 🤔

The primary goal of this lab was to focus on understanding and implementing **multithreading**, **thread synchronization**, and **real-time updates in the console**. By utilizing synchronization mechanisms such as `RLock` and `Queue`, we can safely manage concurrent threads and their interactions. While computing metrics such as performance or statistical data could be useful, this lab's focus was more on demonstrating thread management and synchronization rather than performance analysis. 📊

---

## Bonus Task (5%) 🎉:

1. **Latest temperature updated every 1 second**: ✅ This was achieved by having the `simulate_sensor` function update the `latest_temperatures` dictionary every second. 🕐
2. **Average temperature updated every 5 seconds**: ✅ This was implemented by adding a `time.sleep(5)` inside the `process_temperatures` function to ensure the averages are updated every 5 seconds instead of every second. ⏳

---

## Files Structure 📂:

- **`main.py`**: Entry point of the program that starts the sensor simulation, data processing, and display update threads. 🚀
- **`sensors.py`**: Contains the functions for simulating sensor readings and processing the temperature data. 🌡️
- **`display.py`**: Handles the console display, updating the temperature readings and averages in real-time. 💻
- **`README.md`**: Documentation for the project, including instructions and answers to lab questions. 📄

## Dependencies 🛠️

This project only requires Python's built-in libraries, including:
- `random` 🎲
- `time` 🕰️
- `threading` 🧵
- `queue` 🗳️
