import serial
import threading
import keyboard  # For detecting space bar
import time
from datetime import datetime

def read_serial(port, baud_rate):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {port} at {baud_rate} baud rate.")
        return ser
    except serial.SerialException as e:
        print(f"Failed to connect to {port}: {e}")
        return None

def record_data(serial_conn, recording_flag, file_name, movement_name):
    print("Recording started. Press Space Bar to stop.")
    with open(file_name, "w") as file:
        # file.write(f"Movement: {movement_name}\n")
        file.write("Timestamp,Analog1,Analog2\n")  # CSV header

        while recording_flag[0]:
            try:
                line = serial_conn.readline().decode('utf-8').strip()
                if line:
                    print(line)  # Print to console
                    file.write(f"{time.time()},{line}\n")  # Write to file
            except Exception as e:
                print(f"Error reading serial data: {e}")

    print("Recording stopped.")

def main():
    # port = input("Enter the COM port (e.g., COM3 or /dev/ttyUSB0): ")
    port = "COM3"
    baud_rate = 9600  # Match the baud rate with ESP32 configuration

    serial_conn = read_serial(port, baud_rate)
    if not serial_conn:
        return

    movement_name = input("Enter the name of the movement: ")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{movement_name}_{timestamp}.csv"

    recording_flag = [False]

    def toggle_recording():
        if recording_flag[0]:
            recording_flag[0] = False
        else:
            recording_flag[0] = True
            record_thread = threading.Thread(target=record_data, args=(serial_conn, recording_flag, file_name, movement_name))
            record_thread.start()

    print("Press Space Bar to start and stop recording.")
    try:
        while True:
            if keyboard.is_pressed("space"):
                toggle_recording()
                while keyboard.is_pressed("space"):
                    time.sleep(0.1)  # Avoid multiple toggles due to rapid keypress detection
    except KeyboardInterrupt:
        print("Program terminated.")

    if serial_conn.is_open:
        serial_conn.close()
        print("Serial connection closed.")

if __name__ == "__main__":
    main()
