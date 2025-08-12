from typing import List, Optional
from pydantic import BaseModel

# Data obtained from MPU6050 wihtout the tempt
class ImuData(BaseModel):
    acceleration: List[float]
    angular_velocity: List[float]
    timestamp: float # Unix timestamp in secs

# Data obtained from barometer BMP 280
class BarometerData(BaseModel):
    altitude: float
    pressure: float
    temperature: float
    timestamp: float

# Data obtained from LSM303DLHC Adafruit Compass+Accel sensor
class CompassData(BaseModel):
    orientation: float
    timestamp: float

# Data obtained from Ultrasound sensor
class UltrasoundData(BaseModel):
    distance: float
    timestamp: float

# Data sent if the motors have been activated or not. All motors equal True, anthing else is False
class ESCData(BaseModel):
    active: bool
    timestamp: float

# Collect all the data from different sensors
class ESP32Telemetry(BaseModel):
    imu: ImuData
    barometer: BarometerData
    compass: CompassData
    ultrasound: UltrasoundData
    esc: ESCData
    device_id: str
    battery_level: Optional[float] =  None

# Send commands that are received by the ESP32
class ESP32Command(BaseModel):
    command: str
    device_id: str
