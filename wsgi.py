from os import getenv
from app import initialize_app

config_type = "development" if getenv('ENV') == None else getenv('ENV')
application = initialize_app(config_type)

if __name__ == "__main__":
  application.run(host='0.0.0.0')