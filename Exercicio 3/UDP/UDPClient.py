from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Input lowercase sentence:\n')
    
    clientSocket.sendto(message.encode(),(SERVER_NAME, SERVER_PORT))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    print(modifiedMessage.decode())

    end_conn = input("Do you wish to end the connection? [y/n]\n")
    if end_conn.lower() == 'y':
        break

clientSocket.close()