from flask import Flask, Response, render_template
from flask_socketio import SocketIO
from nanoVehicle import NanoVehicle
from navigationCamera import MarsCamera
from ESP32FlightController import ESP32FlightContoller

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

esp32FC = ESP32FlightContoller("192.168.4.1", 80)
vehicle = NanoVehicle(hostname="Mars Rover")
cameras1 = MarsCamera()

# Start Serial Reading in Background
# threading.Thread(target=esp32FC.read_serial(), daemon=True).start()

@app.route("/")
def home():
    serial_connection = esp32FC.open_serial_connection()
    # Get ESP32 and Jetson Nano dat
    os_name = vehicle.get_os()
    current_dir = vehicle.get_path_dir()
    hostname = vehicle.get_hostname()
    AP_status = esp32FC.get_IP_connections()
    device_connection = esp32FC.get_count_IP_connections()
    # try:
    #     while True:
    #         esp32FC.get_data()
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     print("Stopping data collection...")
    # finally:
    #     esp32FC.close_connection()

    # Pass data to the frontend
    return render_template(
        "home.html",
        os_name=os_name,
        current_dir=current_dir,
        hostname=hostname,
        AP_status=AP_status,
        device_connection = device_connection,
        serial_connection = serial_connection
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
    
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    import threading
    thread = threading.Thread(target=esp32FC.read_serial(), daemon=True)
    thread.start()
    socketio.run(debug=True)

