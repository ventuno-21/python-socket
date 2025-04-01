import pickle, socket

unpickled_list = ["dill", "bread and butter", "hlaf sour"]
print(f"{unpickled_list} and type is = {type(unpickled_list)}")

# Try to encode a list using .encode()
# trial_list = unpickled_list.encode("utf-8")
## You can't encode it a 'list', becasue 'list' has no attribute encode,& encode is get use for 'string'
# print(f"{trial_list} and type is = {type(trial_list)}")


# Threfore lets encode it with pickling
# as the result come back , pickle will return 'byte' object, wich is we can use in SOCKET
pickled_list = pickle.dumps(unpickled_list)
print(f"{pickled_list} and type is = {type(pickled_list)}")


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

# Listen forever to accept any connection
while True:
    # accept any inoming cline connection
    client_socket, client_address = server_socket.accept()
    # print(f"client_socket type = {type(client_socket)}")
    # print(f"client_address type = {type(client_address)}")
    print(f"client_socket = {client_socket}")
    print(f"client_address = {client_address}")

    # send the encoded pickled list, which is already encoded so we dont encode it anymore
    client_socket.send(pickled_list)
    # client_socket.send("NAME".encode(ENCODER))

    # close the socket
    server_socket.close()
