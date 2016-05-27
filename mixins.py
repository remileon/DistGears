import asyncio
import threading
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool
from multiprocessing import Queue, sharedctypes, Pipe
import pickle

class BaseMixIn:
	def process_request_func(self, request, client_address):
		print("start_inner")
		try:
			self.finish_request(request, client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request, client_address)
			self.shutdown_request(request)

	@asyncio.coroutine
	def process_request_func_coroutine(self, request, client_address):
		try:
			self.finish_request(request, client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request, client_address)
			self.shutdown_request(request)

class AsyncioMixIn(BaseMixIn):
	loop = asyncio.get_event_loop()
	
	def process_request(self, request, client_address):
		self.loop.run_until_complete(self.process_request_func_coroutine(request, client_address))

class ThreadPoolMixIn(BaseMixIn):
	pool = ThreadPool(10)

	def process_request(self, request, client_address):
		self.pool.apply_async(self.process_request_func, (request, client_address))

def process_request_func_queue(self, request, client_address):
	print("start inner")
	print("get self")
	try:
		self.finish_request(request, client_address)
		self.shutdown_request(request)
	except Exception as e:
		print(e)
	print("finish")

class ProcessPoolMixIn(BaseMixIn):
	pool = ProcessPool(10)
	
	def __getstate__(self):
		return (self.server_address, self.RequestHandlerClass)

	def __setstate__(self, state):
		HTTPServer.__init__(self, state[0], state[1])
	
	def process_request(self, request, client_address):
		print("start_processing")
		self.pool.apply_async(process_request_func_queue, (self, request, client_address))
