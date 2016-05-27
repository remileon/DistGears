from http.server import HTTPServer,BaseHTTPRequestHandler  
import io,shutil 
import asyncio
import threading

class handler(BaseHTTPRequestHandler):
	def __init__(self, a, b, c):
		self.first = True
		self.loop = asyncio.get_event_loop()
		threading.Thread(target = self.loop.run_forever, args = ())
		BaseHTTPRequestHandler.__init__(self, a, b, c)
		print("construct completed")
	def do_GET(self):
		@asyncio.coroutine
		def do(self):
			r_str="Hello World"  
			enc="UTF-8"  
			encoded = ''.join(r_str).encode(enc)  
			f = io.BytesIO()  
			f.write(encoded)  
			f.seek(0)
			print(self.first)
			if self.first:
				self.first = False
				yield from asyncio.sleep(10000)
			self.send_response(200)  
			self.send_header("Content-type", "text/html; charset=%s" % enc)  
			self.send_header("Content-Length", str(len(encoded)))  
			self.end_headers() 
			shutil.copyfileobj(f,self.wfile) 
		
		self.loop.call_soon(do, self)
