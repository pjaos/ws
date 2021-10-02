#!/usr/bin/env python3.9

import socketserver
import http.server
import logging
import cgi
import cgitb

from   optparse import OptionParser
from   os import chdir
from   getpass import getuser
from   p3lib.boot_manager import BootManager
from   p3lib.uio import UIO

uio = None

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
        uio.info("Shutdown web server.")

def enableAutoStart(user, port, root):
    """@brief Enable this program to auto start when the computer on which it is installed starts.
       @param user The username which which you wish to execute on autostart.
       @param port The TCP port number to run the web server on.
       @param root The root folder of the web server."""
    bootManager = BootManager()
    if user:
        argString = "--port {} --root {}".format(port, root)
        bootManager.add(user=user, argString=argString, enableSyslog=True)
    else:
        raise Exception("--user not set.")

def disableAutoStart():
    """@brief Enable this program to auto start when the computer on which it is installed starts."""
    bootManager = BootManager()
    bootManager.remove()

def checkAutoStartStatus(uio):
    """@brief Check the status of a process previously set to auto start."""
    bootManager = BootManager()
    lines = bootManager.getStatus()
    if lines and len(lines) > 0:
        for line in lines:
            uio.info(line)

def main():
    global uio
    uio = UIO()

    opts=OptionParser(usage='Simple web server.')
    opts.add_option("--port", help="Followed by the web server port (default=8080)", type="int", default=8080)
    opts.add_option("--root", help="Followed by the web server root path", default=".")
    opts.add_option("--cgi",  help="A folder (in the root path) containing the cgi scripts (default=/cgi-bin).", default="/cgi-bin")
    opts.add_option("--enable_auto_start",  help="Auto start when this computer starts.", action="store_true", default=False)
    opts.add_option("--user",               help="The user name when the --enable_auto_start argument is used (default={}).".format(getuser()), default=getuser())
    opts.add_option("--disable_auto_start", help="Disable auto starting when this computer starts.", action="store_true", default=False)
    opts.add_option("--check_auto_start",   help="Check the status of an auto started ogsolar instance.", action="store_true", default=False)

    server = None
    try:
        (options, args) = opts.parse_args()

        if options.enable_auto_start:
            enableAutoStart(options.user, options.port, options.root)

        elif options.disable_auto_start:
            disableAutoStart()

        elif options.check_auto_start:
            checkAutoStartStatus(uio)

        else:
            chdir(options.root)

            cgitb.enable()

            Handler = ServerHandler

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
