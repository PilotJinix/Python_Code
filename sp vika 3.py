import random
print ("=== SELAMAT DATANG DI APLIKASI JODOH METER ===")
masukan=""
cewe=[]
cowo=[]
banyak=0
print ("=====================================================")
while True:
    pilihan=input("Apa jenis kelamin anda (wanita/pria) = ")

    if pilihan=="pria":
        nama=input("masukkan nama anda = ")
        banyak=int(input("masukkan jumlah pasangan anda = "))
        for i in range (banyak):
            masukan=input("masukkan nama pasangan anda = ")
            cewe.append(masukan)
        for j in range (len(cewe)):
            print ("=======================================================")
            print (cewe[j])
            match = random.randrange(0,100)
            print ("match meter",match, '%')
            if match > 80 :
                print (" ndang rabi")
            elif match >60:
                print (" pikir- pikir")
            elif match >40:
                print ("yakin? ")
            elif match > 20 :
                print (" cari lagi ")
            else:
                print ("putusin aja")
                print ("=======================================================")

    if pilihan=="wanita":
        nama=input("masukkan nama anda = ")
        banyak=int(input("masukkan jumlah pasangan anda = "))
        for i in range (banyak):
            masukan=input("masukkan nama pasangan anda = ")
            cowo.append(masukan)
        for j in range (len(cowo)):
            print ("=======================================================")
            print (cowo[j])
            match = random.randrange(0,100)
            print ("match meter",match, '%')
            if match > 80 :
                print (" ndang rabi")
            elif match >60:
                print (" pikir- pikir")
            elif match >40:
                print ("yakin? ")
            elif match > 20 :
                print (" cari lagi ")
            else:
                print ("putusin aja")
                print ("=======================================================")
    confir =input ("Apakah anda setuju sama hasilnya ? y/n ")
    if confir=='y':
        break
    

    
