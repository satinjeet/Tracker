import Tracker
from BaseHTTPServer import HTTPServer

port = 8080
ip =  'localhost'
try:
    server = HTTPServer(('', port), Tracker.HTTPRequestHandler)
    print 'Started httpserver on port ' , port
   
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
   print '^C received, shutting down the web server'
   server.socket.close()