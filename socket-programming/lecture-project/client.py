#Necessary packages
from socket import *

def main():
	message = "Hello world"
	#Create a socket called "client_sd"
	#AF_INET indicates that underlying network is using IPv4
	#SOCK_STREAM indicates that it is a TCP socket
	#If you want to use UDP socket, use SOCK_DGRAM
	client_sd = socket(AF_INET, SOCK_STREAM)
	#Identify the server that you want to contact
	server_ip =  '10.0.2.15'
	port = 12000
	#Connect to the server

	#Send data
	client_sd.send(message.encode())

	#Read data from the socket
	received_line = client_sd.recv(1024).decode()

	#Print
	print(received_line)

	#Closing
