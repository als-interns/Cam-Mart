import requests
import json
o = requests.get('http://127.0.0.1:5000/')
print(o.content)

data = [
        {'name': 'IPython',
        'documentation': {
            'description': 'An IPython console interface which exposes all internal variables of Xi-cam. You can use this to freely manipulate data in Xi-cam.',
            'keywords': ['gui', 'ipython'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://bitbucket.org/lbl-camera/xicam2.plugins.ipython',
         },
        {'name': 'SAXS',
         'documentation': {
             'description': 'A package of plugins for SAXS/WAXS data reduction.',
             'keywords': ['SAXS', 'WAXS', 'scattering'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://github.com/lbl-camera/Xi-cam.plugins.SAXS.git',
         },
        {'name': 'UniqueIPython',
        'documentation': {
            'description': 'An IPython console interface which exposes all internal variables of Xi-cam. You can use this to freely manipulate data in Xi-cam.',
            'keywords': ['gui', 'ipython'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://bitbucket.org/lbl-camera/xicam2.plugins.ipython',
         },
        {'name': 'STUFF',
        'documentation': {
            'description': 'oufoufounoabneofuobeffe',
            'keywords': ['gui', 'ipython'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://bitbucket.org/lbl-camera/xicam2.plugins.ipython',
         },
        {'name': 'UniqueSAXS',
         'documentation': {
             'description': 'Sample sample sample sample sample sample sample sample sample .',
             'keywords': ['SAXS', 'WAXS', 'scattering'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://github.com/lbl-camera/Xi-cam.plugins.SAXS.git',
         },
        {'name': 'QWerty',
        'documentation': {
            'description': 'iubfeuifiuesfiugiraugfiugafiuugfueigfiubgeifbibibfdsbf',
            'keywords': ['gui', 'ipython'],
             'authors': ['Ronald J. Pandolfi'],
             'version': '0.1.0'},
         'installuri': 'pipgit://bitbucket.org/lbl-camera/xicam2.plugins.ipython',
         },
        ]

o = requests.delete('http://127.0.0.1:5000/pluginpackages')


print("deleted")
print(o.content)
print("deleted")
for i in data:
    o = requests.post('http://127.0.0.1:5000/pluginpackages', json.dumps(i), headers={'Content-Type': 'application/json'})
    print(i)

print(o.content)

#o = requests.get('http://127.0.0.1:5000/pluginpackages')
#print(o.content)
