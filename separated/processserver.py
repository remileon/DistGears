import sys



from http.server import HTTPServer
from socketserver import ForkingMixIn
from MyHandler import handler

class MyServer(ForkingMixIn, HTTPServer):
	pass

def main():
	httpd = MyServer(('', 8080), handler)
	print("starting")
	httpd.serve_forever()

if __name__ == '__main__':
	main()
