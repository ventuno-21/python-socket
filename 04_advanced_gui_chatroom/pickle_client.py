import pickle, socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect our socket to a tuple (Ip address & port address)
client_socket.connect((DEST_IP, DEST_PORT_NO))

# receive the pickled list form the server
pickled_list = client_socket.recv(BYTE_SIZE)
print(f"pickeled list = {pickled_list} , type = {type(pickled_list)}")


# You can decode a llst items only string format can be decoded by decode() method
# with pickle.loads() we can convert encoded list(which is in byte) to normal list
unpickled_list = pickle.loads(pickled_list)
print(f"unpickeled list = {unpickled_list} , type = {type(unpickled_list)}")
