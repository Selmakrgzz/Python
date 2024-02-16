#Necessary packages
from socket import *

def main():
	#Create a socket called "server_sd"
	server_sd = socket (AF_INET, SOCK_STREAM)
	#Define how the client can connect
	port = 12000
	server_ip = ' 10.0.2.15'
	#Wait for a connection, and create a new socket "conn_sd" for that connection

	#Read data from the client and print
	received_line = conn_sd.recv(1024).decode()
	print(received_line)

	#Send data back over the connection
	conn_sd.send(received_line.encode())

	#Closing code
