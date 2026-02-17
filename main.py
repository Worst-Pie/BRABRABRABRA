import socket
# import pygame
# import pyscreenshot as ImageGrab
import pygetwindow as gw
from PIL import ImageGrab, Image
import win32gui

HOST = '26.151.218.167'  # Standard loopback interface address (localhost)
PORT = 228     # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)


img = ImageGrab.grab()

img.save("test.png")

img.show()