import tkinter


# define a window
root = tkinter.Tk()
root.title("chatroom")
# root.iconbitmap("./t alk.ico")
root.iconbitmap(r"03_basic_gui_chatroom\talk.ico")
# root.iconphoto(False, tkinter.PhotoImage(file="talk.ico"))
root.geometry("400x600")
root.resizable(0, 0)  # it means you are not allow to resize it


# Define colors
root_color = "#535657"
input_color = "#4f646f"
output_color = "#dee7e7"
root.config(bg=root_color)

# define functions


# Define Gui layout

# run the root window's mainloop
root.mainloop()
