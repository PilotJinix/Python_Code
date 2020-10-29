data =[5,3,1,2]
max = len(data)
print('niali awal data :',data)
idproses =1

for x in range (1,max,1):
    print('x =',x)
    for y in range (x,0,-1):
        print('ketika y =',y)
        if data[y]<data[y-1]:
            temp=data[y-1]
            data[y-1]=data[y]
            data[y]=temp
            print('terjadi pertukaran data',data)
        else:
            print('tidak terjadi pertukaran data')
    print('hasil pertukaran pada proses ke ',idproses,':',data)
    idproses+=1

