from socket import *
import sys
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
	clientSocket.connect((serverName,serverPort))
except:
	print("ConnectionError")
	sys.exit()
while True:
	sentence = input('Input lowercase sentence:')
	clientSocket.send(sentence.encode())
	modifiedSentence = clientSocket.recv(1024)
	print ('From Server:', modifiedSentence.decode())
	if (sentence == "exit"):
		break

clientSocket.close()