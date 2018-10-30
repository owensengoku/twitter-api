# -*- coding: utf-8 -*-

# Constant for Twiter API

# Version 1.1 REST API & Streaming API
    

SCHEME = 'https'
ROOT_DOMAIN = 'twitter.com'
VERSION = '1.1'
NOVERSION = 'NOVERSION'
USER_AGENT = 'twitter-api-client'

# timeout default value for requests
# https://github.com/requests/requests/blob/master/requests/api.py#L34
CONNECT_TIMEOUT = 10
READ_TIMEOUT = 10
REQUEST_TIMEOUT = (CONNECT_TIMEOUT, READ_TIMEOUT)

ENDPOINT_AUTH = {
    'subdomain': 'api',
    'version': NOVERSION,
    'path': 'oauth2/token',
    'method': 'post'
}

ENDPOINT_SEARCH = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'search/tweets.json',
    'method': 'get'
}

ENDPOINT_USER_TIMELINE = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'statuses/user_timeline.json',
    'method': 'get'
}
