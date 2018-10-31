# -*- coding: utf-8 -*-

from .http_status_constants import *

import logging

class TwitterError(Exception):

    """Raised when request fails"""
    def __init__(self, status_code, error_messages):
        self.status_code = status_code
        # Error Messages is the body twitter API return
        # JSON format, should like {"errors":[{"message":"Sorry, that page does not exist","code":34}]}
        self.errors = error_messages.get('errors',[])
        msg = str(self)
        super().__init__(msg)
        
        
    def __str__(self):
        return '(%d) %s' % (self.status_code, self.errors)


class TwitterRequestError(TwitterError):
    
    """HTTP Status Code < HTTP_STATUS_INTERNAL_SERVER_ERROR (Should not retry)"""
    pass

class TwitterServerError(TwitterError):
    
    """HTTP Status Code >= HTTP_STATUS_INTERNAL_SERVER_ERROR (You may retry)"""
    pass

# Notice: The way to invoke super() in Python 2 or Python 3 is different .
# Ref: https://www.pythonforbeginners.com/super/working-python-super-function
# Based on some thought from Clean Code, Add Error Class for each knowen http status code
# While using the library, we want to handling error precise, especially for http status code 420 & 429 
# Because if we do not aware the rate limit, there will be a lot of side effect.
# We add all these classes for  interface consistency and easily check for some code quality tool.
# Ref: https://developer.twitter.com/en/docs/basics/response-codes.html

class TwitterNotModifiedError(TwitterRequestError):
    """HTTP Status Code 304 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_NOT_MODIFIED, error_messages)

class TwitterBadRequestError(TwitterRequestError):
    """HTTP Status Code 400 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_BAD_REQUEST, error_messages)

class TwitterUnauthorizedError(TwitterRequestError):
    """HTTP Status Code 401 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_UNAUTHORIZED, error_messages)

class TwitterForbiddenError(TwitterRequestError):
    """HTTP Status Code 403 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_FORBIDDEN, error_messages)

class TwitterNotFoundError(TwitterRequestError):
    """HTTP Status Code 404 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_NOT_FOUND, error_messages)

class TwitterGoneError(TwitterRequestError):
    """HTTP Status Code 410 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_GONE, error_messages)

class TwitterEnhanceYourCalmError(TwitterRequestError):
    """HTTP Status Code 420 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_ENHANCE_YOUR_CALM, error_messages)

class TwitterUnprocessableEntityError(TwitterRequestError):
    """HTTP Status Code 422 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_UNPROCESSABLE_ENTITY, error_messages)

class TwitterTooManyRequestsError(TwitterRequestError):
    """HTTP Status Code 429 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_TOO_MANY_REQUESTS, error_messages)

class TwitterInternalServerError(TwitterServerError):
    """HTTP Status Code 500 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_INTERNAL_SERVER_ERROR, error_messages)

class TwitterBadGatewayError(TwitterServerError):
    """HTTP Status Code 502 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_BAD_GATEWAY, error_messages)

class TwitterServiceUnavailableError(TwitterServerError):
    """HTTP Status Code 503 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_SERVICE_UNAVAILABLE, error_messages)

class TwitterGatewayTimeoutError(TwitterServerError):
    """HTTP Status Code 504 """
    def __init__(self, error_messages):
        super().__init__(HTTP_STATUS_GATEWAY_TIMEOUT, error_messages)

status_code_errors = {
    HTTP_STATUS_NOT_MODIFIED: TwitterNotModifiedError,
    HTTP_STATUS_BAD_REQUEST: TwitterBadRequestError,
    HTTP_STATUS_UNAUTHORIZED: TwitterUnauthorizedError,
    HTTP_STATUS_FORBIDDEN: TwitterForbiddenError,
    HTTP_STATUS_NOT_FOUND: TwitterNotFoundError,
    HTTP_STATUS_GONE: TwitterGoneError,
    HTTP_STATUS_ENHANCE_YOUR_CALM: TwitterEnhanceYourCalmError,
    HTTP_STATUS_UNPROCESSABLE_ENTITY: TwitterUnprocessableEntityError,
    HTTP_STATUS_TOO_MANY_REQUESTS: TwitterTooManyRequestsError,
    HTTP_STATUS_INTERNAL_SERVER_ERROR: TwitterInternalServerError,
    HTTP_STATUS_BAD_GATEWAY: TwitterBadGatewayError,
    HTTP_STATUS_SERVICE_UNAVAILABLE: TwitterServiceUnavailableError,
    HTTP_STATUS_GATEWAY_TIMEOUT: TwitterGatewayTimeoutError
}


def raise_twitter_error(status_code, error_messages):
    errClass = status_code_errors.get(status_code)
    if errClass is not None:
        raise errClass(error_messages)
    if status_code >= HTTP_STATUS_INTERNAL_SERVER_ERROR:
        raise TwitterServerError(status_code, error_messages)
    raise TwitterRequestError(status_code, error_messages)
