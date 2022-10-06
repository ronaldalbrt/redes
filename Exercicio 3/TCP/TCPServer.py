from socket import *
import threading
import time
import os

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

def runServer(): 
    print("Thread "+str(threading.current_thread().name)+":\n"+"The server is ready to receive\n")

    while True:
        connectionSocket, addr = serverSocket.accept()
        curr_time = time.time()

        while True:
            message = connectionSocket.recv(2048)
            modifiedMessage = message.decode().upper()
            connectionSocket.send(modifiedMessage.encode())
            if time.time() - curr_time > 60:
                break
            
        connectionSocket.close()

n_cpus = os.cpu_count()
for i in range(n_cpus):
    t = threading.Thread(name=str(i),target=runServer)
    t.start()


