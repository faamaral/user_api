from flask import Flask

from user_api import views
from user_api import config



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    views.init_app(app)

    return app

