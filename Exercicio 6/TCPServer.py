from socket import *
import time
import pickle

SERVER_PORT = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

while True:
    state = "Boas-vindas"
    connectionSocket, addr = serverSocket.accept()

    while True:
        if state == "Boas-vindas":
            message = connectionSocket.recv(1024)

            connectionSocket.send("Olá! Bem Vindo! Qual seu nome?".encode())
            name = connectionSocket.recv(1024).decode()
            state = "Serviços"

        elif state == "Serviços": 
            connectionSocket.send(f"Certo, {name}! Como posso te ajudar?\nDigite o numero que corresponde a opcao desejada:\n1 - Agendar um horario de monitoria\n2 - Listar as proximas atividades da disciplina\n3 - E-mail do professor".encode())

            clientResponse = connectionSocket.recv(1024).decode()
            state = "Agendar Monitoria" if clientResponse == "1" else ("Atividades Pendentes" if clientResponse == "2" else  ("Email do Professor" if clientResponse == "3" else "Finalizar"))

        elif state == "Agendar Monitoria":
            connectionSocket.send("Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br\n".encode())
            state = "Finalizar"
        elif state == "Atividades Pendentes":
            connectionSocket.send("Fique atento para as datas das proximas atividades. Confira o que vem por ai!\nP1: 26 de maio de 2022\nLista 3: 29 de maio de 2022\n".encode())
            state = "Finalizar"
        elif state == "Email do Professor":
            connectionSocket.send("Quer falar com o professor?\nO e-mail é sadoc@dcc.ufrj.br\n".encode())
            state = "Finalizar"
        else:
            connectionSocket.send("Obrigado por utilizar nossos servicos!\nAte logo!".encode())
            break
    connectionSocket.close()