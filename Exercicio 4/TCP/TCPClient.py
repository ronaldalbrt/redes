from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))

for i in range(1, N+1):
    clientSocket.send(i.to_bytes(4, 'little', signed=False))

clientSocket.close()



