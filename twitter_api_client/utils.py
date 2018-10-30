# -*- coding: utf-8 -*-

from .variables import *

from datetime import datetime

# URL foramt of the API
# {SCHEME}://{subdomain}.{ROOT_DOMAIN}{version_path}/{path}?{parameters}

def generate_url(endpoint):
    v = endpoint.get('version')
    # becasue some api url without version
    version_path = '' if v == NOVERSION else '/%s' % v
    return '%s://%s.%s%s/%s' % (SCHEME, 
                                endpoint.get('subdomain',''),
                                ROOT_DOMAIN,
                                version_path, 
                                endpoint.get('path',''))

# Ref: https://developer.twitter.com/en/docs/basics/rate-limiting.html
# x-rate-limit-limit: the rate limit ceiling for that given endpoint
# x-rate-limit-remaining: the number of requests left for the 15 minute window
# x-rate-limit-reset: the remaining window before the rate limit resets, in UTC epoch seconds

def get_rate_limit_info(headers):
    """ Get Rate Limit Information from response headers (A Dictionary)
    :returns: Dictionary of 'remaining' (int), 'limit' (int), 'reset' (time)
    """
    ret = {}
    ret['remaining'] = int(headers.get('x-rate-limit-remaining'))
    ret['limit'] = int(headers.get('x-rate-limit-limit'))
    ret['reset'] = datetime.fromtimestamp(int(headers.get('x-rate-limit-reset')))
    return ret


def get_result(response, return_property):
    data = response.json()
    if return_property == RETURN_ALL:
        results = data
    else:
        results = data.get(return_property)
    return {
        'rate_limit_info': get_rate_limit_info(response.headers),
        'results': results
    }