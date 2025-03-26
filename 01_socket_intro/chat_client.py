import socket


# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((DEST_IP, DEST_PORT_NO))
