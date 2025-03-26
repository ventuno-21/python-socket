import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Your ip address
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))  # ip of given hostname

# Bind our new socket to a tuple (Ip address & port address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))


# put socket in listening mode
server_socket.listen()

# Listen forever to accept any connection
while True:
    # accepet any single connection & store two pieces of info
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(type(client_address))
    print(client_socket)
    print(client_address)

    print(f"connected to client add: {client_address}")

    # send a message to connected client, we cant send string to client should be coded
    client_socket.send("You are connected".encode("utf-8"))

    # close the connection
    server_socket.close()
    break
