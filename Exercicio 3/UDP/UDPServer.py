from socket import *
import os, threading

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", SERVER_PORT))

def runServer():     
    print("Thread "+str(threading.current_thread().name)+":\n"+"The server is ready to receive\n")
    
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

n_cpus = os.cpu_count()
for i in range(n_cpus):
    t = threading.Thread(name=str(i),target=runServer)
    t.start()
