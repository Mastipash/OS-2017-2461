from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

ROOT="/home/eugeneai/ex-web-server"
STATIC=ROOT+"/templates/jovaphile"

def hello_world(request):
    return {"text":'Hello World!'}

if __name__ == '__main__':
    with Configurator() as config:
        config.include("pyramid_debugtoolbar")
        config.include("pyramid_chameleon")
        config.add_route('root', '/')
        config.add_view(hello_world, route_name='root', renderer=ROOT+"/templates/page.pt")
        for addr in ["pages","layout","images"]:
            path=STATIC+"/"+addr
            print(addr, path)
            config.add_static_view(name=addr, path=STATIC+"/"+addr)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
