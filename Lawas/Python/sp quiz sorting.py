data = [[10,9,8,7,6],[5,4,3,2,1]]

for i in range(2):
    for k in range (5):
        for j in range (4):
            if data[i][j] > data [i][j+1]:
                data[i][j],data[i][j+1] = data[i][j+1],data[i][j]
if data[0]>data[1]:
    data[0],data[1] = data[1],data[0]
print (data)
