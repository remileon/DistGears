import sys

if len(sys.argv) < 2:
	print("error")
	exit()

mode = sys.argv[1]

from http.server import HTTPServer
from socketserver import ThreadingMixIn, ForkingMixIn
from MyHandler import handler
from mixins import AsyncioMixIn, ThreadPoolMixIn, ProcessPoolMixIn

dict = {
"asyncio": AsyncioMixIn,
"thread":ThreadingMixIn,
"process":ForkingMixIn,
"threadpool":ThreadPoolMixIn,
"processpool":ProcessPoolMixIn
}

class MyServer(dict.get(mode), HTTPServer):
	pass

def main():
	httpd = MyServer(('', 8080), handler)
	print("starting")
	httpd.serve_forever()

if __name__ == '__main__':
	main()
