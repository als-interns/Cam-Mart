import requests
import json
o = requests.get('http://127.0.0.1:5000/')
print(o.content)

data = [
    # {'name': 'IPython',
    #     'plugins': ['IPythonPlugin'],
    #     'documentation': {
    #         'description': 'An IPython console interface which exposes all internal variables of Xi-cam. You can use this to freely manipulate data in Xi-cam.',
    #         'keywords': ['gui', 'ipython'],
    #         'authors': ['Ronald J. Pandolfi'],
    #         'version': '0.1.0'},
    #     'installuri': 'pipgit://bitbucket.org/lbl-camera/xicam2.plugins.ipython',
    #     },
        {'name': 'Log',
         'plugins': ['LogPlugin'],
         'documentation': {
             'description': 'A logging display which exposes history of logged messages for debugging purposes.',
             'keywords': ['debug', 'log'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://github.com/ronpandolfi/xicam.plugins.log.git',
         }
        ]

o = requests.delete('http://127.0.0.1:5000/pluginpackages/IPython')
print(o.content)

o = requests.post('http://127.0.0.1:5000/pluginpackages', json.dumps(data), headers={'Content-Type': 'application/json'})
print(o.content)

o = requests.get('http://127.0.0.1:5000/pluginpackages')
print(o.content)

o = requests.get('http://127.0.0.1:5000/pluginpackages/IPython')
print(json.loads(o.content)["installuri"])
