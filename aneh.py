m1 = [
    [5, 8,4],
    [2, 6,4],
]

m2 = [
    [1,8],
    [1,4],
    [2,2]
]

for x in range (len(m1)):
    for y in range(len(m2[0])):
        m3=[]
        for z in range(len(m2)):
            m3[x][y]+=m1[x][z]*m2[z][y]

for hasil in m3:
    print (hasil)
            

