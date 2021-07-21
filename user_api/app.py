from flask import Flask

from user_api import views
from user_api import config



def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Development)

    views.init_app(app)

    return app

if __name__ == '__main__':
    app_api = create_app()
    app_api.run(debug=True)