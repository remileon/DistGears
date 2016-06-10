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

global_queue = asyncio.Queue()

class AsyncioMixIn(BaseMixIn):
	loop = asyncio.get_event_loop()
	
	def __init__(self, a, b):
		self.loop.create_task(self.process_request_func_coroutine())
		#threading.Thread(target = self.loop.run_forever, args = ()).start()
		#self.loop.run_forever()
		HTTPServer.__init__(self, a, b)

	@asyncio.coroutine
	def process_request_func_coroutine(self):
		print("asd")
		while True:
			print("dsa")
			(request, client_address) = yield from global_queue.get()
			self.process_request_func(request, client_address)

	def process_request(self, request, client_address):
		print("qqq")
		print(self.loop.is_running())
		global_queue.put_nowait((request, client_address))
		if not self.loop.is_running():
			threading.Thread(target = self.loop.run_forever, args = ()).start()

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
