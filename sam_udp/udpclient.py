import socket

bufferSize = 1024
localIP = "127.0.0.1"
localPort = 7501
ADDR = (localIP, localPort)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "221"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket.

connected = True
while connected:
    cnt = 0
    while cnt < 2:
        equipmentID = input(f"Enter equipment ID of green player {cnt + 1}: ") # Collect equipment ID from user.
        if equipmentID == DISCONNECT_MESSAGE: # If input = 221, disconnect.
            bytesToSend = equipmentID.encode(FORMAT) 
            client.sendto(bytesToSend, ADDR) 
            connected = False # Break the loop.
            break
        
        else: # If input is not 221, send the equipment ID to the server.
            bytesToSend = equipmentID.encode(FORMAT)
            client.sendto(bytesToSend, ADDR)

            msgFromServer = client.recvfrom(bufferSize) 
            msg = "Message from Server{}".format(msgFromServer[0]) 
            print(msg)

            cnt += 1 # Increment.
        
        if cnt == 2: # If cnt = 2, break the loop.
            connected = False

client.close() # Close the client.
    

# # Simple input statement.
# connected = True
# while connected:
#     equipmentID = input("Enter equipment ID: ")
#     if equipmentID == DISCONNECT_MESSAGE:
#         bytesToSend = equipmentID.encode(FORMAT)
#         client.sendto(bytesToSend, ADDR)
#         connected = False
#     else:
#         bytesToSend = equipmentID.encode(FORMAT)
#         client.sendto(bytesToSend, ADDR)
#         msgFromServer = client.recvfrom(bufferSize)
#         msg = "Message from Server{}".format(msgFromServer[0])
#         print(msg)
# client.close()