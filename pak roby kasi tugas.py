n=[5,3,1,2]

for j in range (len(n)-1):            
    for k in range (len(n)-1):
        if n[k]<n[k+1]:
            n[k],n[k+1]=n[k+1],n[k]
        print (n)
