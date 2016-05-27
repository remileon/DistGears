import socket  
import signal  
import errno  
from time import sleep   
  
  
def HttpResponse(header, body):
    return str.encode("%s %d\n\n%s\n\n" % (header, len(body), body))
  
def sigIntHander(signo,frame):  
    print('get signo# ',signo) 
    global runflag  
    runflag = False  
    global lisfd  
    lisfd.shutdown(socket.SHUT_RD)  
  
strHost = "45.32.8.53" 
HOST = strHost #socket.inet_pton(socket.AF_INET,strHost)  
PORT = 81 
  
httpheader = '''''\ 
HTTP/1.1 200 OK 
Context-Type: text/html 
Server: Python-slp version 1.0 
Context-Length: '''  
  
lisfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
lisfd.bind((HOST, PORT))  
lisfd.listen(2)  
  
signal.signal(signal.SIGINT,sigIntHander)  
  
runflag = True  
while runflag:  
    try:  
        confd,addr = lisfd.accept()  
    except socket.error as e:  
        if e.errno == errno.EINTR:  
            print('get a except EINTR') 
        else:  
            raise  
        continue  
  
    if runflag == False:  
        break;  
  
    print("connect by ",addr)
    data = confd.recv(1024)  
    
    print(data)  
    response = HttpResponse(httpheader, 'hello crazy')
    confd.send(response)  
    confd.close()
else:  
    print('runflag#',runflag)
  
print('Done')
