from flask import Blueprint, jsonify

import hexagonal_flask.controllers.leagues as controllers_leagues

server = Blueprint("server", __name__)


@server.route("/")
def hello():
    return jsonify(controllers_leagues.english_leagues())
