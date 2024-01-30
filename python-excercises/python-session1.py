print("hello world")
firstname = "selma"
lastname = "krgz"

"""second comment"""

fullname = firstname+ " "+lastname
#my first comment
print(fullname)

print(f"welcome {fullname} your age {20}")

num1=5
num2=6
print(type(num1))

name = str(num1)
print(type(name))

#age = int(input("type age"))
#print(f"your age{age}")

print(5 in [1,2,3,4])

number1 = 3

if number1==5:
    print("right")
else:
    print("your wrong")

count=1

while(count < 10):
    print("hello")
    count=count+1

for c in "python":
    print('characters: ' +c)

for i in range(1,10,1):
    print(i)

a = [1,2]
b = [3,4]

c=a+b

c.append(5)
c.append(6)
print(c)

car = {
    "brand": "tesla",
    "year": 2023,
    "color": "white"
}

print(car["year"])
print(car.values())


def agecheck(age):
    if age < 18:
        return "too young"
    return "your good"
    
val = agecheck(20)
print(val)

def test(nm1, nm2, nm3):
    sum = nm1+nm2+nm3
    product = nm1*nm2*nm3
    return "summen blir: " ,sum,  "Produktet: " ,product



val2=test(1,2,3)
print(val2)