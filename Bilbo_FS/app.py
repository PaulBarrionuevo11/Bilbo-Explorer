#from videoStream import generate_frames
from flask import Flask, Response, render_template, jsonify
from vehicle import Vehicle
from navigationCamera import MarsCamera
from ESP32FlightController import ESP32FlightContoller

app = Flask(__name__)

cameras1 = MarsCamera()
flightController = ESP32FlightContoller()

# Initialize the Vehicle object
vehicle = Vehicle(hostname="Mars Rover")

@app.route("/")
def home():
    # Get data from the Vehicle class
    os_name = vehicle.get_os()
    current_dir = vehicle.get_path_dir()
    hostname = vehicle.get_hostname()
    
    # Check serial connection
    serial_status = "Connected" if vehicle.check_USB_connection() else "Disconnected"

    # Pass data to the frontend
    return render_template(
        "home.html",
        os_name=os_name,
        current_dir=current_dir,
        hostname=hostname,
        serial_status=serial_status,
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

@app.route('/get_sensor_data')
def get_sensor_data():
    data = flightController.getData()
    if data is None or data == 0: # No serial connection or no data
        return jsonify({"error": "No Serial Connection Establsihed"})

    elif data:
        return jsonify({
            "imu_accel": data[:3],
            "imu_gyro": data[3:6],
            "extra_accel": data[6:9],
            "ultrasonic": data[9],
        })
    # If you want to handle other cases explicitly:
    else:
        return jsonify({"error": "Unexpected data format"})
    
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

