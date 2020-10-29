q = input()
a = int(len(q))
temp = 0
for i in range (0,a,1):
    if q[i] == '_':
        temp = temp+1
    elif q[i] == '.':
        print (chr(temp),end = '')
        temp = 0
    
