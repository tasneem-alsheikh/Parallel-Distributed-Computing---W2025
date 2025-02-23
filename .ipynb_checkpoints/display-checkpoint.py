import time
import os
from sensors import latest_temperatures, temperature_averages

def initialize_display():
    """Print the initial display layout for temperatures."""
    print("Current temperatures:")
    print("Latest Temperatures:")
    for i in range(3):  # We have 3 sensors
        print(f"Sensor {i}: --°C")
    print("\nSensor Averages:")
    for i in range(3):
        print(f"Sensor {i} Average: --°C")

def update_display():
    """Update the display with the latest temperatures and averages."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("Current temperatures:")
        print("Latest Temperatures:")
        for sensor_id in range(3):  # We have 3 sensors
            latest_temp = latest_temperatures.get(sensor_id, '--')
            print(f"Sensor {sensor_id}: {latest_temp}°C")
        
        print("\nSensor Averages:")
        for sensor_id in range(3):
            average_temp = temperature_averages.get(sensor_id, '--')
            print(f"Sensor {sensor_id} Average: {average_temp}°C")
        
        time.sleep(5)  # Update display every 5 seconds
