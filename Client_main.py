import socket
from Client_threading import Client_send, Client_recv

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('127.0.0.1', 9999))

client_send_object = Client_send(client_sock)
client_send_object.start()

client_recv_object = Client_recv(client_sock)
client_recv_object.start()