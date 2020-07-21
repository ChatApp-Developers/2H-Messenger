import socket
import threading


PORT = 5050
IP = socket.gethostbyname(socket.gethostname()) #gets the ip address by host name
#or: IP = '127.0.0.1' which is the standard loopback interface address
ADDR = (IP, PORT)


class ChatServer:
    clients_list = []

    last_received_message = ""

    def __init__(self):                                 # to initialize server socket as none and create it
        self.server_socket = None
        self.create_listening_server()

    def create_listening_server(self):                  # to be able to create server at every system
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = socket.gethostbyname(socket.gethostname())
        PORT = 5050    
        # to allow to immediately restart the TCP server :
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # to make the server listen to requests coming from other computers on the network :
        self.server_socket.bind(ADDR)
        print("Listening for incoming messages..")
        self.server_socket.listen(5)
        self.receive_messages_in_a_new_thread()

    def receive_messages(self, so):                     # to indicate receiving settings
        while True:
            incoming_buffer = so.recv(256)
            if not incoming_buffer:
                break
            self.last_received_message = incoming_buffer.decode('utf-8')
            self.broadcast_to_all_clients(so)           # to send to all clients
        so.close()

    def broadcast_to_all_clients(self, senders_socket): # to broadcast the receive buffer size info if the client is not sender
        for client in self.clients_list:
            socket, (IP, PORT) = client
            if socket is not senders_socket:
                socket.sendall(self.last_received_message.encode('utf-8'))

    def receive_messages_in_a_new_thread(self):         # to make a thread for a client if it's accepted
        while True:
            client = so, (ip, port) = self.server_socket.accept()
            self.add_to_clients_list(client)
            print('Connected to ', ip, ':', str(port))
            t = threading.Thread(target=self.receive_messages, args=(so,))
            t.start()

    def add_to_clients_list(self, client):              # to add a client to the client list
        if client not in self.clients_list:
            self.clients_list.append(client)


if __name__ == "__main__":
    ChatServer()