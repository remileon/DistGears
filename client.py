import sys
import http.client
import time
import threading

serveraddr = 'localhost'
if len(sys.argv) >= 2:
	serveraddr = sys.argv[1]

# numbers of test threeads at the same time
n_thread = 5 
# counter for total request numbers dealed
_sum = 0

# inner function of one thread
# loop:
# 	send require, receive respond
def test_thread():
	global _sum
	httpClient = http.client.HTTPConnection(serveraddr, 8080)
	while True:
		httpClient.request('GET', '')
		response = httpClient.getresponse()
		_sum += 1

# construct threads
thread = [1] * n_thread
for i in range(n_thread):
	thread[i] = threading.Thread(target = test_thread, args = ())

# start threads
for i in range(n_thread):
	thread[i].start()

# wait for some time and get the counter
time.sleep(5)
print(_sum / 5)
