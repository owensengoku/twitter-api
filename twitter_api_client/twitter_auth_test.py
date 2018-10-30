# -*- coding: utf-8 -*-

from .twitter_auth import TwitterOAuth2 
from .twitter_error import *
from .utils import generate_url
from .variables import ENDPOINT_AUTH

import pytest
import requests

def test_get_access_token(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    consumer_key = 'key'
    consumer_secret = 'secret'
    client = TwitterOAuth2(consumer_key, consumer_secret)
    token = client.get_access_token()
    assert token  == 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'

def test_get_access_token(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), status_code=403, json={'errors': [{'code': 99, 'message': 'Unable to verify your credentials', 'label': 'authenticity_token_error'}]})
    consumer_key = 'key'
    consumer_secret = ''
    client = TwitterOAuth2(consumer_key, consumer_secret)
    expected = "'code': 99, 'message': 'Unable to verify your credentials'"
    with pytest.raises(TwitterRequestError, match=expected):
        token = client.get_access_token()
    