import threading
import time
from sensors import simulate_sensor, process_temperatures
from display import update_display

# Number of sensors
num_sensors = 3

def start_threads():
    # Start the sensor simulation threads
    for sensor_id in range(num_sensors):
        threading.Thread(target=simulate_sensor, args=(sensor_id,), daemon=True).start()

    # Start the temperature processing thread
    threading.Thread(target=process_temperatures, daemon=True).start()

    # Start the display update thread
    threading.Thread(target=update_display, daemon=True).start()

if __name__ == "__main__":
    start_threads()
    
    # Keep the main thread alive to allow daemon threads to run
    try:
        while True:
            time.sleep(1)  # Add a small sleep to avoid maxing out CPU
    except KeyboardInterrupt:
        print("Program terminated by user.")
