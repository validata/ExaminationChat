import threading

class Server_recv(threading.Thread):
    def __init__(self, client_sock_,address_, list_of_sockets_):
        threading.Thread.__init__(self)
        self.client_sock = client_sock_
        self.address = address_
        self.list_of_sockets = list_of_sockets_

    def run(self):
        while True:
            msg_from_client = self.client_sock.recv(1024).decode()

            if msg_from_client == "/quit":
                self.client_sock.close()
                self.list_of_sockets.remove(self.client_sock)
                return

            msg_from_client = self.address + ": " + msg_from_client

            print(msg_from_client)
            # for sock in self.list_of_sockets:
            #     sock.send(msg_from_client.encode())
            sender_object = ServerSender(self.list_of_sockets, msg_from_client)
            sender_object.start()


class Server_send(threading.Thread):
    def __init__(self, client_sock_, list_of_sockets_):
        threading.Thread.__init__(self)
        self.client_sock = client_sock_
        self.list_of_sockets = list_of_sockets_

    def run(self):
        while True:
            var = input()
            for sock in self.list_of_sockets:
                sock.send(var.encode())

class ServerSender(threading.Thread):

    def __init__(self, list_of_sockets, message):
        super().__init__()
        self.list_of_sockets = list_of_sockets
        self.message = message

    def run(self):
        for client in self.list_of_sockets:
            client.send(self.message.encode())
