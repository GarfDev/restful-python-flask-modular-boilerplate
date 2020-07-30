from flask_restx import Resource
## Import Resource

def helloworld_namespace(api):
  helloworld_namespace = api.namespace('hello_world')

  @helloworld_namespace.route('/')
  class HelloWorld(Resource):

    def get(self):
      return {'json': 'Hello world'}

  return helloworld_namespace