# -*- coding: utf-8 -*-

from .twitter_error import *
from .variables import *
from .utils import *

from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError

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
                    return response.json()
                raise_twitter_error(response.status_code, response.json())
            except TwitterError:
                raise
            except (ConnectionError, ProtocolError, ReadTimeout, ReadTimeoutError,
                    SSLError, ssl.SSLError, socket.error) as e:
                raise NetworkError(e)
            except Exception as e:
                raise Exception('Error requesting twitter api: %s, exception: %s' % (endpoint,e))

    def search_tweets(self, keyword, options=None):
        params = options.copy()  
        params['q'] = keyword  
        return self.request(ENDPOINT_SEARCH, params=params)
