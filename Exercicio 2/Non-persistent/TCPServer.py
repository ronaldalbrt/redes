from socket import *

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    
    connectionSocket.close()

