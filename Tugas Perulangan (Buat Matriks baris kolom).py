x=int(input("Baris = "))
y=int(input("Kolom = "))
a=1
b=1
data1=[]
while a <= x:
    k=int(input('masukkan angka yang diingikan'))
    data1.append(k)
    while b <= y:
        o=int(input('masukkan angka yang diingikan'))
        data1.append(o)
        #print (b)
        #print ("baris ke",a,"kolom ke",b)
        b+=1
    b=1
    a+=1
print(data1[a][b], end=' ')
print()
