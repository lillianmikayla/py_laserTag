import socket

# This server implementation only acts to ensure that the client is broadcasting correctly
# This server is not intended to be used for any other purpose right now.
 
def start_udp_server():
    bufferSize = 1024
    localIP = "127.0.0.1"
    localPort = 7500

    # Create a datagram socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_socket.bind((localIP, localPort))

    print("UDP server up and listening on port 7500")

    # Listen for incoming datagrams
    while True:
        bytes_address_pair = server_socket.recvfrom(bufferSize)
        message = bytes_address_pair[0]
        address = bytes_address_pair[1]

        client_msg = "Message from Client:{}".format(message.decode('utf-8'))
        client_ip = "Client IP Address:{}".format(address)

        print(client_msg)
        print(client_ip)