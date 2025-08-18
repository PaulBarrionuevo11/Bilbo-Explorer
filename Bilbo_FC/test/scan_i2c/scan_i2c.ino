#include <Wire.h>
#include <basicMPU6050.h>   // I2C address 0x68
#include <stdint.h>
#include "main.h"


#define IMU_ADDRESS   (0x68)
#define BAUD_RATE     (115200)

basicMPU6050<> imu;
I2C_CONNECTIONS_t i2c_connections[MAX_I2C_CONNECTIONS];

int16_t ax, ay, az, gx, gy, gz; // acceleration and gyroscope
uint16_t nDevices = 0;

void check_i2c_comm(I2C_CONNECTIONS_t *i2c_connections);


void setup() 
{
  Serial.begin(BAUD_RATE);
  Wire.begin();
  Serial.println("I2C Scanner");
  // Initialize MPU6050
  imu.setup();
  imu.setBias();  // Initial bias values - calibration of the gyro
}

void loop() 
{

  check_i2c_comm(i2c_connections);
  imu.updateBias(); // Compensate for drifts or environmental changes
  // Accelerometer data initalization
  ax = imu.ax();
  ay = imu.ay();
  az = imu.az();
  // Gyroscope data initalization
  gx = imu.gx();
  gy = imu.gy();
  gz = imu.gz();
  // #MPU6050 also has tempt
  //float tempImu = imu.temp();
  Serial.println("Acceleration: ");
  Serial.print("X: ");
  Serial.print(ax);
  Serial.print(" - ");
  Serial.print("Y: ");
  Serial.print(ay);
  Serial.print(" - ");
  Serial.print("Z: ");
  Serial.println(az);

  Serial.println("Gyroscope: ");
  Serial.print("X: ");
  Serial.print(gx);
  Serial.print(" - ");
  Serial.print("Y: ");
  Serial.print(gy);
  Serial.print(" - ");
  Serial.print("Z: ");
  Serial.println(gz);
  delay(1200);
}

void check_i2c_comm(I2C_CONNECTIONS_t *i2c_connections)
{
  byte message, address;
  char hexAddress[5]; // Buffer to store "0xNN" (e.g., "0x1A")

  Serial.println("Scanning...");
  for (address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    message = Wire.endTransmission();
    if (message == 0) {
      // Convert address to hexadecimal string
      snprintf(hexAddress, sizeof(hexAddress), "0x%02X", address);
      strcpy(i2c_connections[nDevices].sensorAdd, hexAddress); // Copy string

      Serial.print("I2C device found at address ");
      Serial.println(hexAddress);
      nDevices++;
    }
  }
  if (nDevices == 0) Serial.println("No I2C devices found");
  else Serial.println("Done");

  for (int i = 0; i < nDevices; i++)
  {
    Serial.print("I2C address ");
    Serial.print(i + 1);
    Serial.println(":");
    Serial.print("Device: ");
    Serial.println(i2c_connections[i].sensorAdd);
  }
  delay(1000);
}
