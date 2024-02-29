#Necessary packages
from socket import *

def main():
	#Create a socket called "server_sd"
	server_sd = socket (AF_INET, SOCK_STREAM)
	#Define how the client can connect
	port = 12000
	server_ip = '127.0.0.1'

	#Wait for a connection, and create a new socket "conn_sd" for that connection
	server_sd.bind((server_ip, port))

	#Activating listening on the socket
	server_sd.listen(1)

	#Server waits on accept() for connections
	conn_sd, addr = server_sd.accept()

	#Read data from the client and print
	received_line = conn_sd.recv(1024).decode()
	print(received_line)

	#Send data back over the connection
	conn_sd.send(received_line.encode())

	#Closing code
	conn_sd.close()
	server_sd.close()

main()