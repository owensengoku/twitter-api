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

RETURN_ALL = 'RETURNALL'

# Ref: https://developer.twitter.com/en/docs/basics/authentication/api-reference/token
ENDPOINT_AUTH = {
    'subdomain': 'api',
    'version': NOVERSION,
    'path': 'oauth2/token',
    'method': 'post'
}

# Ref: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
ENDPOINT_SEARCH = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'search/tweets.json',
    'method': 'get',
    'return' : 'statuses'
}

# Ref: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html
ENDPOINT_USER_TIMELINE = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'statuses/user_timeline.json',
    'method': 'get',
    'return': RETURN_ALL
}

# Ref: https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status
ENDPOINT_RATE_LIMIT_STATUS = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'application/rate_limit_status.json',
    'method': 'get',
    'return': 'resources'
}
