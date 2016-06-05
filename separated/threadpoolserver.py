import sys

from http.server import HTTPServer
from MyHandler import handler
from threadpoolmixin import ThreadPoolMixIn

class MyServer(ThreadPoolMixIn, HTTPServer):
	pass

def main():
	httpd = MyServer(('', 8080), handler)
	print("starting")
	httpd.serve_forever()

if __name__ == '__main__':
	main()
