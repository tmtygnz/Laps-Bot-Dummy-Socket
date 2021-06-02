import socket
import random
from time import sleep

connectedSockets = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()),2020))

sock.listen(1)

def HandleLRC(LRCConnection, LRCAddress):
    while True:
        sleep(0.1)
        vitals = f"{dummyTemp()},{dummyRespRate()},{dummySpo()},{dummyBPM()}"
        bufferLen = len(vitals)
        LRCConnection.send(bytes(f"{bufferLen}","utf-8"))
        LRCConnection.send(bytes(f"{vitals}","utf-8"))

def dummyTemp():
    return random.randint(35,37)

def dummyRespRate():
    return random.randint(12,16)

def dummySpo():
    return random.randint(90,100)

def dummyBPM():
    return random.randint(90,100)

def Start():
    while True:
        socket, address = sock.accept()
        print(f"connection from {address}")
        HandleLRC(socket, address)

Start()
