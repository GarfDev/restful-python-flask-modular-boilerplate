from flask import Flask

def initialize_app(config_type):
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_pyfile(f'config/{config_type}.py',)
  
  with app.app_context():
    return app