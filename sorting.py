a=int(input("masukkan barapa angka yang mau kalian input="))
n=[]
for i in range (a):
    n.append(input())
print (n)
for j in range (len (n)-1):
    print(j)
    for k in range (len(n)-1):
        print ('k',k)
        if n[k]>n[k+1]:
            n[k],n[k+1]=n[k+1],n[k]
            print (n)
                #temp=n[k]
                #n[k]=n[k+1]
                #n[k+1]=temp

