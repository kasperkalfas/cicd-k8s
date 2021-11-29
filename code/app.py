from flask import Flask
from flask import jsonify
import subprocess

app = Flask(__name__)

@app.route('/healthz', methods= ['GET'])
def healthz():
    data = {'message': 'HTTP 200 OK', 'code': 'OK'}
    resp = jsonify(data)
    resp.status_code = 200
    return resp

@app.route('/', methods= ['GET'])
def home():
    bashCommandName = "hostname"
    output = subprocess.check_output(bashCommandName, shell=True).decode('utf-8')
    data = "Hello CloudState from hostname: " + output
    resp = jsonify(data)
    resp.status_code = 200
    return resp

app.run(host = '0.0.0.0', port=80)