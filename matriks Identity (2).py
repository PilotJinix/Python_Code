n=int(input())
u=0
r=1

for i in range (n):
    for x in range (u):
        print ('0',end='')
    u+=1
    print ('1',end='')
    for y in range (n-r):
        print('0',end='')
    r+=1
    print()
