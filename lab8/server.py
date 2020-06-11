from http.server import HTTPServer, CGIHTTPRequestHandler
import time

hostName = "localhost"
hostPort = 9000

myServer = HTTPServer((hostName, hostPort), CGIHTTPRequestHandler)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
