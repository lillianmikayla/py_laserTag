# Implementing using sam_pyudptutorial and Strother example code.

import socket
import threading

# localIP     = "192.168.0.75"
localPort   = 7501 # Maybe change?
SERVER = socket.gethostbyname(socket.gethostname()) # Get IP address of computer, change to hardcode maybe?
ADDR = (SERVER, localPort) # Tuple.
FORMAT = 'utf-8'

buffersize = 1024
msgFromServer = "Hello UDP Client, [1234567890] is your equipment code."
bytesToSend = str.encode(msgFromServer)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket.
server.bind(ADDR) # Bind the server to the address.

print(f"[STARTING] Server is starting...")
print(f"[LISTENING] Server is listening on {SERVER}")

while(True):
    bytesAddressPair = server.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    server.sendto(bytesToSend, address)


# def start():
#     server.listen()
#     print(f"[LISTENING] Server is listening on {SERVER}")
#     while (True):
#         # bytesAddressPair = server.recvfrom(buffersize)
#         conn, addr = server.accept()
#         bytesAddressPair = conn, addr
#         thread = threading.Thread(target=handle_client, args=(bytesAddressPair))
#         thread.start()

#         # message = bytesAddressPair[0]
#         # address = bytesAddressPair[1]
#         # clientMsg = "Message from Client:{}".format(message)
#         # clientIP = "Client IP Address:{}".format(address)

#         # print(clientMsg)
#         # print(clientIP)

#         # server.sendto(bytesToSend, address)

# def handle_client(bytesAddressPair):
#     print(f"[NEW CONNECTION] {bytesAddressPair[1]} connected.")
#     connected = True
#     while connected:
#         msg = bytesAddressPair[0].recv(buffersize).decode(FORMAT)
#         if msg:
#             msg_1 = bytesAddressPair[0].recv(msg).decode(FORMAT)
#             if msg_1 == "DISCONNECT":
#                 connected = False
            
#             print(f"[{bytesAddressPair[1]}] {msg}")
#             bytesAddressPair[0].send("Msg received".encode(FORMAT))
    
#     bytesAddressPair[0].close()
    
    
#     # bytesAddressPair[0].send(bytesToSend)
#     # print(f"[NEW CONNECTION] {bytesAddressPair[1]} connected.")
#     # connected = True
#     # while connected:
#     #     msg = bytesAddressPair[0].recv(buffersize).decode(FORMAT)
#     #     if msg == "DISCONNECT":
#     #         connected = False
#     #     print(f"[{bytesAddressPair[1]}] {msg}")
#     #     bytesAddressPair[0].send("Msg received".encode(FORMAT))

#     # bytesAddressPair[0].close()

# print("[STARTING] Server is starting...")
# start()