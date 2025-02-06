from flask import Flask, Response, render_template, jsonify
from nanoVehicle import NanoVehicle
from navigationCamera import MarsCamera
from ESP32FlightController import ESP32FlightContoller

app = Flask(__name__)

esp32FC = ESP32FlightContoller("192.168.4.1", 80)
vehicle = NanoVehicle(hostname="Mars Rover")
cameras1 = MarsCamera()

@app.route("/")
def home():
    # Get ESP32 and Jetson Nano dat
    os_name = vehicle.get_os()
    current_dir = vehicle.get_path_dir()
    hostname = vehicle.get_hostname()
    AP_status = esp32FC.get_AP_connections()
    device_connection = esp32FC.get_connections()

    # Pass data to the frontend
    return render_template(
        "home.html",
        os_name=os_name,
        current_dir=current_dir,
        hostname=hostname,
        AP_status=AP_status,
        device_connection = device_connection
        # serial_status=serial_status,
    )

@app.route('/cameras')
def cameras():
    return render_template("cameras.html", cameras1=cameras1)

# Navigation Camera stream
@app.route('/video_feed')
def video_feed():
    return Response(cameras1.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(cameras1.generate_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(cameras1.generate_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')
##
# @app.route('/get_sensor_data')
# def get_sensor_data():
#     try:
#         # Fetch sensor data from ESP32
#         response = requests.get(ESP_URL, timeout=5)
#         response.raise_for_status()  # Raises an HTTPError for bad responses
#         return response.text
#     except requests.RequestException as e:
#         print(f"Error fetching data from ESP32: {e}")
#         return "Error: Could not retrieve data from ESP32", 500
    
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

