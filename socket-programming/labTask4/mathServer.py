#Necessary packages
from socket import *

def main():
	#Create a socket called "server_sd"
	server_sd = socket (AF_INET, SOCK_STREAM)
	#Define how the client can connect
	port = 8000
	server_ip = '127.0.0.1'

	#Wait for a connection, and create a new socket "conn_sd" for that connection
	server_sd.bind((server_ip, port))
	print(f"Server listening on {server_ip}:{port}") #Skriver ut melding til terminalen at serveren venter på gitt ip og port
	#Activating listening on the socket
	server_sd.listen(1)
	print("Waiting for connections...") #Skriver ut melding at serveren venter på kobling
	#Server waits on accept() for connections
	conn_sd, addr = server_sd.accept()
	print(f"New connection from {addr}") #Skriver ut melding at server har koblet til gitt ip og port
	#Read data from the client and print
	received_line = conn_sd.recv(1024).decode()
	print(received_line)

	#Send data back over the connection
	conn_sd.send(received_line.encode())

	#Closing code
	conn_sd.close()
	server_sd.close()

if __name__ == "__main__":
    main()