data=[[10,9,8,7,6],
      [5,4,3,2,1]]

for i in range (1):
    for o in range (4):
        if data[i][o]>data[i][o+1:
            temp=data[i][o]
            data[i][o]=n[i][o+1]
            data[i][o+1]=temp

print(data)
                
