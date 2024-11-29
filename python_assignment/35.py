matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

result = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[0])):
        row.append(matrix_2[i][j]+matrix_1[i][j])
    result.append(row)

for row in result:
    print(row)