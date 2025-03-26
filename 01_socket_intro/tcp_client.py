import socket

# create client side ip4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a server located at a given ip & port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
