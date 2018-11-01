# -*- coding: utf-8 -*-

from flask_api import FlaskAPI
from flasgger import Swagger

app = FlaskAPI(__name__)
app.config['SWAGGER'] = {
    'title': 'Twitter API',
    'version': '0.1.0',
    'description': 'An API for fetch tweets from Twitter API'
}
swagger = Swagger(app)

# Ref: http://flask.pocoo.org/docs/1.0/config/
# Ref: http://flask.pocoo.org/docs/1.0/api/#flask.Config
# Notice: Flask Built-in Environment Variable with high priority
# Like : FALSK_ENV, FLASK_DEBUG
# Environment Variables will overwrite the config from file
app.config.from_pyfile('default.cfg')

from .resource import init_resoureces
from .handler import *

def set_config(cfg):
    if cfg.get('APPLICATION_CONFIG_PATH') is not None:
        app.config.from_envvar('APPLICATION_CONFIG_PATH')
    for k,v in cfg.items():
        if v is not None:
            app.config[k] = v

def get_application(cfg):
    set_config(cfg)
    init_resoureces()
    return app

def run():
    app.run(host=app.config.get('APPLICATION_HOST'), port=app.config.get('APPLICATION_PORT'))
