from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))

load_dotenv(path.join(BASE_DIR, '.env'))

# Statement for enabling the development environment
TESTING = False
DEBUG = environ.get("DEBUG", False)
FLASK_ENV = environ.get("FLASK_ENV", "development")
SECRET_KEY = environ.get("SECRET_KEY", "douglas")
API_FOOTBALL_LEAGUES = environ.get("API_FOOTBALL_LEAGUES", "api_football_leagues")