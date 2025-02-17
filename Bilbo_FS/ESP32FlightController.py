import requests
import serial
import serial.tools.list_ports
import time
import socketio
import json

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found port: {port.device} - {port.description}")

# Check if the intended port exists
if "COM5" not in [port.device for port in ports]:
    print("Error: COM5 not found. Check the connection.")

class ESP32FlightController:
    
    # Initialize parameters
    def __init__(self, serial_port="COM5", baudrate=115200):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.serial_connection = None  # Initialize to None
        self.is_serial_connected = False  # Track connection status
        self.sensor_data = {
            "pressure": "--",
            "altitude": "--",
            "acceleration": {"x": "--", "y": "--", "z": "--"},
            "gyroscope": {"x": "--", "y": "--", "z": "--"}
        }
    def open_serial_connection(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.baudrate, timeout=1)
            time.sleep(2)  # Allow ESP32 time to reset
            self.is_serial_connected = True
            print(f"Serial connection established at {self.serial_port}")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.is_serial_connected = False
    
    def read_esp32_data(self):
        # Read data coming from the ESP32
        if self.is_serial_connected:
            try:
                line = self.serial_connection.readline().decode("utf-8").strip()
                if line:
                    print(f"Received: {line}")  # Debugging
                    parsed_data = json.loads(line)  # Parse JSON from ESP32
                    
                    # Update individual values safely
                    self.sensor_data["pressure"] = parsed_data.get("pressure", self.sensor_data["pressure"])
                    self.sensor_data["altitude"] = parsed_data.get("altitude", self.sensor_data["altitude"])
                    self.sensor_data["acceleration"]["x"] = parsed_data.get("acceleration", {}).get("x", self.sensor_data["acceleration"]["x"])
                    self.sensor_data["acceleration"]["y"] = parsed_data.get("acceleration", {}).get("y", self.sensor_data["acceleration"]["y"])
                    self.sensor_data["acceleration"]["z"] = parsed_data.get("acceleration", {}).get("z", self.sensor_data["acceleration"]["z"])
                    self.sensor_data["gyroscope"]["x"] = parsed_data.get("gyroscope", {}).get("x", self.sensor_data["gyroscope"]["x"])
                    self.sensor_data["gyroscope"]["y"] = parsed_data.get("gyroscope", {}).get("y", self.sensor_data["gyroscope"]["y"])
                    self.sensor_data["gyroscope"]["z"] = parsed_data.get("gyroscope", {}).get("z", self.sensor_data["gyroscope"]["z"])
                
            except Exception as e:
                print("Exception detected:", e)


    def close_connection(self):
        # Close the serial connection
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = None  # Reset connection
            self.is_serial_connected = False  # Mark connection as closed
            print("Serial connection closed.")
        