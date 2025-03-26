import socket

# create a server side socket ipv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Your ip address
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))  # ip of given hostname

# Bind our new socket to a tuple (Ip address & port no)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


# we dont need to listen heere, because UDP is connectionless
# we are not accepting either

message, address = server_socket.recvfrom(1024)
message = message.decode("utf-8")
print(f"message = {message}")
print(f"address = {address}")
