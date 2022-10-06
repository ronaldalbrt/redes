from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))
while True:
    message = input()
    clientSocket.send(message.encode())
    
    serverResponse = clientSocket.recv(2048).decode()
    
    if not serverResponse:
        print("Connection closed by the server")
        break

    print(serverResponse)
    
clientSocket.close()