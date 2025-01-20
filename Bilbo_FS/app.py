#from videoStream import generate_frames
from flask import Flask, Response, render_template, jsonify
from vehicle import Vehicle
from pyCamera import MarsCamera
import subprocess

app = Flask(__name__)

cameras1 = MarsCamera()

# Initialize the Vehicle object
vehicle = Vehicle(hostname="Mars Rover")

@app.route("/")
def home():
    # Get data from the Vehicle class
    os_name = vehicle.get_os()
    current_dir = vehicle.get_path_dir()
    hostname = vehicle.get_hostname()
    
    # Check serial connection
    serial_status = "Connected" if vehicle.confirm_serial_connection() else "Disconnected"
    vehicle.close_connection()

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

@app.route('/run_script', methods=['GET'])
def run_script():
    try:
        # Replace with the correct path to your script
        script_path = r"C:\Users\pable\OneDrive\Escritorio\myAI\capeStation\opencv_camera.py"
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        return jsonify({'message': 'Script executed successfully', 'output': result.stdout})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/video_feed')
# def videoFeed():
#     return Response(vehicle1.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/take_photo')
# def takePhoto():
#     return Response(take_photo(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

