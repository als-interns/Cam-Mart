from eve import Eve
from eve.auth import BasicAuth
from eve.io.mongo import Validator
from flask import request
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
        else:
            return False



app = Eve(auth=MyBasicAuth, settings='settings.py')



if __name__ == '__main__':
    app.run()

