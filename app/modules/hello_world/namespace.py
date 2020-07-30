from flask_restx import Resource
## Import Resource
from .resource import hello_get

def helloworld_namespace(api):
  helloworld_namespace = api.namespace('hello_world')

  @helloworld_namespace.route('/')
  class HelloWorld(Resource):

    def get(self):
      return hello_get(self)

  return helloworld_namespace