import os
import serial

class NanoVehicle:

    # Initialize parameters
    def __init__(self, hostname):
        self.hostname = hostname
        self.serial_connection = False

    ## VEHICLE DATA
    def get_os(self):
        os_name = os.name
        if os_name == "nt":
            os_name = "Windows"
        else:
            os_name = "Other"
        print("Operating system:", os_name)
        return os_name

    def get_path_dir(self):
        current_dir = os.getcwd()
        print("Current directory:", current_dir)
        return current_dir

    def get_hostname(self):
        return self.hostname

    def uart_connection(self, port='COM5', baudrate=115200, timeout=None):
        ## Serial connection establish
        try:
            ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
            print(f"Connected to serial port: {ser.name}")
            self.serial_connection = True
            return ser
        except serial.SerialException as e:
            print(f"Error: Could not open serial port {port}. {e}")
            self.serial_connection = False
    def check_UART_connection(self):
        ## Serial connection status
        self.uart_connection(port='COM5', baudrate=115200, timeout=None)
        return self.serial_connection
        
    def close_connection(self):
        # Close the serial connection
        if self.serial_connection:
            self.serial_connection.close()
            self.serial_connection = False  # Mark connection as closed
            print("Serial connection closed.")
