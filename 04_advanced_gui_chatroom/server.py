import tkinter
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

# Define functions


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


# message_frame layout =========================================================


# admin_frame layout ===========================================================


# Run the root window's mainloop()
root.mainloop()
