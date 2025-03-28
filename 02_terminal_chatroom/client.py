import socket
import threading


DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT_NO = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect our socket to a tuple (Ip address & port address)
client_socket.connect((DEST_IP, DEST_PORT_NO))


def send_message():
    """send a message to the server to be broadcast"""
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))


def recieve_message():
    """Receiving an incoming message from server"""
    while True:
        try:
            # receive an incoming message from server
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

            # check for the "NAME" flag, else show the message
            if message == "NAME":
                name = input("What is your name ?")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # An error occured, close the connection
            print("An error occured ...")
            client_socket.close()
            break


# # Start the client
# recieve_message()

# creating threads to continously send & receive messages
recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

recieve_thread.start()
send_thread.start()

recieve_thread.join()
send_thread.join()
