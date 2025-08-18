import serial
import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found port: {port.device} - {port.description}")

# Check if the intended port exists
if "COM5" not in [port.device for port in ports]:
    print("Error: COM5 not found. Check the connection.")

class SerialCommunication:
    # Initialize parameters
    def __init__(self, serial_port="COM5", baudrate=115200):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.serial_connection = None  # Initialize to None
        self.is_serial_connected = False  # Track connection status

    def open_serial_connection(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.baudrate, timeout=1)
            time.sleep(2)  # Allow ESP32 time to reset
            self.is_serial_connected = True
            print(f"Serial connection established at {self.serial_port}")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.is_serial_connected = False
        return self.serial_connection

    def close_connection(self):
        # Close the serial connection
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None  # Reset connection
            self.is_serial_connected = False  # Mark connection as closed
            print("Serial connection closed.")
