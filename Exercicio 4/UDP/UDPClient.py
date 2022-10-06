from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000
N = 80

clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1,N+1):
    clientSocket.sendto(i.to_bytes(4, 'little', signed=False),(SERVER_NAME, SERVER_PORT))

clientSocket.close()