#Functions
def af():
    n3=35
    print('local n3', n3)

n2=40

af()
print('global n2', n2)

#Lists
num = [1,2,3,4,5,6,7]
new_num1 = []

"""for i in num:
    new_num.append(i)"""

new_num1 = [i for i in num]
new_num2 = [i for i in num if i > 3]

print(new_num1)
print(new_num2)


try:
    f = open ('text.txt', 'r')

    data = f.read()

    """for line in f:  
        print(data)"""

    print(data)

    print("done")

    f.close()
except FileNotFoundError:
    print("fant ikke")

with open('text.txt', 'r') as f:
    data2 = f.read()
    print(data2)


try:
    inputTall = input('skriv et tall')
    int(inputTall)
    print('ok')
except:
    print('ikke tall')

#access the command line
import sys

print('first argument ', sys.argv[0])

#import modules
import argparse
import sys
parser = argparse.ArgumentParser(description="simple argument parser")
parser.add_argument('name', help="please enter your name")
parser.add_argument('-n1', '--num1') #one - is short name, -- is long name
parser.add_argument('-n2', '--num2')

args = parser.parse_args()
print(f"your first num:  {args.num1} second is: {args.num2}")
print(f"your name is: {args.name}")