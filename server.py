import os
import sys
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from tornado.web import FallbackHandler, StaticFileHandler
from django.core.wsgi import get_wsgi_application

def main():
    run_env = (sys.argv[1] if len(sys.argv) == 2 else 'dev')
    port = 80 if run_env == 'prod' else 8000
    os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
    application = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(application)
    tornado_app = tornado.web.Application([
	('/static/(.*)', tornado.web.StaticFileHandler, {'path': os.getcwd() + '/static/'}),
        ('.*', tornado.web.FallbackHandler, dict(fallback=container))
    ])
    http_server = tornado.httpserver.HTTPServer(tornado_app)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
