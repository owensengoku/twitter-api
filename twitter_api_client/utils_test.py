# -*- coding: utf-8 -*-

from .utils import *


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