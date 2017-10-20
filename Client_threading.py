import threading
class Client_recv(threading.Thread):
    def __init__(self, client_sock_):
        threading.Thread.__init__(self)
        self.client_sock = client_sock_

    def run(self):
        while True:
            var = self.client_sock.recv(1024).decode()
            print(var)

class Client_send(threading.Thread):
    def __init__(self, client_sock_):
        threading.Thread.__init__(self)
        self.client_sock = client_sock_

    def run(self):
        while True:
            var = input()
            self.client_sock.send(var.encode())
            if var == "/quit":
                self.client_sock.close()
                return