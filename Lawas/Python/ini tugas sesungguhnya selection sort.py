print('selamat datang')
barang=['buku','pulpen','pensil','penghapus','penggaris','kotak pensil','tas','sepatu','seragam','bola basket']
harga=[5000,3000,2000,1000,4000,7000,50000,150000,75000,250000]
pesanan=[]
harga_pesanan=[]
for a in range (len(barang)):
    print(a+1,barang[a])
b=int(input('mau beli berapa barang ?'))
for a in range (b):
    c=int(input('pilih sesuai nomer = '))
    c-=1
    if -1<c<11:
        pesanan.append(barang[c])
        harga_pesanan.append(harga[c])
for d in range (b):
    print(pesanan[d],'=',harga_pesanan[d])
d=input('pesanan sudah sesuai ?(ya/tidak)')
if d=='tidak':
    print('silakan mengulangi kembali dengan menekan ok lalu F5')
    exit()
d=input('mau mengurutkan berdasarkan nama atau harga ? ')
if d=='nama':
    print('<===============>')
    print('2 cara pengurutan')
    print('1.Ascending')
    print('2.descending')
    f=int(input('Pilih sesuai nomer = '))
    if f == 1:
        for i in range (len(pesanan)-1):
            b=i
            for j in range (i+1,len(pesanan)):
                if pesanan[b]>pesanan[j]:
                    b=j
            pesanan[b],pesanan[i]=pesanan[i],pesanan[b]
            harga_pesanan[b],harga_pesanan[i]=harga_pesanan[i],harga_pesanan[b]
            print(pesanan,harga_pesanan)
    if f == 2:
        for i in range (len(pesanan)-1):
            b=i
            for j in range (i+1,len(pesanan)):
                if pesanan[b]<pesanan[j]:
                    b=j
            pesanan[b],pesanan[i]=pesanan[i],pesanan[b]
            harga_pesanan[b],harga_pesanan[i]=harga_pesanan[i],harga_pesanan[b]
            print(pesanan,harga_pesanan)
    if f!=1 and f!=2 :
        print('silakan mengulangi kembali dengan menekan ok lalu F5')
        exit()
if d=='harga':
    print('<===============>')
    print('2 cara pengurutan')
    print('1.Ascending')
    print('2.descending')
    f=int(input('Pilih sesuai nomer = '))
    if f == 1:
        for i in range (len(harga_pesanan)-1):
            b=i
            for j in range (i+1,len(harga_pesanan)):
                if harga_pesanan[b]>harga_pesanan[j]:
                    b=j
            pesanan[b],pesanan[i]=pesanan[i],pesanan[b]
            harga_pesanan[b],harga_pesanan[i]=harga_pesanan[i],harga_pesanan[b]
            print(harga_pesanan,pesanan)
    if f == 2:
        for i in range (len(harga_pesanan)-1):
            b=i
            for j in range (i+1,len(harga_pesanan)):
                if harga_pesanan[b]<harga_pesanan[j]:
                    b=j
            pesanan[b],pesanan[i]=pesanan[i],pesanan[b]
            harga_pesanan[b],harga_pesanan[i]=harga_pesanan[i],harga_pesanan[b]
            print(harga_pesanan,pesanan)
    if f!=1 and f!=2 :
        print('silakan mengulangi kembali dengan menekan ok lalu F5')
        exit()
if d!='nama' and d!='harga':
    print('silakan mengulangi kembali dengan menekan ok lalu F5')
    exit()
    
            
            
        
    
    



    
        


