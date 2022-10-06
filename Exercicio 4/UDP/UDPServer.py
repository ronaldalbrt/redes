from socket import *

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", SERVER_PORT))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(4)
    modifiedMessage = int.from_bytes(message, 'little', signed=False)
    print(modifiedMessage)