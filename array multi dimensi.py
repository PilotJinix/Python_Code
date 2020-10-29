data1=[None]*3
for i in range (3):
    data1[i]=[None]*3
for x in range (3):
    
    for y in range (3):
        print(data1)

data2=[None]*3
for i in range (3):
    data2[i]=[None]*3
for x in range (3):
    for y in range (3):
        data2[x][y]=10
print(data2)

data3=[None]*3
for i in range (3):
    data3 [i]=[None]*3
for x in range (3):
    for y in range (3):
        data1[x][y]=30
        data2[x][y]=10
        data3=data1[x][y] + data2[x][y]
print (data3)
