from multiprocessing import Pool as ProcessPool
from http.server import HTTPServer

# function that each process call at first
# construct an httpServer
def init(HandlerClass):
	global httpServer
	httpServer = HTTPServer(('', 0), HandlerClass)

# function that let a process call to deal with the request
def do_request(request, client_address):
	global httpServer
	try:
		httpServer.finish_request(request, client_address)
		httpServer.shutdown_request(request)
	except Exception as e:
		print(e)
	
class ProcessPoolMixIn():
	def __init__(self, address, HandlerClass):
		self.pool = ProcessPool(10, init, (HandlerClass,))
		HTTPServer.__init__(self, address, HandlerClass)

	def process_request(self, request, client_address):
		self.pool.apply_async(do_request, (request, client_address))
