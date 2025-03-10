import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = 'localhost'
port = 8080
address = (host, port)
sock.connect(address)

bufsize = 1024
response_bytes = sock.recv(bufsize)
while response_bytes:
    print(response_bytes.decode('utf-8'))
    response_bytes = sock.recv(bufsize)

sock.close()