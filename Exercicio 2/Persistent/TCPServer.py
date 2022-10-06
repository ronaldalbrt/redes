from socket import *
import time

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    curr_time = time.time()

    while True:
        message = connectionSocket.recv(2048)
        modifiedMessage = message.decode().upper()
        connectionSocket.send(modifiedMessage.encode())
        if time.time() - curr_time > 10:
            break
        
    connectionSocket.close()

