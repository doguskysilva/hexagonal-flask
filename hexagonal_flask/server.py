import os
from flask import Flask
from flask import jsonify
import hexagonal_flask.controllers.leagues as controllers_leagues

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='douglas')

    if test_config:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
        return jsonify(controllers_leagues.english_leagues())

    return app