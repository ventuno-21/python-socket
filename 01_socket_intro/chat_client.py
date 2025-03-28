import socket


# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((DEST_IP, DEST_PORT_NO))


# send & receive messages
while True:
    # receive info from server
    message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

    # Quit if the connected server wants to quit, else keep sending messages
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\n client: ending the chat .. bye")
        break
    else:
        print(f"\n{message}")
        new_message = input("client message: ")
        client_socket.send(new_message.encode(ENCODER))

# if we write 'quit' we will break a while loop then we should close the connection
client_socket.close()
