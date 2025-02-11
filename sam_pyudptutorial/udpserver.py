import socket
import threading # Separate code so a client isn't waiting for another one to interact with server.

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # Get IP address of computer.
ADDR = (SERVER, PORT) # Tuple.
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket, AF_INET is over internet.
server.bind(ADDR) # Bind the server to the address.

def handle_client(conn, addr): # Handle individual connections, running concurrently.
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # Tells us how long the message is.
        if msg_length:
            msg_length = int(msg_length) # Convert to integer.
            msg = conn.recv(msg_length).decode(FORMAT) # Receive message.
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT)) # Send message back to client.
    
    conn.close()

def start(): # Start listening for connections, pass to handle_client.
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # Wait for a new connection to the server, store address, store and object to send information back to connection.
        thread = threading.Thread(target=handle_client, args=(conn, addr)) # Create new thread for each connection.
        thread.start()
        print([f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}"]) # Amount of threads = amount of clients.

print("[STARTING] Server is starting...")
start()