import os
import serial

class Vehicle:

    # Initialize parameters
    def __init__(self, hostname):
        self.hostname = hostname

    ## VEHICLE DATA
    # Get operating system
    def get_os(self):
        os_name = os.name
        if os_name == "nt":
            os_name = "Windows"
        else:
            os_name = "Other"
        print("Operating system:", os_name)
        return os_name

    # Get current working directory
    def get_path_dir(self):
        current_dir = os.getcwd()
        print("Current directory:", current_dir)
        return current_dir

    # Get hostname
    def get_hostname(self):
        return self.hostname

    ## SERIAL CONNECTION
    # Confirm serial connection Open port at “9600,8,N,1”, no timeout:
    def check_USB_connection(self, port='/dev/ttyUSB0', baudrate=9600, timeout=None):
        try:
            ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            print(f"Connected to serial port: {ser.name}")
            return ser.name
        except serial.SerialException as e:
            print(f"Error: Could not open serial port {port}. {e}")
            return None
