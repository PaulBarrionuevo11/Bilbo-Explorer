#include <WiFi.h>
#include "stdint.h"



class esp32_airhawk_WIFI
{`
private:
    const char* AP_ssid = "APNetwork";
    const char* AP_password = "APPassword";   
    const char* ssid = "MyNetwork";
    const char* password = "MyPassword"; 

public:
    esp32_airhawk_WIFI(/* args */);     // (const char* s, const char* p) : ssid(s), password(p) {}
    ~esp32_airhawk_WIFI();
    void start_AP();
    void connect(const uint8_t s, const uint8_t p);                     // Connect to wifi TODO:
    void disconnect();
    void start_server_communication();                                  // Handles first series of comm with server
    void transmit_data();                                               // Send data to python server
    uint32_t receive_data();                                            // Receive data from python server
};

esp32_airhawk_WIFI::esp32_airhawk_WIFI(/* args */)
{
    connect();

}
void esp32_airhawk_WIFI::start_AP()
{
    Serial.println("Setting up Access Point...");
    WiFi.softAP(AP_ssid, AP_password);
    Serial.print("AP IP address: ");
    Serial.println(WiFi.softAPIP());
    switch (WiFi.status()) {
    case WL_CONNECTED:
        Serial.println("Connected!");
        break;
    case WL_NO_SSID_AVAIL:
        Serial.println("SSID not found!");
        break;
    case WL_CONNECT_FAILED:
        Serial.println("Wrong password!");
        break;
    case WL_DISCONNECTED:
        Serial.println("Disconnected from Wi-Fi!");
        break;
    default:
        Serial.println("Other Wi-Fi error");
        break;
}
}

void esp32_airhawk_WIFI::connect(const uint8_t s, const uint8_t p)
{
    Serial.printf("Connecting to network: %s with password: %s\n", ssid, password);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }
    Serial.println("\nConnected!");
    Serial.printf("IP Address: %s\n", WiFi.localIP().toString().c_str());
}

void esp32_airhawk_WIFI::disconnect()
{
    Wifi.disconnect();
    if (WiFi.status() == WL_DISCONNECTED)
    {
        Serial.println("Disconnected from Wi-Fi!");
    } 
    else {
        Serial.println("Failed to disconnect from WiFi.");
    }
}

esp32_airhawk_WIFI::~esp32_airhawk_WIFI()
{
    disconnect();
}
