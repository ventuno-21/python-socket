import socket

# create a client side socket ipv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some information via connectionless protocol
client_socket.sendto(
    "message form client".encode("utf-8"),
    (socket.gethostbyname(socket.gethostname()), 12345),
)
