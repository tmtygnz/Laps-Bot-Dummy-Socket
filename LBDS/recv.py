import socket
from time import sleep

BUFFER = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostbyname(socket.gethostname()),2020))

while True:
    len = sock.recv(BUFFER).decode('utf-8')
    output = sock.recv(int(len)).decode('utf-8')
    x = output.split(",")
    print(x)
