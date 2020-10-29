c=[]
b=int(input())
for i in range (b):
    a=int(input())
    hasil=0
    for i in range (a+1):
        hasil=hasil+i
    c.append(hasil)

for i in range (len(c)):
##    d='case #'+str(i+1)+":",c[i]
    print('case #'+str(i+1)+":",c[i])
    
