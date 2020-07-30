from dotenv import load_dotenv
from os import getenv

load_dotenv()
class Config(object):
    SECRET_KEY = 'do-i-really-need-this-yeah-you-do'
    FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' if getenv('DATABASE_URL') == None else getenv('DATABASE_URL')
