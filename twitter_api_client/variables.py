# -*- coding: utf-8 -*-

# Constant for Twiter API

# Version 1.1 REST API & Streaming API
    

SCHEME = 'https'
ROOT_DOMAIN = 'twitter.com'
VERSION = '1.1'
NOVERSION = 'NOVERSION'
USER_AGENT = 'twitter-api-client'

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

