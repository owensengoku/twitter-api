# -*- coding: utf-8 -*-

from .variables import *

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