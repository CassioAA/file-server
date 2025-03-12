import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = 'localhost'
port = 8080
address = (host, port)
sock.bind(address)

backlog = 1
sock.listen(backlog)
print('the server is listening to clients')

conn, addr = sock.accept()
print("connection established with", str(addr))

buffer_size = 1024
file_name = conn.recv(buffer_size)
try:
    file_bytes_reader = open(file_name, 'rb')
    file_content_bytes = file_bytes_reader.read()
    conn.send(file_content_bytes)
    file_bytes_reader.close()
except:
    querying_error_bytes = bytes('File not found here on the server', 'utf-8')
    conn.send(querying_error_bytes)

conn.close()