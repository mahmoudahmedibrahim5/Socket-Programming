from socket import *

serverName = "127.0.0.1"
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input sentence: ')
    clientSocket.send(sentence.encode())
    clientSocket.close()
    if sentence == "exit":
        break
