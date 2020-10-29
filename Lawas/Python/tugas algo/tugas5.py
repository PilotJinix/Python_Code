print ("Nama: Muhammad Agung Santoso")
print ("NIM : 182410103081")
print ("Algoritma dan Pemrograman II F")

print("selamat datang ditabungan study excursie ")
harga=1500000
cicilan=0
bulan=0
batas=12
kurang=0
terbayar=0


a=input("apakah anda akan membayar cicilannya ? ya/tidak   ")
    
if a=="ya":
    while bulan<=12:
        bayar=int(input("Mau bayar berapa ?  "))
        terbayar=terbayar+bayar
        if terbayar>=1500000:
            print("Selamat Biaya study excursie anda telah ","LUNAS")
            break
        kurang=harga-terbayar
        bulan+=1
        batas-=1
        if batas==0:
            print("Mohon maaf, anda belum bisa mengikuti study excursie kali ini karena dana anda kurang,untuk study excursie hingga waktu pengumpulan saat ini masih kurang sebesar", "RP",kurang," Silahkan coba lagi tahun depan, dan lebih hemat dan rajin menabung")
            break
        cicilan=kurang//batas
        print("Biaya study excursie anda kurang",kurang,"Rupiah")
        print ("Karena sisa waktu anda tinggal",batas,"bulan")
        print ("sebaiknya anda membayar cicilan senilai",cicilan,"Rupiah","per bulan")
else:
    print("Anda tidak bisa mengikuti study excursie")
    
    
    
