import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = 'localhost'
port = 8080
address = (host, port)
sock.bind(address)

backlog = 1
sock.listen(backlog)

print('the server is listening for a connection')

conn, addr = sock.accept()

response_message = "hi, we are connected o/"
response_bytes = bytes(response_message, 'utf-8')
conn.send(response_bytes)

conn.close()