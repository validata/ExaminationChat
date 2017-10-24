import threading

class Client_recv(threading.Thread):
    def __init__(self, client_sock_):
        threading.Thread.__init__(self)
        self.client_sock = client_sock_

    def run(self):
        while True:
            var = self.client_sock.recv(1024).decode()
            print(var)
    # todo kalla på en funktion i gui som skriver i chatrutan
    # todo jag tror att lättaste är att skicka med textrutan till den här klassen och göra skrivfunktion här.
    # todo måste ha en referens till egna textrutan åtminstone

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
    # todo behöver ingen "while True" loop här. Kalla på den här funktionen antingen när användare klickar på "send"
    # todo är nog lättast att göra en subfunktion i gui som kallar på den är funktionen.