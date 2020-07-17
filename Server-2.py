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
        print("Listening for incoming message...")
        self.server_socket,listen(5)
        self.recieve_message_in_a_new_thread()    
    
    
    def recieve_message(self,so):
        while True:
            income_buffer = so.recv(256)
            if not income_buffer:
                break
            self.last_recieved_message = income_buffer.decode('utf-8')
            self.broadcast_to_all_clients(so)

    
    def broadcast_to_all_clients(self,sender_socket):
        for client in self.client_list:
            so,(ip, port) = client
            if so is not sender_socket:
                so.sendall(self.last_recieved_message.encode('utf-8')


    def recieve_message_in_a_new_thread(self):
        While True:
            client = so, (ip,port) = self.server_socket.accept()
            self.add_to_clients(client)
            t = threading.Thread(target = self.recieve_message, args = (so,))
            t.start()


    def add_to_clients(self, client):
        if client not in self.client_list:
            self.client_list.append(client)


if __name__ = "__main__"
    ChatServer()