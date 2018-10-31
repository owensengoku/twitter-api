# -*- coding: utf-8 -*-

from .api import app
from pprint import pprint
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_root(client):
    """Root Path."""

    ret = client.get('/')
    assert ret.status_code == 200
    assert b'Welcome to this twtter API' in ret.data

def test_health_check(client):
    """Health Check API."""

    ret = client.get('/health')
    assert ret.status_code == 200
    assert b'Hello, I am OK!' in ret.data

def test_hashtags(client):
    """hashtags API."""

    ret = client.get('/hashtags/tagname')
    assert ret.status_code == 200
    assert b'I got you want find hashtag: #tagname' in ret.data

def test_users(client):
    """users API."""

    ret = client.get('/users/username')
    assert ret.status_code == 200
    assert b'I got you want find user: @username' in ret.data

def test_not_found(client):
    """users API."""

    ret = client.get('/not_found')
    assert ret.status_code == 404
    assert b'URI Not Found' in ret.data