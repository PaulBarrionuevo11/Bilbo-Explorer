import requests
import serial
import time
import socketio
import json

class ESP32FlightController:
    
    # Initialize parameters
    def __init__(self, serial_port="/dev/ttyUSB0", baudrate=115200):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.serial_connection = None  # Initialize to None
        self.is_serial_connected = False  # Track connection status
        self.sensor_data = {"pressure": "--", "altitude": "--", "acceleration": "--", "gyroscope": "--"}  # Moved inside __init__

    def open_serial_connection(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.baudrate, timeout=1)
            time.sleep(2)  # Allow ESP32 to initialize in 2 sec
            self.is_serial_connected = True  # Mark connection as successful
            print(f"Serial connection estabished at port: {self.serial_port}")
        except Exception as e:
            print(f"Error: Could not open serial port {self.serial_port}.")
            self.is_serial_connected = False  # No connection, but program still runs
    
    def close_connection(self):
        # Close the serial connection
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None  # Reset connection
            self.is_serial_connected = False  # Mark connection as closed
            print("Serial connection closed.")
        