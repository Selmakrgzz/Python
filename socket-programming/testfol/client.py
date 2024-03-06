# Necessary packages
from socket import *

def main():
    # Create a socket called "client_sd"
    # AF_INET indicates that the underlying network is using IPv4
    # SOCK_STREAM indicates that it is a TCP socket
    # If you want to use a UDP socket, use SOCK_DGRAM
    client_sd = socket(AF_INET, SOCK_STREAM)

    # Identify the server that you want to contact
    server_ip = '127.0.0.12'
    port = 8000
    
    while True:
        equation = input('Connected to the server. Enter a mathematical operation (e.g., "7 + 10"):')

        if equation == "exit":
            break
        else:
            # Connect to the server
            client_sd.connect((server_ip, port))

            # Send data
            client_sd.send(equation.encode())

            # Read data from the socket
            received_line = client_sd.recv(1024).decode()

            if received_line:
                # Print
                result = f"Result from server : {received_line}"
            else:
                result = "No data received from the server"

            print(result)

    

    # Closing
    client_sd.close()

main()