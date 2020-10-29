a=int(input("masukkan barapa angka yang mau kalian input="))
n=[]
for i in range (a):
    n.append(input())
print (n)
for j in range (len (n)-1):
    for k in range (len(n)-1):
        if n[k]>n[k+1]:
    #       n[j],n[j+1]=n[j+1],n[j]
            
                temp=n[k]
                n[k]=n[k+1]
                n[k+1]=temp

                print (n)
