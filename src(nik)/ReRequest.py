<<<<<<< HEAD
#since I can't access lbl plugins with vue i just resend them localy and request from there. 
#CORS isn't going to be an issue since both will be in the same origin, right?

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
=======
#since I can't access lbl plugins with vue i just resend them localy and request from there. 
#CORS isn't going to be an issue since both will be in the same origin, right?

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
>>>>>>> 3db6d2df29db68840b6b21aaa521a2013453e167
