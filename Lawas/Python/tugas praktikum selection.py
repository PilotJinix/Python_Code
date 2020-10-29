nama_sayur=[]
harga_sayur=[]
sayur=int(input('Mau Beli Berapa Sayur?'))
b=0
for i in range (sayur):
    nama_sayur.append(input('nama sayur = '))
    harga_sayur.append(int(input('harga sayur = ')))
print()
print('<======================================================>')
print()
print('1 = Untuk mengurutkan daftar belanja dari harga termurah')
print('2 = Untuk mengurutkan daftar belanja dari harga termahal')
print()
x=int(input('Ingin mengurutkan dari mana,1 atau 2 ?'))
if x == 1:
    for i in range (len(harga_sayur)-1):
        b=i
        print('nilai i=',i)
        print('Nilai b=',b)
        
        for j in range (i+1,len(harga_sayur)):
            print('nilai j=',j)
            if harga_sayur[b]>harga_sayur[j]:
                b=j
                print ('nilai b=',b)
        temp=harga_sayur[b]
        harga_sayur[b]=harga_sayur[i]
        harga_sayur[i]=temp
        temp=nama_sayur[b]
        nama_sayur[b]=nama_sayur[i]
        nama_sayur[i]=temp
        print(nama_sayur)
        print(harga_sayur)
else:
    for i in range (len(harga_sayur)-1):
        b=i
        print('nilai i=',i)
        print('Nilai b=',b)
    
        for j in range (i+1,len(harga_sayur)):
            print('nilai j=',j)
            if harga_sayur[b]<harga_sayur[j]:
                b=j
                print ('nilai b=',b)
        temp=harga_sayur[b]
        harga_sayur[b]=harga_sayur[i]
        harga_sayur[i]=temp
        temp=nama_sayur[b]
        nama_sayur[b]=nama_sayur[i]
        nama_sayur[i]=temp
        print(nama_sayur)
        print(harga_sayur)
