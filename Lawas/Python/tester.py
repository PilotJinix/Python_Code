data=['m','b','h','r','z']

for i in range (len(data)-1):
    for j in range (len(data)-1):
        if data[j]<data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]

print(data)
