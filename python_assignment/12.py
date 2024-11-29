n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2st number: "))
n3 = int(input("Enter 3st number: "))
temp = 0
if n1 > n2:
    temp = n1
    if n3 > n1:
        temp = n3
else:
    temp = n2
    if n3 > n2:
        temp = n3

print(temp)
