from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from esp32 import ESP32FlightController

app = Flask(__name__)
CORS(app)  # Enable CORS for browser fetch requests

esp32FC = ESP32FlightController()

# Store latest sensor data
latest_sensor_data = {
    "accelX": 0.0,
    "accelY": 0.0,
    "accelZ": 0.0,
    "gyroX": 0.0,
    "gyroY": 0.0,
    "gyroZ": 0.0
}

@app.route('/update-sensor', methods=['POST'])
def update_sensor():
    try:
        data = request.json
        if not data:
            print("Error: No JSON data received")
            return jsonify({"status": "error", "message": "No JSON data"}), 400
        print(f"Received: {data}")  # Debug log
        global latest_sensor_data
        latest_sensor_data = data  # Update with new data
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error processing POST: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get-sensor-data', methods=['GET'])
def get_sensor_data():
    try:
        print(f"Serving data: {latest_sensor_data}")  # Debug log
        return jsonify(latest_sensor_data)
    except Exception as e:
        print(f"Error serving data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def home():
    esp32FC.read_esp32_data()
    return render_template('home.html')
@app.route('/test')
def test():
    esp32FC.read_esp32_data()
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)  # Disable debug for performance