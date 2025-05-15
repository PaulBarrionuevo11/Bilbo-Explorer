from flask import Flask, render_template, Response, jsonify
import time
import json
from nano import NanoVehicle
from esp32 import ESP32FlightController

app = Flask(__name__)

# Initialize hardware
rover = NanoVehicle(hostname="Mars Rover")
esp32FC = ESP32FlightController()

# Route for the main page
@app.route('/')
def index():
    uart_connection = rover.check_UART_connection()
    return render_template('index.html', uart_connection=uart_connection)

@app.route('/gs')
def gs():
    uart_connection = rover.check_UART_connection()
    return render_template('gs.html', uart_connection=uart_connection)

# SSE endpoint for sensor data
@app.route('/sensor_stream')
def sensor_stream():
    def generate():
        ser = rover.uart_connection()
        print(f"Streaming started. UART Connection: {ser}")
        time.sleep(2)  # Wait for ESP32 to stabilize
        ser.reset_input_buffer()
        while True:
            esp32FC.read_esp32_data(ser)
            data = esp32FC.sensor_data
            print(f"Streaming data: {data}")  # Debug log
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(0.1)  # Adjust update rate
    return Response(generate(), mimetype='text/event-stream')

# Optional JSON endpoint for debugging
@app.route('/sensor_data')
def sensor_data():
    return jsonify(esp32FC.sensor_data)

if __name__ == '__main__':
    print("Starting Flask server on http://0.0.0.0:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)