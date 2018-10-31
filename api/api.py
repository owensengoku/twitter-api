# -*- coding: utf-8 -*-


from flask_api import FlaskAPI

app = FlaskAPI(__name__)
app.config["DEBUG"] = True

from .handler import *

def run():
    app.run()

if __name__ == "__main__":
    run()