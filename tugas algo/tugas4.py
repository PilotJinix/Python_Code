print ("Nama: Muhammad Agung Santoso")
print ("NIM : 182410103081")
print ("Algoritma dan Pemrograman II F")

print("1.segitiga normal")
print("2.segitiga terbalik")
a=int(input("Pilih segitiga?"))
if (a==1):
    d=""
    l=1
    b=int(input("masukkan jumlah level segitiga:"))
    while (l<=b):
       i=l
       while(i>0):
           d+="*"
           i-=1
       d=d+"\n"
       l+=1
    print(d)
    
elif (a==2):
    b=int(input("masukkan jumlah level piramida?"))
    f=""
    while(b>0):
        k=b
        while(k>0):
            f+="*"
            k-=1
        b-=1
        f=f+"\n"
    print(f)
    
