a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))
operation = input("Enter the operation: A for +,B for -,C for * , D for / : ").lower()
if operation == 'a':
    print(f"{a}+{b} = {a+b}")
elif operation == 'b':
    print(f"{a}-{b} = {a - b}")
elif operation == 'c':
    print(f"{a}*{b} = {a * b}")
elif operation == 'd':
    print(f"{a}/{b} = {a / b}")
else:
    print(f"{operation} is invalid ")
