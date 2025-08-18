#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <basicMPU6050.h>   // I2C address 0x68
#include <stdint.h>
#include "main.h"
#include <ArduinoJson.h> // Use ArduinoJson for JSON serialization

#define IMU_ADDRESS   (0x68)
#define BAUD_RATE     (115200)

basicMPU6050<> imu;
I2C_CONNECTIONS_t i2c_connections[MAX_I2C_CONNECTIONS];
float ax, ay, az, gx, gy, gz; // acceleration and gyroscope
uint16_t nDevices = 0;

// Wi-Fi credentials
const char* ssid = "Dhamma";
const char* password = "Bonfire2025$$";
// Flask server details
const char* serverName = "http://10.0.0.110:5001/update-sensor";
void check_i2c_comm(I2C_CONNECTIONS_t *i2c_connections);


void setup() 
{
  Serial.begin(BAUD_RATE);
  Wire.begin();
  Serial.println("I2C Scanner");
  // Initialize MPU6050
  imu.setup();
  imu.setBias();  // Initial bias values - calibration of the gyro
  check_i2c_comm(i2c_connections);


  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void loop() {
  imu.updateBias();
  ax = imu.ax();
  ay = imu.ay();
  az = imu.az();
  gx = imu.gx();
  gy = imu.gy();
  gz = imu.gz();

  StaticJsonDocument<200> doc;
  doc["accelX"] = ax;
  doc["accelY"] = ay;
  doc["accelZ"] = az;
  doc["gyroX"] = gx;
  doc["gyroY"] = gy;
  doc["gyroZ"] = gz;

  String jsonData;
  serializeJson(doc, jsonData);
  Serial.println("Sending JSON: " + jsonData);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://10.0.0.110:5001/update-sensor"); // Replace <server-ip>
    http.addHeader("Content-Type", "application/json");
    http.setTimeout(5000);

    int httpResponseCode = http.POST(jsonData);
    if (httpResponseCode > 0) {
      Serial.printf("HTTP POST success, code: %d\n", httpResponseCode);
      String response = http.getString();
      Serial.println("Response: " + response);
    } else {
      Serial.printf("HTTP POST failed, error: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();
  } else {
    Serial.println("WiFi disconnected");
    WiFi.reconnect(); // Attempt to reconnect
  }
  delay(1000);
  Serial.printf("Accel: X=%f, Y=%f, Z=%f\n", ax, ay, az);
  Serial.printf("Gyro: X=%f, Y=%f, Z=%f\n", gx, gy, gz);
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
