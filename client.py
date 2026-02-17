import socket

HOST = '26.151.218.167'  # The server's hostname or IP address
PORT = 228        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello, world')
	data = s.recv(1024)

print(f'Received {data.decode()!r}')