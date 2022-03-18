from flask import Flask
import hexagonal_flask.controllers.leagues as controllers_leagues
from flask import jsonify

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
def home():
    return jsonify(controllers_leagues.english_leagues())