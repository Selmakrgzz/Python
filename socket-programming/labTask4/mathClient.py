from socket import *
import sys


def main():
    # Create a socket called "client_sd"
    # AF_INET indicates that the underlying network is using IPv4
    # SOCK_STREAM indicates that it is a TCP socket
    # If you want to use a UDP socket, use SOCK_DGRAM

    # Identify the server that you want to contact
    server_ip = '127.0.0.1'
    serverPort = 4848

    clientSocket = socket(AF_INET, SOCK_STREAM)
    try:
        # Connect to the server
        clientSocket.connect((server_ip,serverPort))
    except:
        print("Connection Error")
        sys.exit()
    while True:
        equation = input('Enter an mathematical operation:')
        # Send data
        clientSocket.send(equation.encode())
        # Read data from the socket
        received_line = clientSocket.recv(1024)
        # Print
        print ('From Server:', received_line.decode())
        if (equation == "exit"):
            break
    # Closing
    clientSocket.close()

if __name__ == '__main__':
	main()