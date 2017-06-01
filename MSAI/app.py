# -*- coding: utf-8 -*-
"""
This script runs the application using a development server.
"""

import bottle
import os
import sys

# routes contains the HTTP handlers for our server and must be imported.
import routes
import socket;

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)

def check_server_port(ADRESS, PORT):
    # Create a TCP socket
    sock = socket.socket()
    print "Attempting to connect to %s on port %s" % (ADRESS, PORT)
    try:
        sock.bind((ADRESS, PORT))
        if PORT == sock.getsockname()[1]:
            print "The PORT %s for the address %s is not in use" % (PORT,ADRESS)
            return True
        else:
            print "The PORT %s for the address %s is already in use" % (PORT,ADRESS)
            return False
    except socket.error, e:
        print "Connection to %s on port %s failed: %s" % (ADRESS, PORT, e)
        return False
    finally:
        sock.close()

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()

if __name__ == '__main__':
    port_not_used = False
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    # PORT de lancement du serveur
    ADRESS = '127.0.0.1'
    PORT = 1854

    port_not_used = check_server_port(ADRESS,PORT)
    if port_not_used == True:
        @bottle.route('/static/<filepath:path>')
        def server_static(filepath):
            """Handler for static files, used with the development server.
            When running under a production server such as IIS or Apache,
            the server should be configured to serve the static files."""
            return bottle.static_file(filepath, root=STATIC_ROOT)

        # Starts a local test server.
        bottle.run(reloader = True, server = 'wsgiref', host = HOST, port = PORT)
