import socket
import queue


server_should_stop = False

# This server implementation listens for events from the traffic generator
def start_udp_server(event_queue):
    bufferSize = 1024
    localIP = "127.0.0.1"
    localPort = 7501  # Server listens on port 7501

    # Create a datagram socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_socket.bind((localIP, localPort))

    print(f"UDP server up and listening on port {localPort}")

    # Listen for incoming datagrams
    while True:
        if server_should_stop:
            print("Game timer ended. Sending code to traffic generator.")
            stop_code = "221"
            server_socket.sendto(stop_code.encode('utf-8'), ("127.0.0.1", 7500))

        try:
            # Receive message from the client or traffic generator
            bytes_address_pair = server_socket.recvfrom(bufferSize)
            message = bytes_address_pair[0].decode('utf-8')  # Decode the message
            traffic_generator_address = ("127.0.0.1", 7500)

            if message == "202":
                print("Game Start Code (202) received from client.")
                # Forward the game start code to the traffic generator
                server_socket.sendto(message.encode('utf-8'), traffic_generator_address)
                print("Game Start Code (202) forwarded to Traffic Generator.")
            elif message == "221":
                print("Game Stop Code (221) received. Stopping server...")
                # Forward the stop code to the traffic generator
                server_socket.sendto(message.encode('utf-8'), traffic_generator_address)
                break
            else:
                #print(f"Event Recieved: {message}")
                event_queue.put(message)

                if ":" in message:
                    try:
                        shooter, target = message.split(":")
                        print(f"Event received: {target}")
                        acknowledgment = target
                    except ValueError:
                        print("Invalid message format.")
                        acknowledgment = "Invalid format"
                else:
                    print(f"Received unformatted message: {message}")
                    acknowledgment = "Invalid format"

                server_socket.sendto(acknowledgment.encode('utf-8'), traffic_generator_address)
                

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Close the socket when the server stops
    server_socket.close()
    print("UDP server has stopped.")