import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = 'localhost'
port = 8080
address = (host, port)
sock.connect(address)

file_name = 'aa'
file_name_bytes = bytes(file_name, 'utf-8')
sock.send(file_name_bytes)

buffer_size = 1024
file_content_bytes = sock.recv(buffer_size)
file_content = file_content_bytes.decode('utf-8')
with open(file_name, "w", encoding="utf-8") as f:
    f.write(file_content)
print("Content of the received file:")
print(file_content)

sock.close()