# Client Side GUI Chat Room
import tkinter, socket, threading, json
from tkinter import DISABLED, VERTICAL, END, NORMAL, StringVar

# Define window
root = tkinter.Tk()
root.title("Chat Client")
# root.iconbitmap(r"03_basic_gui_chatroom\talk.ico")
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

# Define socket constants
ENCODER = "utf-8"
BYTESIZE = 1024
global client_socket


# create connection class to hold client socket
class Connection:
    """A class to store a connection,  a client socket and pertinent info"""

    def __init__(self):
        self.encoder = "utf-8"
        self.bytesize = 1024


# Define Functions
def connect(connection):
    """Connect to a server at a given ip/port address"""
    # Clear any previous chats from index 0 to the last one which is 'END'
    my_listbox.delete(0, END)

    # Get required info for connection from input fields
    connection.name = name_entry.get()
    connection.target_ip = ip_entry.get()
    connection.port = port_entry.get()
    connection.color = text_color.get()

    try:
        # Create a client socket
        connection.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.client_socket.connect((connection.target_ip, int(connection.port)))

        # Recieve an incoming message packet from the server
        message_json = connection.client_socket.recv(connection.bytesize)
        process_message(connection, message_json)
    except:
        my_listbox.insert(0, "Connection not established...Bye.")


def verify_connection(name):
    pass
    # """Verify that the server connection is valid and pass required information"""
    # global client_socket

    # # The server will send a NAME flag if a valid connection is made
    # flag = client_socket.recv(BYTESIZE).decode(ENCODER)

    # if flag == "NAME":
    #     # The connection was made, send client name and await verification
    #     client_socket.send(name.encode(ENCODER))
    #     # Server will broadcast your name
    #     message = client_socket.recv(BYTESIZE).decode(ENCODER)

    #     if message:
    #         # Server sent a verification, connection is valid!
    #         my_listbox.insert(0, message)

    #         # Change button/entry states
    #         connect_button.config(state=DISABLED)
    #         disconnect_button.config(state=NORMAL)
    #         send_button.config(state=NORMAL)

    #         name_entry.config(state=DISABLED)
    #         ip_entry.config(state=DISABLED)
    #         port_entry.config(state=DISABLED)

    #         # Create a thread to contiuously recieve messages from the server
    #         recieve_thread = threading.Thread(target=recieve_message)
    #         recieve_thread.start()
    #     else:
    #         # No verification message was recieved
    #         my_listbox.insert(0, "Connection not verified. Bye...")
    #         client_socket.close()
    # else:
    #     # No name flag was sent, connection was refused
    #     my_listbox.insert(0, "Connection is refused. Bye...")
    #     client_socket.close()


def disconnect(connection):
    """Disconnect client from the server"""
    # Create a message packet to be sent
    message_packet = create_message(
        "DISCONNECT", connection.name, "I am leaving.", connection.color
    )
    message_json = json.dumps(message_packet)
    connection.client_socket.send(message_json.encode(connection.encoder))

    # Disable GUI for chat
    gui_end()


def gui_start():
    """Officially start connection by updating GUI/ enable/disable buttones"""
    connect_button.config(state=DISABLED)
    disconnect_button.config(state=NORMAL)
    send_button.config(state=NORMAL)
    name_entry.config(state=DISABLED)
    ip_entry.config(state=DISABLED)
    port_entry.config(state=DISABLED)

    for button in color_buttons:
        button.config(state=DISABLED)


def gui_end():
    """Officially end connection by updating GUI"""
    connect_button.config(state=NORMAL)
    disconnect_button.config(state=DISABLED)
    send_button.config(state=DISABLED)
    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)

    for button in color_buttons:
        button.config(state=NORMAL)


def create_message(flag, name, message, color):
    """Return a message packet to be sent"""
    message_packet = {
        "flag": flag,
        "name": name,
        "message": message,
        "color": color,
    }
    return message_packet


def process_message(connection, message_json):
    """Update the client based on message packet flag"""
    pass
    # Update the chat history first by unpacking the json message.
    message_packet = json.loads(message_json)  # decode and turn to dict in one step!
    flag = message_packet["flag"]
    name = message_packet["name"]
    message = message_packet["message"]
    color = message_packet["color"]

    if flag == "INFO":
        # Server is asking for information to verify connection.  Send the info.
        message_packet = create_message(
            "INFO", connection.name, "Joins the server!", connection.color
        )
        message_json = json.dumps(message_packet)
        connection.client_socket.send(message_json.encode(connection.encoder))

        # Enable GUI for chat
        gui_start()

        # Create a thread to coninousuly recieve messages from the server
        recieve_thread = threading.Thread(target=recieve_message, args=(connection,))
        recieve_thread.start()

    elif flag == "MESSAGE":
        # Server has sent a message so display it
        my_listbox.insert(0, f"{name}: {message}")
        my_listbox.itemconfig(0, fg=color)

    elif flag == "DISCONNECT":
        # Server is asking you to leave (kicked/banned by server )
        my_listbox.insert(0, f"{name}: {message}")
        my_listbox.itemconfig(0, fg=color)
        disconnect(connection)

    else:
        # Catch for errors...
        my_listbox.insert(0, "Error processing message...")


def send_message(connection):
    """Send a message to the server to be broadcast"""
    # Send the message to the server
    message_packet = create_message(
        "MESSAGE", connection.name, input_entry.get(), connection.color
    )
    # convert dictionary to 'string' so be able to send it to server
    message_json = json.dumps(message_packet)
    connection.client_socket.send(message_json.encode(connection.encoder))

    # Clear the input entry from index 0 to last index which in 'END'
    input_entry.delete(0, END)


def recieve_message(connection):
    """Recieve an incoming message from the server"""
    while True:
        # Recive an incoming message packet from the server
        try:
            # Recive an incoming message packet
            message_json = connection.client_socket.recv(connection.bytesize)
            process_message(connection, message_json)
        except:
            # Cannot recive message, close the connection and break
            my_listbox.insert(0, "Connection has been closed...Bye.")
            break


# Define GUI Layout
# Create Frames
info_frame = tkinter.Frame(root, bg=black)
color_frame = tkinter.Frame(root, bg=black)
output_frame = tkinter.Frame(root, bg=black)
input_frame = tkinter.Frame(root, bg=black)

info_frame.pack()
color_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

# Info Frame Layout ======================================================
name_label = tkinter.Label(
    info_frame, text="Client Name:", font=my_font, fg=light_green, bg=black
)
name_entry = tkinter.Entry(info_frame, borderwidth=1, font=my_font)
ip_label = tkinter.Label(
    info_frame, text="Host IP:", font=my_font, fg=light_green, bg=black
)
ip_entry = tkinter.Entry(info_frame, borderwidth=1, font=my_font)
port_label = tkinter.Label(
    info_frame, text="Port Num:", font=my_font, fg=light_green, bg=black
)
port_entry = tkinter.Entry(info_frame, borderwidth=1, font=my_font, width=10)
connect_button = tkinter.Button(
    info_frame,
    text="Connect",
    font=my_font,
    bg=light_green,
    borderwidth=5,
    width=10,
    # command=connect,
    command=lambda: connect(my_connection),
)
disconnect_button = tkinter.Button(
    info_frame,
    text="Disconnect",
    font=my_font,
    bg=light_green,
    borderwidth=5,
    width=10,
    state=DISABLED,
    # command=disconnect,
    command=lambda: disconnect(my_connection),
)

name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

# Color Frame Layout ======================================================
text_color = StringVar()
text_color.set("#ff0000")  # only one radiobutton will be chosen
orange_button = tkinter.Radiobutton(
    color_frame,
    text="Orange",
    variable=text_color,
    value=orange,
    bg=black,
    font=my_font,
    fg=light_green,
    width=5,
)
green_button = tkinter.Radiobutton(
    color_frame,
    text="Green",
    variable=text_color,
    value=green,
    bg=black,
    font=my_font,
    fg=light_green,
    width=5,
)
blue_button = tkinter.Radiobutton(
    color_frame,
    text="Blue",
    variable=text_color,
    value=blue,
    bg=black,
    font=my_font,
    fg=light_green,
    width=5,
)
purple_button = tkinter.Radiobutton(
    color_frame,
    text="Purple",
    variable=text_color,
    value=purple,
    bg=black,
    font=my_font,
    fg=light_green,
    width=5,
)
color_buttons = [orange_button, green_button, blue_button, purple_button]
orange_button.grid(row=1, column=0, padx=2, pady=2)
green_button.grid(row=1, column=1, padx=2, pady=2)
blue_button.grid(row=1, column=2, padx=2, pady=2)
purple_button.grid(row=1, column=3, padx=2, pady=2)


# Output Frame Layout ======================================================
my_scrollbar = tkinter.Scrollbar(output_frame, orient=VERTICAL)
my_listbox = tkinter.Listbox(
    output_frame,
    height=20,
    width=55,
    borderwidth=3,
    bg=black,
    fg=light_green,
    font=my_font,
    yscrollcommand=my_scrollbar.set,
)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")  # NS = North to south

# Input Frame Layout ======================================================
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=1, font=my_font)
send_button = tkinter.Button(
    input_frame,
    text="send",
    borderwidth=5,
    width=10,
    font=my_font,
    bg=light_green,
    state=DISABLED,
    command=lambda: send_message(my_connection),
    # command=send_message,
)
input_entry.grid(row=0, column=0, padx=5)
send_button.grid(row=0, column=1, padx=5)

# create an object of Connection class & Run the root window's mainloop()
my_connection = Connection()
root.mainloop()
