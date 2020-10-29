data = []
jumlah=[]
x=int(input('mau berapa kali '))
for i in range (x):
    y=int(input('masukkan anggka yang kalian inginkan '))
    data.append(y)
cari = int(input('masukkan angka yang kalian cari '))
for i in range(0,len(data)):
    if cari==data[i]:
        print((cari),'ada di index ke ',(i))
        jumlah.append(cari)
    if cari!=data[i]:
        print('tidak ditemukan di index ke ',i)
print(jumlah)
print('jadi jumlah angka',cari,' yang sama ada ',len(jumlah))        
