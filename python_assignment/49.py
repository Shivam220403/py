arr = [1,2,3,4,5,6,7,8,9]
num = int(input("Enter a number to search in array: "))

for i in range(0, len(arr)):
    if num == arr[i]:
        print(i)
