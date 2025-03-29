from tkinter import BOTH, StringVar, END, Tk
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

# because all 3 buttons are linked to text_color, only one of them can be chosen
text_color = StringVar()
text_color.set("#ff0000")  # only one radiobutton will be chosen
red_button = tkinter.Radiobutton(
    input_frame, text="Red", variable=text_color, value="#ff0000", bg=input_color
)
green_button = tkinter.Radiobutton(
    input_frame, text="Green", variable=text_color, value="#00ff00", bg=input_color
)
blue_button = tkinter.Radiobutton(
    input_frame, text="Blue", variable=text_color, value="#0000ff", bg=input_color
)
red_button.grid(row=1, column=0)
green_button.grid(row=1, column=1)
blue_button.grid(row=1, column=2)

output_label = tkinter.Label(
    output_frame,
    text="--- Stored Messages ---",
    fg=input_color,
    bg=output_color,
    font=("Helvetica bold", 10),
)
output_label.pack(pady=15)

# run the root window's mainloop
root.mainloop()
