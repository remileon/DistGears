import http.client
import time
import threading

n = 2000
n_thread = 5
_sum = 0
def test_thread():
	global _sum
	httpClient = http.client.HTTPConnection('localhost', 8080)
	before = time.time()
	for i in range(n):
		httpClient.request('GET', '')
		response = httpClient.getresponse()
	after = time.time()
	average = n / (after - before)
	_sum += average

thread = [1] * 10
for i in range(n_thread):
	thread[i] = threading.Thread(target = test_thread, args = ())

for i in range(n_thread):
	thread[i].start()

for i in range(n_thread):
	thread[i].join()

print(_sum/n_thread)
