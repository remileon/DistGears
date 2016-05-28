import http.client
import time
import threading

n = 2000
n_thread = 8 
_sum = 0
def test_thread():
	global _sum
	httpClient = http.client.HTTPConnection('localhost', 8080)
	for i in range(n):
		for j in range(72):
			httpClient.request('GET', '')
			response = httpClient.getresponse()
		_sum += 72

thread = [1] * 10
for i in range(n_thread):
	thread[i] = threading.Thread(target = test_thread, args = ())

#before = time.time()
for i in range(n_thread):
	thread[i].start()
#for i in range(n_thread):
#	thread[i].join()
#after = time.time()

time.sleep(5)
print(_sum / 5)
