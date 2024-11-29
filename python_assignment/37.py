a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]


for rows in result:
    print(rows)
