from multiprocessing.dummy import Pool as ThreadPool

class ThreadPoolMixIn():
	pool = ThreadPool(10)

	def process_request_func(self, request, client_address):
		#print("start_inner")
		try:
			self.finish_request(request, client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request, client_address)
			self.shutdown_request(request)

	def process_request(self, request, client_address):
		self.pool.apply_async(self.process_request_func, (request, client_address))
