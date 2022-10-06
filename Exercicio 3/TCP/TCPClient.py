from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))
while True:
    message = input('Input lowercase sentence:\n')
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    if modifiedMessage.decode() is None:
        print("Connection closed by the server")
        break
    print(modifiedMessage.decode())

    end_conn = input("Do you wish to end the connection? [y/n]\n")
    if end_conn.lower() == 'y':
        break
    
clientSocket.close()