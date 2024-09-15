a = int(input("ENTER THE 1ST: "))
b = int(input("ENTER THE 2nd: "))

s = (input("TYPE 1 FOR ADD \n TYPE 2 FOR SUBTRACTION \n TYPE * FOR MULTIPLY \n TYPE / FOR DEVIDE: "))

if s == "+":
    print("THE ADDITION IS : ",a + b)
elif s == "-":
    print("THE subtracTION IS : ",a - b)
elif s == "*":
    print("THE multiply IS : ",a * b)
else:
    print("THE division IS : ",a / b)


