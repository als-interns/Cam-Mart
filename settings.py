import os

MONGO_URI = os.getenv('MONGO_URI')

MONGO_HOST = 'mongodb'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'cam-mart'
HTTP_AUTH_METHOD = 'none'
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'unique': True,
        'required': True,
    },
    # # 'role' is a list, and can only contain values from 'allowed'.
    # 'role': {
    #     'type': 'list',
    #     'allowed': ["author", "contributor", "copy"],
    # },
    # An embedded 'strongly-typed' dictionary.
    'documentation': {
        'type': 'dict',
        'schema': {
            'description': {'type': 'string'},
            'keywords': {'type': 'list','schema': {'type':'string'}},
            'authors': {'type': 'list','schema':{'type':'string'}},
            'version': {'type': 'string'},
            'reference': {'type': 'string'},
            'publication': {'type': 'string'}
        },
    },
    'installuri': {
        'type': 'string'
    },
    'submitter': {
        'type': 'string',
        'default': 'person'
    }
}

accountschema = {
    'username': {
        'type': 'string',
        'unique': True,
        'required': True,
        'minlength': 5,
        'maxlength': 20
    },
    'email': {
        'type': 'string',
        'unique': True,
    },
    'id':{
    'type':'string',
    },
    'idprovider': {
        'type': 'string',
        'allowed':['cammart', 'google', 'orcid']
    },
    'password': {
        'type': 'string',
        'minlength': 8,
        'maxlength': 18
    },
    'role': {
        'type':'string',
        'allowed': ["member", "admin"]
    },
    'pluginsowned': {
        'type': 'list',
        'schema': {'type': 'string',
                   'default': 'none'
                   }
    }
}

pluginpackages = {
    'http_auth_method': 'none',
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's'
    # 'item_title': 'pluginpackage',

    # by default the standard item entry point is defined as
    # '/pluginpackages/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/pluginpackages/<name>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',  #TODO: modify to allow '.'
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'schema': schema
}

accounts = {
    'http_auth_method': 'none',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'cache_control': '',
    'cache_expires': 0,
    'allowed_roles': ['admin'],
    'public_methods': ['POST'],
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'public_item_methods': ['POST'],
    'schema': accountschema,
}

DOMAIN = {
    #'accounts': accounts,
    'pluginpackages': pluginpackages,
}


