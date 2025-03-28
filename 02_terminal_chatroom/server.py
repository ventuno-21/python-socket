import socket
import threading


# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind our new socket to a tuple (Ip address & port address)
server_socket.bind((HOST_IP, HOST_PORT_NO))
# put socket in listening mode
server_socket.listen()


# create two blank list to store connected client sockets and their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    """Sending a message to all clients that are connected to the server"""
    for client_socket in client_socket_list:
        client_socket.send(message)


def recive_message(client_socket):
    """Receiving an incoming message from a specific client & forward the message to be broadcast"""
    while True:

        try:
            # Get the name of given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # receive messafe from the client
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m".encode(ENCODER)
            broadcast_message(message)

        except:
            # Get the name of given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Remobe the client_socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # close the client_socket connection
            client_socket.close()

            # Broadcating to othe clients that specific client has left the chatroom
            broadcast_message(
                f"\033[5;91m\t{name} has left the chat!\033[0m".encode(ENCODER)
            )
            break


def connect_client():
    """Connecting an incoming client to the server"""
    while True:
        # accept any inoming cline connection
        client_socket, client_address = server_socket.accept()
        print(f"client_socket type = {type(client_socket)}")
        print(f"client_address type = {type(client_address)}")
        print(f"client_socket = {client_socket}")
        print(f"client_address = {client_address}")

        # send a Name flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        # Add new client socket and name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Update the server, individual client and all clients
        print(f"Name of new client is: {client_name}\n")  # server
        client_socket.send(
            f"{client_name}, you have connected to the server".encode(ENCODER)
        )  # individual client
        # inform other clients that new client is joined to chatroom
        broadcast_message(f"{client_name} has joined to chatroom".encode(ENCODER))

        # Now that a new client has connected, start a thread
        recieve_thread = threading.Thread(target=recive_message, args=(client_socket,))
        recieve_thread.start()


# start the server
print(f"Server is listening for incoming connections ... \n")
connect_client()
