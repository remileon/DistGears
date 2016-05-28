import http.client
import time

httpClient = http.client.HTTPConnection('localhost', 8080)
before = time.time()
for i in range(1, 20):
	httpClient.request('GET', '')
	response = httpClient.getresponse()
after = time.time()
print(after - before)
