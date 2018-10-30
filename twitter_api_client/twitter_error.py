# -*- coding: utf-8 -*-

import logging


# Ref: https://developer.twitter.com/en/docs/basics/response-codes.html


status_code_descriptions = {
    200 : ' Success!'
}


class TwitterError(Exception):

    """Raised when request fails"""
    def __init__(self, status_code, error_messages):
        self.status_code = status_code
        # Error Messages is the body twitter API return
        # JSON format, should like {"errors":[{"message":"Sorry, that page does not exist","code":34}]}
        self.error_messages = error_messages
        msg = str(self)
        super(Exception, self).__init__(msg)
        
        
    def __str__(self):
        return '(%d) %s' % (self.status_code, self.error_messages )


class TwitterRequestError(TwitterError):
    
    """HTTP Status Code < 500 (Should not retry)"""
    pass

class TwitterServerError(TwitterError):
    
    """HTTP Status Code >= 500 (You may retry)"""
    pass

def raise_twitter_error(status_code, error_messages):
    if status_code >= 500:
        raise TwitterServerError(status_code, error_messages)
    raise TwitterRequestError(status_code, error_messages)
