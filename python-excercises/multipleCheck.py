def multipleCheck(num, multipleNum):
    output="Output: "
    if num % multipleNum == 0:
        output+="True"
    else:
        output+="False"
    print(output)

multipleCheck(20,4)
