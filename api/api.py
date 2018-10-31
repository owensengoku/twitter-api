# -*- coding: utf-8 -*-

from flask import request
from flask_api import FlaskAPI, status
from .response import response_message
from .validate import get_args
from .variables import *

app = FlaskAPI(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET','POST'])
def welcome():
    return response_message("Welcome to this twtter API")

@app.route('/health', methods=['GET'])
def health_check_handler():
    return response_message("Hello, I am OK!")


@app.route('/hashtags/<hashtag>', methods=['GET'])
def haghtags_handler(hashtag):
    args = get_args(request.args)
    return response_message("I got you want find hashtag: #%s" % hashtag )

@app.route('/users/<user>', methods=['GET'])
def users_handler(user):
    args = get_args(request.args)
    return response_message("I got you want find user: @%s" % user )

@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found_handler(e):
    return response_message("URI Not Found"), status.HTTP_404_NOT_FOUND


def run():
    app.run()

if __name__ == "__main__":
    run()