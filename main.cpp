/*
    Author: Paul Barrionuevo
    Date: 01/20/2025
    Description: ESP32WROOM Flight Controller - BILBO FC
*/

#include <Arduino.h>
#include <basicMPU6050.h>   // I2C address 0x68
#include <Adafruit_BMP280.h> // I2C address 0x76
#include <stdint.h>

/*
    VARIABLES AND CLASS DECLARATIONS
*/
basicMPU6050<> imu;
Adafruit_BMP280 bmp;
float ax, ay, az, gx, gy, gz; // acceleration and gyroscope
float pressure, altitude, temperatureBMP;
const float altitude_val = 1013.25; // Adjustable or optional
unsigned status;

/*
    FreeRTOS FUNCTIONS 
*/
void taskAlt(void * parameter)
{
    while(1)
    {
        pressure = bmp.readPressure();
        altitude = bmp.readAltitude(altitude_val);  
        temperatureBMP = bmp.readTemperature();
        // Serial.print(F("Pressure = "));
        Serial.println("Pressure: " + String(pressure) + "hPa"); 
        Serial.println("Altitude: " + String(altitude) + " m"); 
        Serial.println("Temperature: " + String(temperatureBMP) + "Celsius");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

void taskIMU(void * parameter)
{
    while (1)
    {
        imu.updateBias(); // Compensate for drifts or environmental changes
        // Accelerometer data initialization
        ax = imu.ax();
        ay = imu.ay();
        az = imu.az();
        // Gyroscope data initialization
        gx = imu.gx();
        gy = imu.gy();
        gz = imu.gz();
        // TODO: MPU6050 has tempt readings
        Serial.println("Acc X: " + String(ax));
        Serial.println("Acc Y: " + String(ay));
        Serial.println("Acc Z: " + String(az));
        Serial.println("Gyro X: " + String(gx));
        Serial.println("Gyro Y: " + String(gy));
        Serial.println("Gyro Z: " + String(gz));
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

/*
    REGULAR FUNCTIONS
*/
void setup() {
    
    Serial.begin(115200);
    //status = bmp.begin(BMP280_ADDRESS_ALT, BMP280_CHIPID);
    status = bmp.begin(0x76);
    /* Default settings from datasheet. */
    bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                    Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                    Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                    Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                    Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

    // Initialize MPU6050
    imu.setup();
    imu.setBias();  // Initial bias values - calibration of the gyro
    xTaskCreate(
        taskAlt, 
        "Altimeter", 
        2048, 
        NULL,
        1, 
        NULL
    );
    xTaskCreate(
        taskIMU, 
        "IMU", 
        2048, 
        NULL, 
        1, 
        NULL
    );
}
void loop() {
    vTaskDelay(500 / portTICK_PERIOD_MS);
}

/*
I2C SCANNER CODE:
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Serial.println("I2C Scanner");
}

void loop() {
  byte error, address;
  int nDevices = 0;

  Serial.println("Scanning...");
  for (address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address < 16) Serial.print("0");
      Serial.println(address, HEX);
      nDevices++;
    }
  }
  if (nDevices == 0) Serial.println("No I2C devices found");
  else Serial.println("Done");
  delay(5000);
} 
*/