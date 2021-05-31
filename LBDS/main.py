import socket
import random
from time import sleep

connectedSockets = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()),2020))
print(socket.gethostname())
sock.listen(1)

def handleLRC(LRCSocket, address) -> None:
    connectedSockets[LRCSocket] = address
    while True:
        sleep(0.1)

        BPM = randomBPM()
        Temp = randomTemp()
        SPO = randomSPO()
        RespRate = randomRespRate()

        StringToSend = f"{BPM},{Temp},{SPO},{RespRate}"
        StringLength = len(StringToSend)

        LRCSocket.send(bytes(f"{StringLength}", "utf-8")) #send the buffer size
        LRCSocket.send(bytes(f"{StringToSend}","utf-8")) 
        print(f"{StringToSend}:sent")

def randomBPM() -> int:
    return str(random.randint(90,100))

def randomTemp() -> float:
    return random.uniform(35,37)

def randomSPO() -> int:
    return random.randint(80,100)

def randomRespRate() -> int:
    return random.randint(12,20)

while True:
    LRCSocket, address = sock.accept()
    print(f"connection from {address}")
    handleLRC(LRCSocket,address)
