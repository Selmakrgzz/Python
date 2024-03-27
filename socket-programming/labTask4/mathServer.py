#Necessary packages
from socket import *
import _thread as thread
import sys

#Operations
def addition(num1, num2):
    sum=int(num1)+int(num2)
    return sum

def subtraction(num1, num2):
    sum=int(num1)-int(num2)
    return sum

def multiplication(num1, num2):
    sum=int(num1)*int(num2)
    return sum

def division(num1, num2):
    sum=int(num1)/int(num2)
    return sum

def modulo(num1, num2):
    sum=int(num1)%int(num2)
    return sum

#Converting the equation to an array
def inputAppend(input):
    result=[]
    num=''
    for i in input:
        if i.isdigit():
            num+=str(i)
        else:
            if num: #If num is not emty(holding a number)
                result.append(int(num))
                num=''
            result.append(i)
    if num:
        result.append(int(num))
    return result

def calculation(equation):
    list = inputAppend(equation)
    
    #print(list)
    sum=0
    num1=0
    num2=0
    operand=''

    for i in range(0, len(list), 1):
        if isinstance(list[i], int): #Checking if the val is an int
            if operand == '': #If the operand is an emty string, then there is a num there
                num1=list[i] #Assigning num1 to val on index i
                #print(f"num nr{i}: {num1}") 
            else:
                num2=list[i] #If the operand is not emty(we have passed an operand), we will assign the num2 to the second val
                #print(f"num nr{i}: {num2}")
                if operand == '+': #If the operand is the given operation
                    sum=addition(num1, num2)
                if operand == '-': #If the operand is the given operation
                    sum=subtraction(num1, num2)
                if operand == '*': #If the operand is the given operation
                    sum=multiplication(num1, num2)
                if operand == '/': #If the operand is the given operation
                    sum=division(num1, num2)
                if operand == '%': #If the operand is the given operation
                    sum=modulo(num1, num2)
                operand='' #Emtying the operand string for next loop
                num1=sum #Setting num1 to sum
        elif isinstance(list[i], str): #Checking if the val is a string aka an operand
            operand=list[i] #Assigning the val to the operand variable
    return sum


def handleClient(connection, addr):
    print(f"Accepted connection from {addr}")

    while True:
        received_line = connection.recv(1024).decode()

        if  received_line == "exit":
            break
        else:
            print(f"Received equation: {received_line}")

            #Read data from the client and print
            result = calculation(received_line)

            #Send data back over the connection
            connection.send(str(result).encode())
		
    connection.close()
    print(f"Connection with {addr} closed")



def main():
    #Define how the client can connect
    server_ip = '127.0.0.1'
    serverPort = 4848

    #Create a socket called "server_sd"
    serverSocket = socket(AF_INET,SOCK_STREAM)

    try:
        #Wait for a connection, and create a new socket "conn_sd" for that connection
        serverSocket.bind((server_ip,serverPort))
    except: 
        print("Bind failed. Error : ")
        sys.exit()

    #Skriver ut melding til terminalen at serveren venter på gitt ip og port
    print(f"Server listening on {server_ip} :{serverPort}")

    #Activating listening on the socket
    serverSocket.listen(1)

    #Skriver ut melding at serveren venter på kobling
    print("Waiting for connections...")

    while True:
        #Server waits on accept() for connections
        connectionSocket, addr = serverSocket.accept() 

        #Skriver ut melding at server har koblet til gitt ip og port
        print(f"New connection from {addr}") 
        thread.start_new_thread(handleClient, (connectionSocket, addr))
        
        if not handleClient:
            break
    serverSocket.close()
             
    

if __name__ == '__main__':
	main()
