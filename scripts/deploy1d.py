#!/usr/bin/env python

from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import os
import sys
import time
import daemon
from multiprocessing import Process
import logging

import logging
log = logging.getLogger ( "auto1" )
log.addHandler ( logging.FileHandler ( "/var/log/auto1.log" ) )
log.setLevel ( logging.INFO )


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''
    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())
		 
    def isatty ( self ) :
        return False	
	
    def flush ( self ): 
        for handler in self.logger.handlers:
            handler.flush ()

"""
logging.basicConfig(
   level=logging.DEBUG,
   format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   filename="out.log",
   filemode='a'
)
"""
 
stdout_logger = logging.getLogger('STDOUT')
stdout_logger.addHandler ( logging.FileHandler ( "/var/log/auto1.log" ) )
sl = StreamToLogger(stdout_logger, logging.INFO)
sys.stdout = sl
 
stderr_logger = logging.getLogger('STDERR')
stderr_logger.addHandler ( logging.FileHandler ( "/var/log/auto1.log" ) )
sl = StreamToLogger(stderr_logger, logging.ERROR)
sys.stderr = sl

def fork ( ):
  if os.fork ( ):
    os._exit ( 0 );

  os.chdir ( "/" )
  os.setsid ( )
  os.umask ( 0 )

  if os.fork ( ):
    os._exit ( 0 )
  #os.dup2 ( file ( os.devnull, "r" ).fileno ( ), sys.stdin.fileno ( ) )
  #os.dup2 ( file ( os.devnull, "a+" ).fileno ( ), sys.stdout.fileno ( ) )
  #os.dup2 ( file ( os.devnull, "a+", 0 ).fileno ( ), sys.stderr.fileno ( ) )

def deploy ( ):
  os.setuid ( 1000 )
  out = ""
  stdin, stdout, stderr = os.popen3 ( "cd /var/bukaopu/; pwd; git pull origin master" )
  out += stderr.read ( ) + stdout.read ( )
  stdin, stdout, stderr = os.popen3 ( "supervisorctl -s http://127.0.0.1:9001 restart gunicorn" )
  out += stderr.read ( ) + stdout.read ( )


def restart ( ):
  p = Process ( target = deploy )
  p.start ( )
  stdout_logger.info ( "restart" )
  return "Ok"
 

def echo ( s ):
  return s


def main ( ):
  server = SimpleXMLRPCServer ( ( '', 9002 ), SimpleXMLRPCRequestHandler, False )
  server.register_function ( restart, "restart" )
  server.register_function ( echo,    "echo"    )
  server.serve_forever()
  
if "__main__" == __name__:
  fork ()
  main ( )
