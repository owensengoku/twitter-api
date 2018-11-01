# -*- coding: utf-8 -*-

from flask import request
from flask_api import status
from flasgger.utils import swag_from

from .api import app
from .resource import twitter_back_service
from .response import response_message
from .swagger_spec import haghtags_spec, users_spec
from .validate import get_args


@app.route('/', methods=['GET','POST'])
def welcome():
    return response_message("Welcome to this twtter API")

@app.route('/health', methods=['GET'])
def health_check_handler():
    return response_message("Hello, I am OK!")

@app.route('/hashtags/<hashtag>', methods=['GET'])
@swag_from(haghtags_spec)
def haghtags_handler(hashtag):
    """endpoint returning a list of tweets by hashtag
    This is using docstrings for specifications.
    """
    args = get_args(request.args)
    return twitter_back_service.search_tweets('#%s' % hashtag, args.get('limit'))
   
@app.route('/users/<user>', methods=['GET'])
@swag_from(users_spec)
def users_handler(user):
    args = get_args(request.args)
    return twitter_back_service.user_timeline('@%s' % user, args.get('limit'))

@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found_handler(e):
    return response_message("URI Not Found"), status.HTTP_404_NOT_FOUND
