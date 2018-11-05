#!/bin/python

import SimpleHTTPServer
import SocketServer
import os
import sys

PORT = int(sys.argv[1])

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
httpd.serve_forever()

http_response = """\
HTTP/1.1 200 OK
"""

client_connection.sendall(http_response)
client_connection.close()
