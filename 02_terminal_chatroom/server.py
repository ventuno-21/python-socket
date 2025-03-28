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


def broadcat_message(message):
    """Sending a message to all clients that are connected to the server"""
    pass


def recive_message(client_socket):
    """Receiving an incoming message from a specific client & forward the message to be broadcast"""
    pass


def connect_client()
    '''Connecting an incoming client to the server'''
    pass
