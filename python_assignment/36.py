matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        if i != j and j < i:
            matrix_1[i][j], matrix_1[j][i] = matrix_1[j][i], matrix_1[i][j]

for rows in matrix_1:
    print(rows)
