data=[5,3,1,2]
b=0

for i in range (len(data)-1):
    b=i
    print('nilai i=',i)
    print('Nilai b=',b)
    
    for j in range (i+1,len(data)):
        print('nilai j=',j)
        if data[b]>data[j]:
            b=j
            print ('nilai b=',b)
    temp=data[b]
    data[b]=data[i]
    data[i]=temp
    print(data)
    
        
