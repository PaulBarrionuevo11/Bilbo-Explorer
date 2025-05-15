import re

class ESP32FlightController:
    def __init__(self):
        self.sensor_data = {
            "pressure": "--",
            "altitude": "--",
            "acceleration": {"x": "--", "y": "--", "z": "--"},
            "gyroscope": {"x": "--", "y": "--", "z": "--"}
        }
    
    def read_esp32_data(self, ser):
        try:
            raw_line = ser.readline()
            if raw_line:
                try:
                    line = raw_line.decode('utf-8').strip()
                    print(f"Raw line: {line}")
                except UnicodeDecodeError:
                    print(f"Invalid UTF-8 data skipped: {raw_line}")
                    return
                
                match = re.match(r"(.+?): ([-+]?\d*\.\d+|\d+)", line)
                if match:
                    label, value = match.groups()
                    value = float(value)
                    
                    label_map = {
                        "Pressure": ("pressure", None),
                        "Altitude": ("altitude", None),
                        "Acc X": ("acceleration", "x"),
                        "Acc Y": ("acceleration", "y"),
                        "Acc Z": ("acceleration", "z"),
                        "Gyro X": ("gyroscope", "x"),
                        "Gyro Y": ("gyroscope", "y"),
                        "Gyro Z": ("gyroscope", "z")
                    }
                    
                    if label in label_map:
                        key, subkey = label_map[label]
                        if subkey:
                            self.sensor_data[key][subkey] = value
                        else:
                            self.sensor_data[key] = value
        except Exception as e:
            print(f"Error in read_esp32_data: {e}")