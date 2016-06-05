from http.server import HTTPServer,BaseHTTPRequestHandler  
import io,shutil 
import asyncio
import threading

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		r_str="Hello World"  
		enc="UTF-8"  
		encoded = ''.join(r_str).encode(enc)  
		f = io.BytesIO()  
		f.write(encoded)  
		f.seek(0)
		self.send_response_only(200)
		self.send_header("Content-type", "text/html; charset=%s" % enc)
		self.send_header("Content-Length", str(len(encoded)))  
		self.end_headers() 
		shutil.copyfileobj(f,self.wfile)
