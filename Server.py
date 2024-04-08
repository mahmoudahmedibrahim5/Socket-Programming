import socket
import threading

def handle_client(conn, addr):
    print("New Connection")
    connected = True
    while connected:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"{addr} {msg}")
        
        if msg == DISCONNECT_MESSAGE:
            connected = False
    conn.close()

def start():
    print("Server is starting")
    server.listen()
    print(f"Server is listenning on {IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"New thread is started, now there is {threading.activeCount() - 1} active")



if __name__ == "__main__":
    HEADER = 64
    PORT = 5050
    IP = socket.gethostbyname(socket.gethostname())
    ADDR = (IP, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "Disconnect"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    
    start()    
    