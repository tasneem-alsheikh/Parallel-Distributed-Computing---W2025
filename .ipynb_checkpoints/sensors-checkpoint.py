import random
import time
import threading
from queue import Queue

# Global dictionaries to store the latest temperatures and temperature averages
latest_temperatures = {}
temperature_averages = {}

# Lock to protect shared data structures
temperature_lock = threading.RLock()

# Queue to safely transfer data between threads
temperature_queue = Queue()

def simulate_sensor(sensor_id):
    """Simulate a temperature reading and update latest_temperatures every second."""
    global latest_temperatures
    while True:
        # Simulate temperature between 15 and 40°C
        temperature = random.randint(15, 40)
        
        # Lock to safely update the global dictionary
        with temperature_lock:
            latest_temperatures[sensor_id] = temperature
            print(f"Sensor {sensor_id} updated to {temperature}°C")  # Debug output
        
        # Put the temperature reading into the queue for processing
        temperature_queue.put((sensor_id, temperature))
        
        time.sleep(1)  # Simulate a delay of 1 second between readings

def process_temperatures():
    """Calculate the average temperature from the readings in the queue."""
    global temperature_averages
    while True:
        if not temperature_queue.empty():
            sensor_id, temperature = temperature_queue.get()
            
            # Lock for safely updating the temperature averages
            with temperature_lock:
                if sensor_id not in temperature_averages:
                    temperature_averages[sensor_id] = []
                temperature_averages[sensor_id].append(temperature)
                
            # Wait for 5 seconds before calculating average to meet the bonus requirement
            time.sleep(5)
            
            # Calculate the average for the sensor
            average_temperature = sum(temperature_averages[sensor_id]) / len(temperature_averages[sensor_id])
            
            # Update the global dictionary with the calculated average
            with temperature_lock:
                temperature_averages[sensor_id] = average_temperature
                print(f"Sensor {sensor_id} average updated to {average_temperature:.2f}°C")  # Debug output
