from flask import Flask, render_template, jsonify, request
import socket
import threading
import json

app = Flask(__name__)

@app.route('/update-sensor', methods=['POST'])
def update_sensor():
    data = request.json
    print(f"Received: {data}")
    return jsonify({"status": "success"}), 200

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)