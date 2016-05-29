import sys

if len(sys.argv) < 2:
	print("error")
	exit()

mode = sys.argv[1]

from http.server import HTTPServer
from socketserver import ThreadingMixIn, ForkingMixIn
from MyHandler import handler
from mixins import AsyncioMixIn, ThreadPoolMixIn, ProcessPoolMixIn, ProcessPoolServer

dict = {"asyncio": AsyncioMixIn, "thread":ThreadingMixIn, "process":ForkingMixIn, "threadpool":ThreadPoolMixIn, "processpool":ProcessPoolServer}

class AsyncioServer(AsyncioMixIn, HTTPServer):
	pass
#	def __init__(self, a, b, c=True):
#		AsyncioMixIn.__init__(self)
#		HTTPServer.__init__(self, a, b, c)

class ThreadingServer(ThreadingMixIn, HTTPServer):
	pass

class ThreadPoolServer(ThreadPoolMixIn, HTTPServer):
	pass

class ProcessPoolServer(ProcessPoolMixIn, HTTPServer):
	pass

class MyServer(dict.get(mode), HTTPServer):
	pass

def main():
	httpd = MyServer(('', 8080), handler)
	print("starting")
	httpd.serve_forever()

if __name__ == '__main__':
	main()
