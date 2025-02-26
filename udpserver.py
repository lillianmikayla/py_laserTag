import socket

localIP = "127.0.0.1"
localPort = 7501
ADDR = (localIP, localPort)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "221" 
buffersize = 1024

msgFromServer = "Hello UDP Client."
bytesToSend = str.encode(msgFromServer)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket.

def change_network(new_ip):
    global ADDR
    ADDR = (new_ip, localPort) # Update the address with the new IP.
    print(f"Server network changed to IP: {new_ip}, Port: {localPort}")

def start_server():
    server.bind(ADDR) # Bind the server to the address.
    print(f"[STARTING] Server is starting...")

    while True:
        connected = True
        message, address = server.recvfrom(buffersize) 
        while connected:
            if message.decode(FORMAT) == DISCONNECT_MESSAGE: # If input = 221, disconnect.
                connected = False
                clientMsg = "Player has disconnected.".format(message)
                print(clientMsg)
            else:
                clientMsg = "[SERVER] Here is player's equipment number: {}".format(message)
                print(clientMsg)
                server.sendto(bytesToSend, address)

            if connected:
                message, address = server.recvfrom(buffersize) # Receive message from client.

if __name__ == "__main__":
    start_server()