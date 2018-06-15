# -*- coding:utf-8 -*-

from bottle import route, run
import os


@route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return static_file(filepath, root=STATIC_ROOT)

    # Starts a local test server.
    run(server='wsgiref', host=HOST, port=PORT)

#run(host='localhost', port=8080, debug=True)