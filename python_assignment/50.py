arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
temp = []
for i in range(0, len(arr)):
    for j in range(0, len(arr[0])):
        temp.append(arr[i][j])
arr = temp
temp = []
print(arr)