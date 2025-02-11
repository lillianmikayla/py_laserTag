import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.75" # Change to your IP address.
ADDR = (SERVER, PORT)

udpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udpclient.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # Add spaces to make it 64 bytes.
    udpclient.send(send_length)
    udpclient.send(message)
    print(udpclient.recv(2048).decode(FORMAT)) # Print message received from server.

send("Hello World!")
send("Hello Everyone!")
send("Hello Tim!")

send(DISCONNECT_MESSAGE) # Disconnect from server.