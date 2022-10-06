from socket import *
import time
import pickle

USER = "user"
PASSWORD = "password"

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    message = connectionSocket.recv(1024)

    message = pickle.loads(message)

    if(message["user"] == USER and message["password"] == PASSWORD):
        connectionSocket.send("Successfully Logged!".encode())
    else:
        connectionSocket.send("Wrong User or Password!".encode())
    
    connectionSocket.close()

