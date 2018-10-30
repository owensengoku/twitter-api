# -*- coding: utf-8 -*-

from .twitter_error import *
from .variables import *
from .utils import *
import base64
import requests


class TwitterOAuth2(requests.auth.AuthBase):

    """Get access token for Twitter OAuth2 authentication.
    :param consumer_key: Twitter application consumer key
    :param consumer_secret: Twitter application consumer secret
    """

    def __init__(self, consumer_key, consumer_secret, proxies=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self._access_token = None


    def _get_credentials(self):
        auth = '%s:%s' % (self.consumer_key, self.consumer_secret)
        return base64.b64encode(auth.encode('utf8'))

    """
    Allows a registered application to obtain an OAuth 2 Bearer Token, which can be used to make API requests on an application’s own behalf, without a user context. This is called Application-only authentication.
    """
    def get_access_token(self):
        credentials = self._get_credentials()
        params = {'grant_type': 'client_credentials'}
        headers = {}
        headers['User-Agent'] = USER_AGENT
        headers['Authorization'] = 'Basic ' + credentials.decode('utf8')
        headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
        try:
            response = requests.request(
                ENDPOINT_AUTH.get('method',''),
                generate_url(ENDPOINT_AUTH),
                params=params,
                headers=headers)
            data = response.json()
            # HTTP Status Code 200
            if response.status_code == requests.codes['ok']:
                return data['access_token']
            raise_twitter_error(response.status_code, data)
        except TwitterError:
            raise
        except Exception as e:
            raise Exception('Error requesting bearer access token: %s' % e)
    """
    For compatiablility of requests
    """
    def __call__(self, r):
        if self._access_token is None:
            self._access_token = self.get_access_token()

        r.headers['Authorization'] = "Bearer %s" % self._access_token
        return r
