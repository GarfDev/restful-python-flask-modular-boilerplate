from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

def initialize_app(config_type):
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object(f'app.config.{config_type}.Config')
  ## Initialize ORM
  db = SQLAlchemy(app)
  ## Initialize RESTful
  api = Api(app)
  
  with app.app_context():
    ## Modules contexts
    from .modules.hello_world.resource import helloworld_namespace

    api.add_namespace(helloworld_namespace(api))

    return app