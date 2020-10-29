namaF=[]
hargaberas=[]
tanggungan=[]
totalzakatF=[]
namaM=[]
hargaemas=[]
tabungan=[]
totalzakatM=[]


def fitrah():
    a=input("Masukkan nama anda : ")
    c=int(input("Masukkan harga beras 1 kg : "))
    d=int(input("Berapa jumlah anggota keluarga yang anda tanggung = "))
    total=d*c*25/10
    namaF.append(a)
    hargaberas.append(c)
    totalzakatF.append(total)
    print(namaF)
    
def mall():
    b=input("Masukkan nama anda : ")
    e=int(input("Masukkan harga emas saat ini : "))
    emas=e*85
    f=int(input("Masukkan total tabungan anda selama 1 tahun = "))
    if f>=emas:
        g=f*25/10
        namaM.append(b)
        hargaemas.append(e)
        tabungan.append(f)
        totalzakatM.append(g)
    else:
        print("")
        print("Anda belum bisa melakukan zakat Mall untuk saat ini")
        print("")

def hapus():
    hapus=input("Hapus data sesuai nama = ")
    index=namaF.index(hapus)
    print(index)
    namaF.remove(namaF[index])
    

while True:
    print("=====SELAMAT DATANG=======")
    print("==========ZAKAT===========")
    print("")
    masuk=input("Masuk sebagai = customer / admin ")
    print("")
    if masuk=="customer":
        while True:
            print("=====SELAMAT DATANG=======")
            print("1.Membayar Zakat \n2.Pengertian Zakat Fitrah \n3.Pengertian Zakat Mall \n4.Selesai")
            pilihan=int(input("Masukkan pilihan anda = "))
            if pilihan==1:
                print("Macam Macam Zakat \n1.Fitrah \n2.Mall")
                pilihanzakat=int(input("Pilih Sesuai Nomer = "))
                if pilihanzakat==1:
                    fitrah()
                elif pilihanzakat==2:
                    mall()
                else:
                    print()
                    print("SILAKAN COBA LAGI")
                    print()
            elif pilihan==2:
                print("=================================================Zakat Fitrah=======================================================")
                print()
                print("Zakat fitrah adalah zakat yang wajib dikeluarkan umat Muslim menjelang hari raya Idul Fitri atau pada bulan Ramadan.")
                print("Zakat fitrah dapat dibayar dengan setara 3,5 liter (2,5 kilogram) makanan pokok dari daerah yang bersangkutan.")
                print("Makanan pokok di Indonesia adalah nasi, maka yang dapat dijadikan sebagai zakat adalah berupa beras.")
                print()
            elif pilihan==3:
                print("===================================================Zakat Mall=========================================================")
                print()
                print("Zakat maal (harta) adalah zakat penghasilan seperti hasil pertanian, hasil pertambangan, hasil laut, hasil perniagaan,")
                print("hasil ternak, harta temuan, emas dan perak. Masing-masing jenis penghasilan memiliki perhitungannya sendiri.")
                print()
            elif pilihan==4:
                keluar=input("Apa Anda Yakin Untuk Keluar = ya / tidak ")
                print("")
                if keluar=="ya":
                    break
                else:
                    print()

    elif masuk=="admin":
        u="agung"
        p="agung"
        i=0
        z=True
        while True:
            print("=============================================")
            print("================Silakan Login================")
            print("=============================================")
            print("")
            while True:
                u=input("Masukkan Username = ")
                p=input("Masukkan Password = ")
                if u=="agung" and p=="agung":
                    break
                print("")
                print("SILAKAN COBA LAGI!!")
                print("")
                i+=1
                if i==3:
                    print("Maaf kami terpaksa untuk mengeluarkan anda ")
                    exit()
            while True:
                print("=====SELAMAT DATANG=======")
                print("1.Melihat semua orang yang berzakat \n2.Menghapus data pezakat \n3.Selesai")
                pilihan=int(input("Pilih sesuai nomor = "))
                if pilihan==1:
                    pilih=int(input("Pilih Jenis Zakat \n1.Zakat Fitrah\n2.Zakat Mall"))
                    if pilih==1:
                        for i in range (len(namaF)):
                            print(i+1,".",namaF[i]," berzakat sebesar = ",totalzakatF[i])
                    elif pilih==2:
                        for i in range (len(namaM)):
                            print(i+1,".",namaM[i]," berzakat sebesar = ",totalzakatM[i])
                    
                elif pilihan==2:
                    hapus()
                    print("")
                    print("Selamat data telah terhapus")
                    print("")
                elif pilihan==3:
                    break
                    
                else:
                    print("")
                    print("Silakan Coba Lagi!!")
                    print("")
            break

