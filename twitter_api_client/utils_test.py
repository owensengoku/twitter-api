# -*- coding: utf-8 -*-

from .utils import *

from datetime import datetime

def test_generate_url_noversion():
    test_endpoint = {
        'subdomain':'testcategroy',
        'path': 'test/relativepath',
        'version': NOVERSION,
        'method': 'unusedmethod'
    }
    assert generate_url(test_endpoint) == 'https://testcategroy.twitter.com/test/relativepath'

def test_generate_url_version():
    test_endpoint = {
        'subdomain':'testcategroy',
        'path': 'test/relativepath',
        'version': '9.9',
        'method': 'unusedmethod'
    }
    assert generate_url(test_endpoint) == 'https://testcategroy.twitter.com/9.9/test/relativepath' 

def test_get_rate_limit_info():
    test_headers = {
        'x-rate-limit-limit': '1500',
        'x-rate-limit-remaining': '1497',
        'x-rate-limit-reset': '1540917079'
    }
    assert get_rate_limit_info(test_headers) == {'remaining': 1497, 'limit': 1500, 'reset': datetime.fromtimestamp(1540917079)}