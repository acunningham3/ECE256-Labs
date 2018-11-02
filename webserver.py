#!/bin/python

import SimpleHTTPServer
import SocketServer
import time
import os

from datetime import datetime
now = datetime.now()
seconds = now.second

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)



print "serving at port", PORT
httpd.serve_forever()



http_response = """\
HTTP/1.1 200 OK
"""

client_connection.sendall(http_response)
client_connection.close()
