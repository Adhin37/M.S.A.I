# -*- coding: utf-8 -*-
"""
This script runs the application using a development server.
"""
import os
import sys
import socket
# routes contains the HTTP handlers for our server and must be imported.
import routes
import bottle


if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)


def check_server_port(serv_address, serv_port):
    """Return if a port is used or not"""
    # Create a TCP socket
    sock = socket.socket()
    print("Attempting to connect to %s on port %s" % (serv_address, serv_port))
    try:
        sock.bind((serv_address, serv_port))
        if serv_port == sock.getsockname()[1]:
            print("The port %s for the address %s is not in use" %
                  (serv_port, serv_address))
            return True
        else:
            print("The port %s for the address %s is already in use" %
                  (serv_port, serv_address))
            return False
    except socket.error as error:
        print("Connection to %s on port %s failed: %s" %
              (serv_address, serv_port, error))
        return False
    finally:
        sock.close()


def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()


if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    # port de lancement du serveur
    ADDRESS = '127.0.0.1'
    PORT = 1854

    PORT_NOT_USED = check_server_port(ADDRESS, PORT)
    if PORT_NOT_USED is True:
        @bottle.route('/static/<filepath:path>')
        def server_static(filepath):
            """Handler for static files, used with the development server.
            When running under a production server such as IIS or Apache,
            the server should be configured to serve the static files."""
            return bottle.static_file(filepath, root=STATIC_ROOT)

        # Starts a local test server.
        bottle.run(reloader=True, server='wsgiref', host=HOST, port=PORT)
