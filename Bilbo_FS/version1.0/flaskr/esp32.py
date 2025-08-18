import time
from data.serial_comm import SerialCommunication


serial_comm = SerialCommunication()
serial_open = serial_comm.open_serial_connection()


class ESP32FlightController:
    # Initialize parameters
    def __init__(self):
        pass

    def read_esp32_data(self):
        while True:
            if serial_open.in_waiting > 0: # Check if there is data in the buffer
                line = serial_open.readline().decode('utf-8').strip()
                print(f"Received: {line}")
            time.sleep(0.1) # Small delay to prevent busy-waiting