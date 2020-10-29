mat1 = [
    [5, 0,],
    [2, 6,]
]

mat2 = [
    [1,8],
    [1,4]
]
print(mat1)
print(mat2)

mat3 = []

for x in range(len(mat1)):
    row = []
    for y in range(len(mat1[0])):
        total = 0
        for z in range(len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(len(mat3)):
    for y in range(len(mat3[0])):
        print (mat3[x][y], end=' ')
    print()

