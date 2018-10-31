# -*- coding: utf-8 -*-

from .twitter_error import *
from .variables import *
from .utils import *

from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
from datetime import datetime

import requests
import socket
import ssl


class TwitterAPI(object):

    """Access Twitter RESTful API.
 
    :param auth: Twitter Auth Object
    """
    def __init__(self, auth, timeout=None):
        self.auth = auth
        self.timeout = REQUEST_TIMEOUT if timeout == None else timeout

    def request(self, endpoint, params=None, data=None, timeout=None):
        """Request a Twitter RESTful API.

        :param endpoint: A Twitter API endpoint Dictionary
        :param params: Dictionary with endpoint parameters, default is None.
        :param data: Dictionary with endpoint data(in HTTP body), default is None.
        :param timeout: (optional) How many seconds to wait for the server to send data
                         before giving up, as  a :ref:`(connect timeout, read timeout) 
                         <timeouts>` tuple.
        :returns: TwitterResponse
        :raises: TwitterError
        """
        if timeout is None:
            timeout = self.timeout

        with requests.Session() as session:
            session.auth = self.auth
            session.headers = {'User-Agent': USER_AGENT}
            
            try:
                response = session.request(
                    endpoint.get('method',''),
                    generate_url(endpoint),
                    data=data,
                    params=params,
                    timeout=timeout)
                # HTTP Status Code 200
                if response.status_code == requests.codes['ok']:
                    return get_result(response, endpoint.get('return'))
                raise_twitter_error(response.status_code, response.json())
            except TwitterError:
                raise
            except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError,
                    SSLError, ssl.SSLError, socket.error) as e:
                raise NetworkError(e)
            except Exception as e:
                raise Exception('Error requesting twitter api: %s, exception: %s' % (endpoint,e))

    # Ref: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
    def search_tweets(self, keyword, options={}):
        params = options.copy()  
        params['q'] = keyword  
        return self.request(ENDPOINT_SEARCH, params=params)

    # Ref: https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html
    def user_timeline(self, user_id=None, screen_name=None, options={}):
        params = options.copy()
        # Check if user_id and screen_name are used at the same time is just to remind.
        # Actually, after trying with twitter API.
        # If pass these two argument at the same time, only screen_name work, twitter API will ignore the user_id argument.
        if all([user_id, screen_name]):
            # raise ValueError, reference is following URL.
            # https://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python 
            raise ValueError('user_id, screen_name only should use only one at the same time')

        if user_id is not None:
            params['user_id'] = user_id
        if screen_name is not None:
            params['screen_name'] = screen_name

        return self.request(ENDPOINT_USER_TIMELINE, params=params)

    # Ref: https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status
    def rate_limit_status(self, options={}):
        params = options.copy()
        ret = self.request(ENDPOINT_RATE_LIMIT_STATUS, params=params)
        # Make constitent data format with rate limit info  
        # Convert the UTC epoch to datetime.datetime
        # Notice: iterate the dictionary with .items is for Python 3
        # Ref: https://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems
        for group, epdict in ret.get('result',{}).items():
            for k, v in epdict.items():
                ret['result'][group][k]['reset'] = datetime.fromtimestamp(v.get('reset',0))
        return ret