from socket import *

serverPort = 12000
serverName = "127.0.0.1"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    connectionSocket.close()
    if sentence == "exit":
        break
    