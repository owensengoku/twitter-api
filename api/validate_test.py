# -*- coding: utf-8 -*-

from flask_api import exceptions as fa_exc
from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from .validate import *

import pytest


test_schema = {
    'type' : 'object',
    'properties' : {
        'min1max100' : {
            'type' : 'integer',
            'minimum': 1,
            'maximum': 100,
            'default': 10
        },
        'stringnotwork' : {
            'type' : 'string',
            'default': 'notwork'
        }
    }   
}

def test_convert_args():
    args = MultiDict([('min1max100', '1')])
    convert_args(args, test_schema)
    assert args.get('min1max100') == 1

def test_convert_args_default():
    args = MultiDict()
    convert_args(args, test_schema)
    assert args.get('min1max100') == 10
    assert args.get('stringnotwork') is None

def test_get_args():
    request_args = ImmutableMultiDict([('limit', '1')])
    args = get_args(request_args)
    assert args.get('limit') == 1

def test_get_args_default():
    request_args = ImmutableMultiDict()
    args = get_args(request_args)
    assert args.get('limit') == 30

def test_get_args_min():
    request_args = ImmutableMultiDict([('limit', '0')])
    expected = 'Invalid Parameter'
    with pytest.raises(fa_exc.ParseError, match=expected):
        args = get_args(request_args)

def test_get_args_min():
    request_args = ImmutableMultiDict([('limit', '3201')])
    expected = 'Invalid Parameter'
    with pytest.raises(fa_exc.ParseError, match=expected):
        args = get_args(request_args)