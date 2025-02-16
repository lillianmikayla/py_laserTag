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
    bytesToSend = equipmentID.encode(FORMAT)
    client.sendto(bytesToSend, ADDR)

    #Hello UDP Client Message:
    #for some reason whenever I try to remove this message from the server it breaks the code so it stays for now
    msgFromServer = client.recvfrom(bufferSize) 
    msg = "Message from Server{}".format(msgFromServer[0]) 
    #print(msg)
<<<<<<< HEAD

    #if player_count == 2:
        #client.close()
=======
>>>>>>> 53776695eb9ce80fdcae9fe3897adaa166e21b02
 
if __name__ == "__main__":
    print("Starting client...")
    
