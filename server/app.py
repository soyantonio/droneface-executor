from flask import Flask, abort
import subprocess

app = Flask(__name__)

services = {
    "ad34f389": 0,
    "bd3f8c47": 1,
    "0aa433d2": 2,
    "a73cdae8": 3
}


@app.route('/api/service/<service_id>')
def hello_world(service_id):
    if service_id not in services:
        abort(404)
    subprocess.Popen(["python", "../../droneface-pop/LoadTrained.py"])
    return 'Hello, World!'
