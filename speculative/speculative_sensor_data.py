import time
import random
import csv
import math
from datetime import datetime

def simulate_sensor_data():
    """Simulates reading data from your sensor. Replace this with your actual sensor reading code."""
    intensity = random.uniform(0, 1)  # Example: 0 to 1
    direction = random.uniform(0, 2 * math.pi) # Example: 0 to 360 degrees in radians
    vibration = random.uniform(0, 10)  # Example: frequency
    speed = random.uniform(0, 50)      # Example: units per second
    timestamp = datetime.now().isoformat()
    return timestamp, intensity, direction, vibration, speed

def save_to_csv(data, filename="sensor_data.csv"):
    """Saves the sensor data to a CSV file."""
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:  # Write header if the file is new
            writer.writerow(["Timestamp", "Intensity", "Direction", "Vibration", "Speed"])
        writer.writerow(data)
    print(f"Data saved to {filename}: {data}")

if __name__ == "__main__":
    try:
        print("Simulating sensor data recording (Ctrl+C to stop)...")
        while True:
            sensor_data = simulate_sensor_data()
            save_to_csv(sensor_data)
            time.sleep(1)  # Adjust the reading frequency as needed
    except KeyboardInterrupt:
        print("\nRecording stopped.")