import tkinter, socket, threading, json
from datetime import datetime
from tkinter import DISABLED, VERTICAL, END, NORMAL, StringVar, VERTICAL

# Define window
root = tkinter.Tk()
root.title("Chat Server")
root.iconbitmap(r"03_basic_gui_chatroom\talk.ico")
root.geometry("600x600")
root.resizable(0, 0)


# Define fonts and colors
my_font = ("SimSun", 14)
# black = "#010101"
# light_green = "#1fc742"
light_green = "#B8D3CB"
black = "#12598E"
orange = "#FDAE73"
green = "#98AB59"
blue = "#98AB59"
purple = "#9c51b6"
root.config(bg=black)


# create connection class to hold server socket
class Connection:
    """A class to store a connection,  a server socket and pertinent info"""

    def __init__(self):
        self.host_ip = socket.gethostbyname(socket.gethostname())
        self.encoder = "utf-8"
        self.bytesize = 1024

        self.client_sockets = []
        self.client_ips = []
        self.banned_ips = []


# Define functions ==============================================================
def start_server(connection):
    """start the server on a given port"""
    # Get the port number to run the serrver & attach to the connection object
    connection.port = int(port_entry.get())

    # Create server socket, then bind it and then start listening
    connection.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.server_socket.bind((connection.host_ip, connection.port))
    connection.server_socket.listen()

    # Update GUI
    history_listbox.delete(0, END)  # Clear from index 0 to the last indez
    history_listbox.insert(0, f"Server started on port: {connection.port}.")
    end_button.config(state=NORMAL)
    self_broadcast_button.config(state=NORMAL)
    message_button.config(state=NORMAL)
    kick_button.config(state=NORMAL)
    ban_button.config(state=NORMAL)
    start_button.config(state=DISABLED)

    # Create a thread to continously listen for connections
    # Because we want to have more than one connection at a same time, so we use threading
    connect_thread = threading.Thread(target=connect_client, args=(connection,))
    connect_thread.start()


def close_server(connection):
    """Begin the process to close the server"""
    pass


def connect_client(connection):
    """connect an incoming clietn to server"""
    while True:
        try:
            client_socket, client_address = connection.server_socket.accept()
            # Check to see if the IP of the client is banned.
            # client address is a 'tuple' & first item in this tuple is client ip_address
            if client_address[0] in connection.banned_ips:
                message_packet = create_message(
                    "DISCONNECT",
                    "Admin (private)",
                    "You have been banned...bye",
                    light_green,
                )
                # because our message to client is in dictionary, first we have to change the format to 'string
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))

                # Clost the client socket
                client_socket.close()
            else:
                # Send a message pakcet to recieve client info
                message_packet = create_message(
                    "INFO", "Admin (private)", "Please send your name", light_green
                )
                # because our message to client is in dictionary, first we have to change the format to 'string
                # Therefore we use json.dumps() to convert it to 'string' and then encode it
                message_json = json.dumps(message_packet)
                client_socket.send(message_json.encode(connection.encoder))

                # Wait for confimration message to be sent verifiying the connection
                message_json = client_socket.recv(connection.bytesize)
                process_message(connection, message_json, client_socket, client_address)
        except:
            break


def create_message(flag, name, message, color):
    """Return a message packet to be sent (in dictionary)"""
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "color": color,
    }

    return message_packet


def process_message(connection, message_json, client_socket, client_address=(0, 0)):
    """Update server info based on a message packet flag"""
    pass


def broadcast_message(connection, message_json):
    """Send a message to all client sockets connected to the server"""
    pass


def receive_message(connection, client_socket):
    """Recieve an incoming message from a client"""
    pass


def self_broadcast(connection):
    """Broadcast a special admin message to all clients"""
    pass


def private_message(connection):
    """send a pivate messafe to a single client"""
    pass


def kick_client(coonection):
    """kick out the given client"""
    pass


def ban_client(coonection):
    """Ban a given client based on their IP address"""
    pass


#  Define gui layout

# create frames
connection_frame = tkinter.Frame(root, bg=black)
history_frame = tkinter.Frame(root, bg=black)
client_frame = tkinter.Frame(root, bg=black)
message_frame = tkinter.Frame(root, bg=black)
admin_frame = tkinter.Frame(root, bg=black)


connection_frame.pack(pady=5)
history_frame.pack()
client_frame.pack(pady=5)
message_frame.pack()
admin_frame.pack()


# connection_frame layout ======================================================
port_label = tkinter.Label(
    connection_frame,
    text="Port Number:",
    font=my_font,
    bg=black,
    fg=light_green,
)
port_entry = tkinter.Entry(
    connection_frame,
    width=10,
    borderwidth=1,
    font=my_font,
)
start_button = tkinter.Button(
    connection_frame,
    text="Start Server",
    borderwidth=1,
    width=15,
    font=my_font,
    bg=light_green,
    command=lambda: start_server(my_connection),
)
end_button = tkinter.Button(
    connection_frame,
    text="End Server",
    borderwidth=1,
    width=15,
    font=my_font,
    bg=light_green,
    state=DISABLED,
)


port_label.grid(row=0, column=0, padx=2, pady=10)
port_entry.grid(row=0, column=1, padx=2, pady=10)
start_button.grid(row=0, column=2, padx=5, pady=10)
end_button.grid(row=0, column=3, padx=5, pady=10)

# history_frame layout =========================================================
history_scrollbar = tkinter.Scrollbar(history_frame, orient=VERTICAL)
history_listbox = tkinter.Listbox(
    history_frame,
    height=10,
    width=55,
    borderwidth=3,
    font=my_font,
    bg=black,
    fg=light_green,
    yscrollcommand=history_scrollbar.set,
)
history_scrollbar.config(command=history_listbox.yview)

history_listbox.grid(row=0, column=0)
history_scrollbar.grid(row=0, column=1, sticky="NS")


# client_frame layout ==========================================================
client_scrollbar = tkinter.Scrollbar(client_frame, orient=VERTICAL)
client_listbox = tkinter.Listbox(
    client_frame,
    height=10,
    width=55,
    borderwidth=3,
    font=my_font,
    bg=black,
    fg=light_green,
    yscrollcommand=client_scrollbar.set,
)
client_scrollbar.config(command=client_listbox.yview)

client_listbox.grid(row=0, column=0)
client_scrollbar.grid(row=0, column=1, sticky="NS")

# message_frame layout =========================================================
input_entry = tkinter.Entry(message_frame, width=40, borderwidth=1, font=my_font)
self_broadcast_button = tkinter.Button(
    message_frame,
    text="Broadcast",
    width=13,
    borderwidth=5,
    font=my_font,
    bg=light_green,
    state=DISABLED,
)

input_entry.grid(row=0, column=0, padx=5, pady=5)
self_broadcast_button.grid(row=0, column=1, padx=5, pady=5)

# admin_frame layout ===========================================================
message_button = tkinter.Button(
    admin_frame,
    text="PM",
    borderwidth=5,
    width=15,
    font=my_font,
    bg=light_green,
    state=DISABLED,
)
kick_button = tkinter.Button(
    admin_frame,
    text="Kick",
    borderwidth=5,
    width=15,
    font=my_font,
    bg=light_green,
    state=DISABLED,
)
ban_button = tkinter.Button(
    admin_frame,
    text="Ban",
    borderwidth=5,
    width=15,
    font=my_font,
    bg=light_green,
    state=DISABLED,
)

message_button.grid(row=0, column=0, padx=5, pady=5)
kick_button.grid(row=0, column=1, padx=5, pady=5)
ban_button.grid(row=0, column=2, padx=5, pady=5)

# create an object of Connection class & then Run the root window's mainloop()
my_connection = Connection()
root.mainloop()
