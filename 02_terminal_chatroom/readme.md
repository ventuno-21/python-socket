# Terminal Chatroom

This project demonstrates a simple terminal-based chatroom application built using Python's socket programming. It allows multiple clients to connect to a server and communicate with each other in real-time through their terminal interfaces.

## Features

- **Multi-client support**: Multiple clients can connect to the server simultaneously.
- **Real-time messaging**: Messages sent by one client are broadcasted to all connected clients in real-time.
- **Terminal-based interface**: The application operates entirely within the terminal, without the need for a graphical user interface.

## Requirements

- Python 3.x
- `socket` module (usually included with Python standard library)

## Setup and Usage

### 1. Clone the repository

```bash
git clone https://github.com/ventuno-21/python-socket.git
cd python-socket/02_terminal_chatroom
2. Run the server
bash
Copia codice
python server.py
3. Run the client
bash
Copia codice
python client.py
Multiple clients can be run simultaneously on different terminals or machines by specifying the server's IP address and port.

How It Works
Server: Listens for incoming client connections, accepts them, and creates a new thread for each client to handle communication.

Client: Connects to the server, sends messages, and listens for incoming messages from other clients.

Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

Licens
