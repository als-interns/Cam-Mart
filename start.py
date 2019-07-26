from eve import Eve
from eve.auth import BasicAuth
from eve.io.mongo import Validator
from flask import request
import json
import bcrypt
from redis import StrictRedis

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if method == 'GET' and not resource == 'accounts':
            return True
        if resource == 'pluginpackages' and method == 'POST':
            user = app.data.driver.db['accounts']
            user = user.find_one({'username': username, 'password': password})
            if user:
                return True
            else:
                return False
        elif resource == 'accounts' and method == 'POST':
            return True
        elif resource == 'login' and method == 'POST':
            return True
        else:
            return False


app = Eve(auth=MyBasicAuth, settings='settings.py')


@app.route('/login', methods=['POST'])
def login():
    info = request.data
    #info = info.decode('utf-8') <-- converts to str, not necesary
    info = json.loads(info)
    user = app.data.driver.db['accounts']
    user = user.find_one(info)
    if user:
        print(info['username'] + ' has logged in')
        return 'ok'
    else:
        print('someone failedto login')
        return 'fail'


if __name__ == '__main__':
    app.run()

