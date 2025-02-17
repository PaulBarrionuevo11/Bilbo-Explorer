from flask import Flask, Response, render_template, jsonify
from flask_socketio import SocketIO
from nanoVehicle import NanoVehicle
from navigationCamera import RoverCamera
from ESP32FlightController import ESP32FlightController
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

esp32FC = ESP32FlightController()
esp32FC.open_serial_connection()
serial_connection = esp32FC.is_serial_connected


thread = threading.Thread(target=esp32FC.read_esp32_data, daemon=True)
thread.start()

rover = NanoVehicle(hostname="Mars Rover")
roverCam = RoverCamera()




@app.route("/")
def home():
    # Get ESP32 and Jetson Nano dat
    os_name = rover.get_os()
    current_dir = rover.get_path_dir()
    hostname = rover.get_hostname()
    esp32FC.open_serial_connection()

    # Pass data to the frontend
    return render_template(
        "home.html",
        os_name=os_name,
        current_dir=current_dir,
        hostname=hostname,
        serial_connection = serial_connection
        # serial_status=serial_status,
    )

@app.route('/flight')
def flight():  # Make sure this matches 'sensor_data'
    return render_template(
        'control_panel.html',
        serial_connection = serial_connection
)

@app.route('/sensor_data')
def sensor_data():
    return jsonify(esp32FC.sensor_data)

@app.route('/cameras')
def cameras():
    return render_template("cameras.html", roverCam=roverCam)

# Navigation Camera stream
@app.route('/video_feed')
def video_feed():
    return Response(roverCam.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed1')
def video_feed1():
    return Response(roverCam.generate_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(roverCam.generate_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)

