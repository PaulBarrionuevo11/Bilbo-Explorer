import serial

class ESP32FlightContoller:
    
    # Initialize parameters
    # Add specific serial port, baudrate and timeout if needed
    def __init__(self):
        return
    
    # COM5 will be used for Windows
    def getData(self): 
        serial=serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        while True:
            if self.serial.in_waiting > 0:
                line = self.serial.readline().decode('utf-8').rstrip()
                data = line.split(',')
                if len(data) == 10:  # Ensure we have all 10 pieces of data
                    imu_ax, imu_ay, imu_az, imu_gx, imu_gy, imu_gz, accel_x, accel_y, accel_z, ultrasonic = data     
                    # Process or print the data
                    print(f"IMU Accel: {imu_ax}, {imu_ay}, {imu_az}")
                    print(f"IMU Gyro: {imu_gx}, {imu_gy}, {imu_gz}")
                    print(f"Ultrasonic: {ultrasonic}")
                    return data
                elif len(data) != 10:
                    # Information is missing
                    return "Unable to acces information"
            elif self.serial.in_waiting <= 0:
                return 0
