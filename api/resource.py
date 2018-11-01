# -*- coding: utf-8 -*-

from .back_service import TwitterBackService
from .api import app

twitter_back_service = TwitterBackService()

def init_resoureces():
    twitter_back_service.init_app(app)
    

