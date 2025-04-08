import socket

bufferSize = 1024
localIP = "127.0.0.1"
localPort = 7500
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
        
def inputEquipID(equipmentID):
    bytesToSend = equipmentID.encode(FORMAT)
    client.sendto(bytesToSend, ADDR)


def send_game_code(code):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 7500)
    message = str(code).encode()
    sock.sendto(message, server_address)
    sock.close()

if __name__ == "__main__":
    print("Starting client...")