#!/usr/bin/env python3.9

import socketserver
import http.server
import http.server
import logging
import cgi
from   optparse import OptionParser
from   os import chdir
import cgitb; 

VERSION = 1.6

class ServerHandler(http.server.CGIHTTPRequestHandler):

    QUERY_STRING = "QUERY_STRING"
    
    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        http.server.CGIHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.warning("======= POST STARTED =======")
        logging.warning(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        logging.warning("======= POST VALUES =======")
        for item in form.list:
            logging.warning("%s=%s" % (item.name, item.value) )
        logging.warning("\n")
        http.server.CGIHTTPRequestHandler.do_POST(self)
   
def shutdown(server):
    """Shutdown the web server"""
    if server != None:
        server.socket.close()
        print(("Shutdown server on port", port))

def main():
    opts=OptionParser(usage='Simple web server.')
    opts.add_option("--port", help="Followed by the web server port (default=8080)", type="int", default=8080)
    opts.add_option("--root", help="Followed by the web server root path", default=".")
    opts.add_option("--cgi",  help="A folder (in the root path) containing the cgi scripts (default=/cgi-bin).", default="/cgi-bin")
    server = None
    port=None
    try:
        (options, args) = opts.parse_args()
        
        chdir(options.root)
        
        cgitb.enable()
        
        Handler = ServerHandler
        port    = options.port
        
        Handler.cgi_directories = [options.cgi]

        print(("serving at port", options.port))
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.ThreadingTCPServer.allow_reuse_address = True
        server = http.server.HTTPServer(("", options.port), Handler)

        server.serve_forever()

    #If the user presses CTRL C
    except KeyboardInterrupt:
        shutdown(server)

    #If the program throws a system exit exception
    except SystemExit:
        shutdown(server)
      
    except:
      raise

if __name__ == '__main__':
    main()
