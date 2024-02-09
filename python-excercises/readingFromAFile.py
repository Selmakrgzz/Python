from decimal import Decimal, getcontext
getcontext().prec = 50

#Checking what type of unit and returning the answer
def checkType(val):
    kilo='Kbps'
    mega='Mbps'
    giga='Gbps'

    if kilo in val:
        return kilo
    elif mega in val:
        return mega
    elif giga in val:
        return giga

#Converting the num based on the type
#Converting all of them to bps to compare later
def convert(num, type):
    numDec=Decimal(num)

    if type == 'Kbps':
        numDec=numDec*Decimal(1000)
        return numDec
    elif type == 'Mbps':
        numDec=numDec*Decimal(1000000)
        return numDec
    elif type == 'Gbps':
        numDec=numDec*Decimal(1000000000)
        return numDec

def result(list, convertedList):
    minVal=min(convertedList) #Finding the min value in the converted list
    index=convertedList.index(minVal) #Finding the index of the min value
    result=list[index] #Since both lists are sorted the same the index of min value will be the same in list
    return result

def main():
    f = open('throughput_values.txt', 'r')

    convertedList=[] #List that will hold on the converted values
    list=[]
    num='' #Variable that will hold on the put-together-num from the given file
    type='' #Saving the type of unit so we can use it for right conversion

    for i in f: 
        list.append(i)
        type=checkType(i) #Saving the unit type for later use
        for j in i:
            if j.isdigit(): #Checking if the chars in i contains integers
                num=num+str(j) #If so we'll put together the integers as string
            elif j == 's': #When we come to the end of unit for instant Kbp[s], Mbp[s], Gbp[s]
                converted=convert(num,type)
                convertedList.append(float(converted)) #Adding the converted values to the list
                num='' #Emtying the variable num
            
    print(f"Result is: {result(list, convertedList)}")

main()
