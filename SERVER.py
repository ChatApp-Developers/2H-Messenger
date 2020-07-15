import socket
import threading

class SERVER:
    client_list = []
    last_received_message = ""


    def __init__(self):                     # to initialize server socket as none and create it
        self.server_socket = None
        self.create_server()


    def create_server():                    # to be able to create server at every system
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_ip = '127.0.0.1'
        local_port = 10319
        self.server_socket.bind((local_ip, local_port))
        self.server_socket,listen()


    def receive_messages():                 # to indicate receiving settings

    
    def broadcast_all():                    # to broadcast the receive buffer size info if the client is not sender


    def receive_message_new_thread():       # to make a thread for a client if it's accepted


    def add_to_clients():                   # to add a client to the client list