import requests
from flask import Flask, jsonify
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins':'*'}})



@app.route('/plugins')
def run():
    return requests.get('http://cam.lbl.gov:5000/pluginpackages').content

app.run(host='0.0.0.0')