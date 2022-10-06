from socket import *
import pickle

SERVER_NAME = "localhost"
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))

user = input("User: ")
password = input("Password: ") 

payload = {
    "user": user,
    "password": password
}

clientSocket.send(pickle.dumps(payload))

serverResponse = clientSocket.recv(2048)

print(serverResponse.decode())

clientSocket.close()