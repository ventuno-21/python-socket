import json, socket

# unpickled_list = ["dill", "bread and butter", "hlaf sour"]
# print(f"{unpickled_list} and type is = {type(unpickled_list)}")

# Try to encode a list using .encode()
# trial_list = unpickled_list.encode("utf-8")
## You can't encode it a 'list', becasue 'list' has no attribute encode,& encode is get use for 'string'
# print(f"{trial_list} and type is = {type(trial_list)}")


# # Threfore lets encode it with pickling
# # as the result come back , pickle will return 'byte' object, wich is we can use in SOCKET
# pickled_list = pickle.dumps(unpickled_list)
# print(f"{pickled_list} and type is = {type(pickled_list)}")


# Create a dictionary with what info that we want
message_info = {
    "flag": "message",
    "name": "ventuno",
    "message": "hello to vent1",
    "color": "#00ff5f",
}


print(f"message_info dict include = {message_info}, type = {type(message_info)}")

# # YOu can't encode dictionary with encode() method
# # Below code will face an error => AttributeError: 'dict' object has no attribute 'encode'
# print(message_info.encode("utf-8"))

# Turn a dict into a string using json
message_json = json.dumps(message_info)
print(f"message_json dict include = {message_json}, type = {type(message_json)}")

# Now we encode the stirng representation of our dictionary
print(
    f"message_json dict include with encoding = {message_json.encode}, type = {type(message_json.encode())}"
)


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

    # send the json object whichh is just 'string' and we have to encode it
    client_socket.send(message_json.encode(ENCODER))
    # client_socket.send("NAME".encode(ENCODER))

    # close the socket
    server_socket.close()
