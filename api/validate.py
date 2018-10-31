# -*- coding: utf-8 -*-

from jsonschema import validate
from jsonschema import exceptions as js_exc
from flask_api import exceptions as fa_exc
from .variables import DEFAULT_LIMIT

import logging

query_schema = {
    'type' : 'object',
    'properties' : {
        'limit' : {
            'type' : 'integer',
            'minimum': 1,
            'maximum': 3200,
            'default': DEFAULT_LIMIT
        }
    }   
}

# Notice: jsonschema could support "default"
# Ref: https://github.com/Julian/jsonschema/blob/8cc6a5af0b5ab343707c0c71021c477651aa479b/docs/faq.rst
# After trying, it could not work in Python 3, it is an issue about jsonschema
# Maybe we should send an PR later
# So add this method for support default, and convert the string to int
# Simple support current use case
def convert_args(args, schema):
    for k,v in schema.get('properties',{}).items():
        if v.get('type') == 'integer':
            arg = args.get(k)
            if arg is None:
                args[k] = v.get('default')
            else:
                args[k] = int(arg)

def get_args(args):
    # Because the input args is an ImmutableMultiDict, use copy() to generate ret(MultiDict)
    ret = args.copy()
    try:
        convert_args(ret, query_schema)
        validate(ret, query_schema)
    except Exception as e:
        logging.debug('Invalid Parameters %s' % e)
        raise fa_exc.ParseError('Invalid Parameter')
    return ret