from tkinter import BOTH, END, Tk
import tkinter

# define a window
root = Tk()
root.title("chatroom")
# root.iconbitmap("./t alk.ico")
root.iconbitmap(r"03_basic_gui_chatroom\talk.ico")
# root.iconphoto(False, tkinter.PhotoImage(file="talk.ico"))
root.geometry("400x600")
root.resizable(0, 0)  # it means you are not allow to resize it


# Define colors
root_color = "#e4cfa1"
input_color = "#4f646f"
output_color = "#dee7e7"
root.config(bg=root_color)

# define functions


# Define Gui layout
# Define Frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# Define Widgets
message_entry = tkinter.Entry(
    input_frame, text="Enter a message", width=25, font=("Helvetica", 12)
)
send_button = tkinter.Button(input_frame, text="Send", bg=output_color)
message_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
send_button.grid(row=0, column=3, rowspan=2, padx=10, pady=10, ipadx=20, ipady=5)


# run the root window's mainloop
root.mainloop()
