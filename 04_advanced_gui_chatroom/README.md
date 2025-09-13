# 🧠 Advanced GUI Chatroom (Python Socket)

This project is a feature-rich, multi-client chatroom built using Python's `socket` and `tkinter` libraries. It demonstrates how to combine networking and GUI programming to create a real-time messaging application with a clean interface and responsive performance.

---

## 🚀 Features

- **Client-Server Architecture**  
  Centralized server handles multiple clients using threads.

- **Graphical User Interface**  
  Built with `tkinter` for a user-friendly chat experience.

- **Real-Time Messaging**  
  Messages are instantly broadcast to all connected clients.

- **Threaded Communication**  
  Ensures smooth GUI performance while handling socket I/O.

- **User Join/Leave Notifications**  
  Keeps all participants informed of chatroom activity.

---

## 🧩 Folder Structure

04_advanced_gui_chatroom/ ├── client.py # GUI-based chat client ├── server.py # Multi-threaded chat server └── README.md # Project documentation (you can replace this with the content below)

Codice

---

## 📦 Requirements

- Python 3.x  
- No external dependencies — uses built-in libraries like `socket`, `threading`, and `tkinter`

---

## 🖥️ How to Run

### 1. Start the Server

Run the following command in your terminal to start the server:

```bash
python server.py
The server will start listening for incoming connections on a specified port.

2. Launch Clients
Open a new terminal window and run:

bash
python client.py
Each client opens a GUI window where users can enter their name and start chatting.

🛠️ Implementation Highlights
Server
Accepts multiple connections using threading.Thread

Broadcasts messages to all connected clients

Handles client disconnection gracefully

Client
GUI built with tkinter

Separate thread for receiving messages to avoid blocking the UI

Input field and send button for user interaction

📚 Learning Objectives
This project is ideal for understanding:

Socket programming fundamentals

GUI development with tkinter

Threading for concurrent I/O

Basic client-server communication patterns
