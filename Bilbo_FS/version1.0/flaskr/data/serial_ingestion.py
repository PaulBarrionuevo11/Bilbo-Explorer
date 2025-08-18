import serial
import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found port: {port.device} - {port.description}")

# Check if the intended port exists
if "COM5" not in [port.device for port in ports]:
    print("Error: COM5 not found. Check the connection.")

class ESP32_Serial:
    ser = serial.Serial('COM5', 115200, timeout=None)
    time.sleep(2)
    try:
        if ser.is_open:
            print("Serial port connected at COM5")
        if not ser.is_open:
            print("Serial is not connected")
    except Exception as e:
        print("Exception detected:", e)

    line = ser.readline().decode("utf-8").strip()
    if line:
        print(f"Received: {line}")  # Debugging
