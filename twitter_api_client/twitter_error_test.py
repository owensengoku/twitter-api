# -*- coding: utf-8 -*-

from .twitter_error import *

import pytest

def test_raise_not_modified():
    status_code = 304
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterNotModifiedError):
        raise_twitter_error(status_code, error_messages)

def test_raise_bad_request():
    status_code = 400
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterBadRequestError):
        raise_twitter_error(status_code, error_messages)

def test_raise_unauthorized():
    status_code = 401
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterUnauthorizedError):
        raise_twitter_error(status_code, error_messages)

def test_raise_forbiddend():
    status_code = 403
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterForbiddenError):
        raise_twitter_error(status_code, error_messages)

def test_raise_not_found():
    status_code = 404
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterNotFoundError):
        raise_twitter_error(status_code, error_messages)

def test_raise_enhance_your_calm():
    status_code = 420
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterEnhanceYourCalmError):
        raise_twitter_error(status_code, error_messages)

def test_raise_unprocessable_entity():
    status_code = 422
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterUnprocessableEntityError):
        raise_twitter_error(status_code, error_messages)

def test_raise_too_many_requests():
    status_code = 429
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterTooManyRequestsError):
        raise_twitter_error(status_code, error_messages)

def test_raise_internal_server_error():
    status_code = 500
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterInternalServerError):
        raise_twitter_error(status_code, error_messages)


def test_raise_bad_gateway():
    status_code = 502
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterBadGatewayError):
        raise_twitter_error(status_code, error_messages)

def test_raise_service_unavailable():
    status_code = 503
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterServiceUnavailableError):
        raise_twitter_error(status_code, error_messages)

def test_raise_gateway_timeout():
    status_code = 504
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterGatewayTimeoutError):
        raise_twitter_error(status_code, error_messages)

def test_raise_reuqest_error():
    status_code = 301
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterRequestError):
        raise_twitter_error(status_code, error_messages)

def test_raise_server_error():
    status_code = 505
    error_messages = {'errors':{'code':99,'message':'unknow'}}
    with pytest.raises(TwitterServerError):
        raise_twitter_error(status_code, error_messages)
