from eve import Eve
from eve.auth import TokenAuth
import requests
from eve.io.mongo import Validator
from flask import request
import json
import jwt
import time
from eve.methods.post import post_internal

secret_key = 'thesecretkey'

CLIENT_ID = ''
CLIENT_SECRET = ''


app = Eve(__name__, settings='settings.py')


@app.route('/login', methods=['POST'])
def login():
    info = request.data
    info = json.loads(info)
    user = app.data.driver.db['accounts']
    user = user.find_one(info)
    if user:
        print(info['username'] + ' has logged in')
        return jwt.encode({'user': info['username'], 'exp': int(time.time()) + 1200}, secret_key)
    else:
        print('someone failed to login')
        return 'fail'


@app.route('/addplugin', methods=['POST'])
def addplugin():
    info = json.loads(request.data)
    print(jwt.decode(info['token'], secret_key)['user'])
    print(not info['submitter'] == jwt.decode(info['token'], secret_key)['user'])
    try:
        if not (info['submitter'] == jwt.decode(info['token'], secret_key)['user']):
            return 'submitter validation fail'
    except:
        return 'submitter validation fail'
    try:
        token = info['token']
        if jwt.decode(token, secret_key):
            del info['token']
            #post to db
            try:
                post_internal('pluginpackages', info)
                #requests.post('http://127.0.0.1:5000/pluginpackages', json.dumps(info), headers={'Content-Type': 'application/json'})
            except:
                return 'error with adding a plugin to database'
            return 'success'
        else:
            return 'token fail'
    except:
        return 'error'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

