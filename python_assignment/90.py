num = int(input("Enter a number: "))
temp = num
count = 0
while temp != 0:
    temp = temp//10
    count+=1
print(f"The Number of digits in {num} is {count}")