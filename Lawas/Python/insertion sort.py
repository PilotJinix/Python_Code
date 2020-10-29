data=[5,3,1,2]

##for i in range (1,len(data)):
##    a=data[i]
##    j=i-1
##    while j>=0 and a<data[j]:
##        data[j+1]=data[j]
##        j-=1
##        data[j+1]=a
##        print(data)
print()
print()

for i in range (1,len(data)+1):
    for j in range (len(data)-1):
        if data[j+1]<data[j]:
            data[j+1],data[j]=data[j],data[j+1]
            print(data)
