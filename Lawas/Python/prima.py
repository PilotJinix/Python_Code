a=int(input())

if a>1:
    for i in range (2,a):
        print(i)
        if (a % i)==0:
            
            print("bukan")
            break
        else:
            print("iya")
            break
print("===================")
print("no4")
b=int(input("masukkan angka"))


for i in range (b):
    if i%2==0:
        print(i)
        
