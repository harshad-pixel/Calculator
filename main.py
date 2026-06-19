i = float(input("Enter the value of first number :"))
j = float(input("Enter the value of second number :"))

op = input("Enter the operation to perform : ")

if op == "+" :
    print(i+j)
elif op == "-" :
    print(i-j)
elif op == "*" :
    print(i*j)
elif op == "/" :
    print(i/j)
else :
    print("Error!!")
