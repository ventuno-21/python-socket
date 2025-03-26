import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Your ip address
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))  # ip of given hostname

# Bind our new socket to a tuple (Ip address & port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


# pu socket in listening mode
server_socket.listen()
