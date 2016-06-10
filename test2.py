#echo.py
from socket import *
import asyncio

loop = asyncio.get_event_loop()


async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        #print("connect from ", addr)
        loop.create_task(echo_handler(client))


async def echo_handler(client):
    with client:
        data = await loop.sock_recv(client, 10000)
        await loop.sock_sendall(client, '''HTTP/1.1 200 OK\nContext-Type: text/html; charset=utf-8\nServer: Python-slp version 1.0\nContext-Length:\n\n<h1>Hello world!</h1>'''.encode('utf-8'))
    #print("connection closed")

loop.create_task(echo_server(('', 8080)))
loop.run_forever()
