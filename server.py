# -*- coding: utf-8 -*-

import sys
import os
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(SCRIPT_DIR))

def get_config_from_env():
    key_default_values = {
        'APPLICATION_HOST': '0.0.0.0',
        'APPLICATION_PORT': '5000',
        'APPLICATION_CONFIG_PATH': None,
        'TWITTER_API_CONSUMER_KEY': 'key',
        'TWITTER_API_CONSUMER_SECRET': 'secret'
    }
    ret = {}
    for k, v in key_default_values.items():
        ret[k] = os.getenv(k, v)
    return ret

cfgs = get_config_from_env()

from api import api
# Setting application for gunicorn default setting
application = api.get_application(cfgs)

if __name__ == '__main__':
    # For development environemnt
    api.run()
