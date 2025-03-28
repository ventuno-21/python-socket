import socket


# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Your ip address
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))  # ip of given hostname

# Bind our new socket to a tuple (Ip address & port address)
server_socket.bind((HOST_IP, HOST_PORT_NO))


# put socket in listening mode
server_socket.listen()


# Accept any incoming connection and inform them
print("Server is running & listening .... \n")

# accepet any single connection & store two pieces of info
client_socket, client_address = server_socket.accept()
print(f"client_socket type = {type(client_socket)}")
print(f"client_address type = {type(client_address)}")
print(f"client_socket = {client_socket}")
print(f"client_address = {client_address}")

client_socket.send("server: You are connected ...\n".encode(ENCODER))


# send/recieve messages
while True:
    # receive infor from client
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

    # quite if client socket wants to quit, otherwise show messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\n server: ending the chat .. bye")
        break
    else:
        print(f"\n {message}")
        message = input("server message: ")
        client_socket.send(message.encode(ENCODER))


server_socket.close()
