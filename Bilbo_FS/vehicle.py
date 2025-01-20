import os
import serial

class Vehicle:

    # Initializing parameters
    def __init__(self, hostname, port='/dev/ttyUSB0', baudrate=9600):
        self.hostname = hostname
        self.port = port
        self.baudrate = baudrate
        self.connection = None


    ## VEHICLE DATA
    # Get operating system
    def get_os(self):
        os_name = os.name
        print("Operating system: ", os_name)

        if(os_name == "nt"):
            os_name = "Windows" 
        else:
            os_name = "Other"

        print("Operating system: ", os_name)
        return os_name
    
    # Get current working directory
    def get_path_dir(self):
        current_dir = os.getcwd()
        print("Current dir:", current_dir)
        return current_dir
    
    def get_hostname(self):
        self.hostname = "Mars 1" 
        return self.hostname
    
    ## SERIAL CONNECTION
    # Confirm serial connection
    def confirm_serial_connection(self):
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            if self.connection.is_open:
                print(f"Serial connection established on {self.port} at {self.baudrate} baud.")
                return True
        except serial.SerialException as e:
            print(f"Serial connection error: {e}")
        return False

    # Close serial connection
    def close_connection(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Serial connection closed.")