import socket
import threading

def send(msg):
    message = msg.encode(FORMAT)
    message_length = str(len(message)).encode(FORMAT)
    message_length += b' ' * (HEADER - len(message_length))
    client.send(message_length)
    client.send(message)
    
if __name__ == "__main__":
    HEADER = 64
    PORT = 5050
    IP = socket.gethostbyname(socket.gethostname())
    ADDR = (IP, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "Disconnect"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        msg = input("Enter Message: ")
        send(msg)
        if msg == DISCONNECT_MESSAGE:
            break
        