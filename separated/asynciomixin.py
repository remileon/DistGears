import asyncio

class AsyncioMixIn():
	loop = asyncio.get_event_loop()

	@asyncio.coroutine
	def process_request_func_coroutine(self, request, client_address):
		#print("start_inner")
		try:
			self.finish_request(request, client_address)
			self.shutdown_request(request)
		except:
			self.handle_error(request, client_address)
			self.shutdown_request(request)

	# method that overrides BaseServer in socketserver
	def process_request(self, request, client_address):
		self.loop.run_until_complete(self.process_request_func_coroutine(request, client_address))
