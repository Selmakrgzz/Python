#Necessary packages
from socket import *

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
                num2=list[i] #If the operand is not emty(we have passed an operand), we'll assign the num2 to the second val
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
	result = calculation(received_line)
	print(result)

	#Send data back over the connection
	conn_sd.send(str(result).encode())

	#Closing code
	conn_sd.close()
	server_sd.close()

if __name__ == "__main__":
    main()