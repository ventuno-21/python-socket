import socket

# create client side ip4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a server located at a given ip & port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))


# Receive a  message form server side, max number of bytes should be specefied which will be received
message = client_socket.recv(10)
message = message.decode("utf-8")
print(f"client receive message : {message}")
print(type(message))

message = client_socket.recv(10)
message = message.decode("utf-8")
print(f"client receive message : {message}")
print(type(message))

# close client socket
client_socket.close()
