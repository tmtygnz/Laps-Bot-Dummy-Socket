import socket
import random

connected = False
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("",2020))
print(socket.gethostname())
sock.listen(1)

def handleLRC(LRCSocket, address):
    while True:
        LRCSocket.send(bytes(f"{randomBPM}","utf-8"))

def randomBPM() -> int:
    return random.randint(90,100)

while True:
    LRCSocket, address = sock.accept()
    print(f"connection from {address}")
    handleLRC(LRCSocket,address)