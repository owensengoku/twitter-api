# -*- coding: utf-8 -*-

from flask_api import FlaskAPI

import os
app = FlaskAPI(__name__)
app.config["DEBUG"] = True

app.config['TWITTER_API_CONSUMER_KEY'] = os.getenv('TWITTER_API_CONSUMER_KEY')
app.config['TWITTER_API_CONSUMER_SECRET'] = os.getenv('TWITTER_API_CONSUMER_SECRET')

from .resource import init_resoureces
init_resoureces()

from .handler import *

def run():
    app.run()

if __name__ == "__main__":
    run()