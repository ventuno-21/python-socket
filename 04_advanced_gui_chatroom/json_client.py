"""'
json.loads() => can convert 'bytes' & 'string' types both to dictionary
threfore the resault of below examples are the same:

example 1) 
    # receive the message form the server whch is in bytes
    messagen_json = client_socket.recv(BYTE_SIZE).decode(ENCODER)
    print(f"json_dict  = {messagen_json} , type = {type(messagen_json)}")

    # message_json is 'string' to convert it to dictionary we can use json.loads()
    message_dict = json.loads(messagen_json)
    print(f"message_dict  = {message_dict} , type = {type(message_dict)}")

example 2)
    # receive the message form the server whch is in bytes
    messagen_json = client_socket.recv(BYTE_SIZE)
    print(f"json_dict  = {messagen_json} , type = {type(messagen_json)}")

    # message_json is 'bytes' to convert it to dictionary we can use json.loads()
    message_dict = json.loads(messagen_json)
    print(f"message_dict  = {message_dict} , type = {type(message_dict)}")


"""

import json, socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect our socket to a tuple (Ip address & port address)
client_socket.connect((DEST_IP, DEST_PORT_NO))

# # receive the message form the server whch is in bytes
# messagen_json = client_socket.recv(BYTE_SIZE).decode(ENCODER)
# print(f"json_dict  = {messagen_json} , type = {type(messagen_json)}")

# # message_json is 'string' to convert it to dictionary we can use json.loads()
# message_dict = json.loads(messagen_json)
# print(f"message_dict  = {message_dict} , type = {type(message_dict)}")


# receive the message form the server whch is in bytes
messagen_json = client_socket.recv(BYTE_SIZE)
print(f"json_dict  = {messagen_json} , type = {type(messagen_json)}")

# message_json is 'bytes' to convert it to dictionary we can use json.loads()
message_dict = json.loads(messagen_json)
print(f"message_dict  = {message_dict} , type = {type(message_dict)}")


for key, value in message_dict.items():
    print(f"======> {key}:{value}")
