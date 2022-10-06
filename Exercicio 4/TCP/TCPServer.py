from socket import *
import time

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    while True:
        message = connectionSocket.recv(4)
        if not message:
            break 

        modifiedMessage = int.from_bytes(message, 'little', signed=False)
        print(modifiedMessage)
        
    connectionSocket.close()

