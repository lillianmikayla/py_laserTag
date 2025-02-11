# Implementing using sam_pyudptutorial and Strother example code.

import socket

msgFromClient = "Hello, I am a UDP client!" # Message to send to server.
bytesToSend = str.encode(msgFromClient)
bufferSize = 1024

localPort   = 7501 # Maybe change?
SERVER = socket.gethostbyname(socket.gethostname()) # Get IP address of computer, change to hardcode maybe?
ADDR = (SERVER, localPort) # Tuple.
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket.
# client.connect(ADDR) # Connect to server.

client.sendto(bytesToSend, ADDR) # Send message to server.

msgFromServer = client.recvfrom(bufferSize)
msg = "Message from Server{}".format(msgFromServer[0])

print(msg) # Print message from server, should be the client's equipment number.