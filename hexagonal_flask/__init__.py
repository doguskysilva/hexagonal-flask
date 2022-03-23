import os

from flask import Flask

from hexagonal_flask.diplomat.http_server import server


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(server)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.from_mapping(test_config)

    print(app.config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
