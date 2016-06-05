import asyncio
import threading
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
from multiprocessing import Queue, sharedctypes, Pipe
from http.server import HTTPServer

class BaseMixIn:
	def process_request_func(self, request, client_address):
		#print("start_inner")
		try:
			self.finish_request(request, client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request, client_address)
			self.shutdown_request(request)

	@asyncio.coroutine
	def process_request_func_coroutine(self, request, client_address):
		self.process_request_func(request, client_address)

class AsyncioMixIn(BaseMixIn):
	loop = asyncio.get_event_loop()
	
	def process_request(self, request, client_address):
		self.loop.run_until_complete(self.process_request_func_coroutine(request, client_address))

class ThreadPoolMixIn(BaseMixIn):
	pool = ThreadPool(10)

	def process_request(self, request, client_address):
		self.pool.apply_async(self.process_request_func, (request, client_address))

def init(HandlerClass):
	global httpServer
	httpServer = HTTPServer(('', 0), HandlerClass)

def do_request(request, client_address):
	global httpServer
	try:
		httpServer.finish_request(request, client_address)
		httpServer.shutdown_request(request)
	except Exception as e:
		print(e)
	
class ProcessPoolMixIn(BaseMixIn):
	def __init__(self, address, HandlerClass):
		self.pool = ProcessPool(10, init, (HandlerClass,))
		HTTPServer.__init__(self, address, HandlerClass)

	def process_request(self, request, client_address):
		self.pool.apply_async(do_request, (request, client_address))
