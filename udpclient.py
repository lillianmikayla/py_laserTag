import socket

bufferSize = 1024
localIP = "127.0.0.1"
localPort = 7502
ADDR = (localIP, localPort)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "221"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket.

def change_network(new_ip):
    global ADDR
    ADDR = (new_ip, localPort) # Update the address with the new IP.
    print(f"Client network changed to IP: {new_ip}, Port: {localPort}")

def player_added(player_count):
    equipmentID = input(f"Enter equipment ID of player {player_count}: ") # Collect equipment ID from user

    if equipmentID == DISCONNECT_MESSAGE: # If input = 221, disconnect.
            bytesToSend = equipmentID.encode(FORMAT) 
            client.sendto(bytesToSend, ADDR) 
            client.close()

    bytesToSend = equipmentID.encode(FORMAT)
    client.sendto(bytesToSend, ADDR)

    msgFromServer = client.recvfrom(bufferSize) 
    msg = "Message from Server{}".format(msgFromServer[0]) 
    print(msg)

    if player_count == 2:
        client.close()

    #slightly modified version of old logic below.
    """
    connected = True
    while connected:
        equipmentID = input(f"Enter equipment ID of player {player_count}: ") # Collect equipment ID from user.
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
            
        if player_count == 2: # If player_count = 2, break the loop.
            connected = False
    client.close() # Close the client.
    """

if __name__ == "__main__":
    print("Starting client...")
    

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