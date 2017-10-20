import socket
from Server_threading import Server_recv, Server_send

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(('127.0.0.1', 9999))
server_sock.listen()

list_of_sockets = []
while True:
    client_sock, addr = server_sock.accept()
    list_of_sockets.append(client_sock)

    server_recieve_object = Server_recv(client_sock, list_of_sockets)
    server_recieve_object.start()

    server_send_object = Server_send(client_sock, list_of_sockets)
    server_send_object.start()