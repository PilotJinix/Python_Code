# class Daftar:
#
#     flashdisk_32_GB = 80000
#     flashdisk_64_GB = 150000
#     hardisk_1_TB = 1000000
#     UPS_1000W = 500000
#     CPU_desktop = 5000000
#
#     def __init__(self, nama , shop, jlm, nama1, shop1, jlm1, nama2 = "", shop2 =0, jlm2=0, nama3 = "", shop3=0, jlm3=0, nama4 = "", shop4=0, jlm4=0):
#         self.nama = nama
#         self.nama1 = nama1
#         self.nama2 = nama2
#         self.nama3 = nama3
#         self.nama4 = nama4
#         self.belanja = shop
#         self.jumlah = jlm
#         self.belanja1 = shop1
#         self.jumlah1 = jlm1
#         self.belanja2 = shop2
#         self.jumlah2 = jlm2
#         self.belanja3 = shop3
#         self.jumlah3 = jlm3
#         self.belanja4 = shop4
#         self.jumlah4 = jlm4
#
#     def cek(self):
#         totalpembelian = self.belanja * self.jumlah + self.belanja1 * self.jumlah1 + self.belanja2 * self.jumlah2 + self.belanja3 * self.jumlah3 + self.belanja4 * self.jumlah4
#         totalpembelianasli = totalpembelian
#         if(totalpembelian < 500000):
#             diskon = "Diskon 0 %"
#             jumlahdiskon = totalpembelian * 0
#             totalpembelian = totalpembelian
#             bonus = "-"
#
#         elif(totalpembelian >= 500000 and totalpembelian < 1500000):
#             diskon = "Diskon 1 %"
#             jumlahdiskon = totalpembelian * 0.01
#             totalpembelian = totalpembelian * 0.99
#             bonus = "-"
#
#         elif (totalpembelian >= 1500000 and totalpembelian < 5000000):
#             diskon = "Diskon 4 %"
#             jumlahdiskon = totalpembelian * 0.04
#             totalpembelian = totalpembelian * 0.96
#             bonus = "-"
#
#         else :
#             diskon = "Diskon 10 %"
#             jumlahdiskon = totalpembelian * 0.1
#             totalpembelian = totalpembelian * 0.9
#             if(totalpembelian > 10000000):
#                 bonus = totalpembelian // 10000000
#
#         return "No \t Nama Barang \t\t Harga \t\t jumlah \t\t jumlah * Harga \n1. \t {} \t {} \t\t {} \t\t\t\t\t {}\n2. \t {} \t {} \t {} \t\t\t\t\t {}\n3. \t {} \t\t {} \t {} \t\t\t\t\t {}\n4. \t {} \t {} \t\t {} \t\t\t\t\t {}\n5. \t {} \t {} \t\t {} \t\t\t\t\t {} \n---------------------------------------------------------------------- + \n \t\t\t\t\t\t\t\t\t Total \t\t\t\t {} \n \t\t\t\t\t {} x \t{}\t\t\t\t {} \n---------------------------------------------------------------------- - \n\t\t\t\t\t\t\t Total dibayar \t\t\t\t{} \n\t\t\t\t\t\t\t\t\t Bonus \t\t\t\t\t{} ".format(self.nama, self.belanja,self.jumlah,self.jumlah*self.belanja,self.nama1, self.belanja1,self.jumlah1,self.jumlah*self.belanja1,self.nama2, self.belanja2,self.jumlah2,self.jumlah2*self.belanja2,self.nama3, self.belanja3,self.jumlah3,self.jumlah3*self.belanja3,self.nama4, self.belanja4,self.jumlah4,self.jumlah4*self.belanja4,totalpembelianasli,diskon,totalpembelianasli, jumlahdiskon,totalpembelian,bonus)
#
# barang1 = Daftar("flashdisk_32_GB",Daftar.flashdisk_32_GB,5,"flashdisk_64_GB",Daftar.flashdisk_64_GB,4,"hardisk_1_TB",Daftar.hardisk_1_TB,2)
# barang2 = Daftar(Daftar.CPU_desktop,1,Daftar.UPS_1000W,1,Daftar.hardisk_1_TB,1)
# barang3 = Daftar(Daftar.CPU_desktop,2,Daftar.flashdisk_32_GB,5,Daftar.hardisk_1_TB,2)
# barang4 = Daftar(Daftar.flashdisk_32_GB,1,Daftar.flashdisk_64_GB,1)
# barang5 = Daftar(Daftar.flashdisk_32_GB,1,Daftar.flashdisk_64_GB,1,Daftar.hardisk_1_TB,1,Daftar.UPS_1000W,1,Daftar.CPU_desktop,1)

# print(barang1.cek())

# class Kualitas:
#
#     def __init__(self, name, seed, weight ):
#         self.nama = name
#         self.biji = seed
#         self.berat = weight
#
#
#     def cek(self):
#         if (self.biji >= 2 and self.berat > 2):
#             kualitas4 = 'SUPER'
#         elif (self.berat <= 2 and self.berat >= 1.5):
#             kualitas4 = 'BIASA'
#         else:
#             kualitas4 = 'CURAH'
#         return "Kualitas Biji = {}".format(kualitas4)
#
#
# jumlahbiji = float(input("Masukkan jumlah biji buah edamame  = "))
# beratedam = float(input("Masukkan jumlah berat buah edamame  = "))
# edam = Kualitas("Edamame pertama",jumlahbiji, beratedam  )
# print("======================================================================")
# jumlahbiji1 = float(input("Masukkan jumlah biji buah edamame  = "))
# beratedam1 = float(input("Masukkan jumlah berat buah edamame  = "))
# edam1 = Kualitas("Edamame pertama",jumlahbiji1, beratedam1  )
# print("======================================================================")
# jumlahbiji2 = float(input("Masukkan jumlah biji buah edamame  = "))
# beratedam2 = float(input("Masukkan jumlah berat buah edamame  = "))
# edam2 = Kualitas("Edamame pertama",jumlahbiji2, beratedam2  )
# print("======================================================================")
# jumlahbiji3 = float(input("Masukkan jumlah biji buah edamame  = "))
# beratedam3 = float(input("Masukkan jumlah berat buah edamame  = "))
# edam3 = Kualitas("Edamame pertama",jumlahbiji3, beratedam3  )
# print("======================================================================")
# print(edam.cek())
# print("===============================")
# print(edam1.cek())
# print("===============================")
# print(edam2.cek())
# print("===============================")
# print(edam3.cek())

### Nomer 3
# class RumusFisika:
#     def DayaListrik(self, usaha, waktu):
#         return usaha / waktu
#
#     def HambatanListrik(self, volt, ampere):
#         return volt / ampere
#
#     def Gaya(self, massa, percepatan):
#         return massa * percepatan
#
#
# class RumusMatematika:
#     def VolumeBalok(self, panjang, lebar):
#         return panjang * lebar
#
#     def LuasBalok(self, panjang, lebar):
#         return 2 * (panjang * lebar + panjang * lebar + panjang * lebar)
#
#     def VolumeKubus(self, sisi):
#         return sisi * sisi * sisi
#
#     def LuasKubus(self, sisi):
#         return 6 * (sisi * sisi)
#
#     def VolumeBola(self, jari):
#         return (4 / 3 * 3.14 * (jari * jari * jari))
#
#     def LuasBola(self, jari):
#         return (4 * 3.14 * (jari * jari))
#
#
# from random import randint as rand
#
# daftarPujian = ["k-fear", "goblok", "awtis"]
# daftarSambutan = ["Hai", "Halooo", "Welkam to mobel lejen"]
# fisika = RumusFisika()
# matematika = RumusMatematika()
# print(daftarSambutan[rand(0, len(daftarSambutan) - 1)] + " Segawon " + daftarPujian[rand(0, len(daftarPujian) - 1)])
# print("Pilihan Mata Pelajaran: "
#       "\n1.Rumus Fisika"
#       "\n2.Rumus Matematika"
#       "\nMasukkan pilihan dengan angka: ")
# mataPelajaran = int(input())
# if (mataPelajaran==1):
#     print(
#         "Pilih Rumus: "
#         "\n1.Daya Listrik"
#         "\n2.Hambatan Listrik"
#         "\n3.Gaya"
#         "\nMasukkan pilihan dengan angka: ")
#     rumus = int(input())
#     if (rumus==1):
#         print(fisika.DayaListrik(
#             int(input("Masukkan usaha: ")),
#             int(input("Masukka waktu: "))
#         ))
#     elif(rumus==2):
#         print(fisika.HambatanListrik(
#             int(input("Masukkan volt: ")),
#             int(input("Masukkan ampere: "))
#         ))
#     elif(rumus==3):
#         print(fisika.Gaya(
#             int(input("Masukkan massa: ")),
#             int(input("Masukkan percepatan: "))
#         ))
#     else:
#         print("Inputan salah")
# elif(mataPelajaran==2):
#     print(
#         "Pilih Rumus: "
#         "\n1.Volume Balok"
#         "\n2.Luas Balok"
#         "\n3.Volume Kubus"
#         "\n4.Luas Kubus"
#         "\n5.Volume Bola"
#         "\n6.Luas Bola"
#         "\nMasukkan pilihan dengan angka: ")
#     rumus = int(input())
#     if (rumus==1):
#         print(matematika.VolumeBalok(
#             int(input("Masukkan Panjang: ")),
#             int(input("Masukkan Lebar: "))
#         ))
#     elif(rumus==2):
#         print(matematika.LuasBalok(
#             int(input("Masukkan Panjang: ")),
#             int(input("Masukkan Lebar: "))
#         ))
#     elif(rumus==3):
#         print(matematika.VolumeKubus(
#             int(input("Masukkan Sisi: "))
#         ))
#     elif(rumus==4):
#         print(matematika.LuasKubus(
#             int(input("Masukkan Sisi: "))
#         ))
#     elif(rumus==5):
#         print(matematika.VolumeBola(
#             int(input("Masukkan Jari-Jari: "))
#         ))
#     elif(rumus==6):
#         print(matematika.LuasBola(
#             int(input("Masukkan Jari-Jari: "))
#         ))
#     else:
#         print("Inputan salah")
# else:
#     print("Inputan salah")

# ### Nomer 2
# class Mahasiswa:
#     def __init__(self, nama, nim, ipk, ukt):
#         self.__nama = nama
#         self.__nim = nim
#         self.__ipk = ipk
#         self.__ukt = ukt
#
#     def set_nama(self, nama):
#         self.__nama = nama
#
#     def get_nama(self):
#         return self.__nama
#
#     def set_nim(self, nim):
#         self.__nim = nim
#
#     def get_nim(self):
#         return self.__nim
#
#     def set_ipk(self, ipk):
#         self.__ipk = ipk
#
#     def get_ipk(self):
#         return self.__ipk
#
#     def set_ukt(self, ukt):
#         self.__ukt = ukt
#
#     def get_ukt(self):
#         return self.__ukt
#
#
# daftarMahasiswa = [
#     Mahasiswa("Agung", 182410103081, 3.7, 9000000),
#     Mahasiswa("Dida", 182410102001, 3.4, 1000000),
#     Mahasiswa("Dewangga", 182410103005, 3.0, 2500000)
# ]
#
# def searchMahasiswaByNim(nim):
#     for mahasiswa in daftarMahasiswa:
#         if mahasiswa.get_nim() == nim:
#             return mahasiswa
#
# print("Masukkan NIM Mahasiswa: ")
# mahasiswa = searchMahasiswaByNim(int(input()))
#
# print(mahasiswa.get_nama())
# print(mahasiswa.get_nim())
# print(mahasiswa.get_ipk())
# print(mahasiswa.get_ukt())
#
# if (mahasiswa.get_ipk() >= 3.5):
#     print('kamu memenuhi kualifikasi')
# elif (mahasiswa.get_ipk() < 3.5):
#     if mahasiswa.get_ukt() > 4000000:
#         print("maaf kamu tidak memenuhi kualifikasi")
#     else:
#         print('kamu memenuhi kualifikasi')
# else:
#     print("maaf kamu tidak memenuhi kualifikasi")
import sqllite3

class Barang:
    def __init__(self, namaBarang, hargaBarang):
        self.namaBarang = namaBarang
        self.hargaBarang = hargaBarang


class Toko:
    def __init__(self, namaToko, jumlahKaryawan, jamBuka, jamTutup, daftarBarang):
        self.__namaToko = namaToko
        self.__jumlahKaryawan = jumlahKaryawan
        self.__jamBuka = jamBuka
        self.__jamTutup = jamTutup
        self.__daftarBarang = daftarBarang

    def get_namaToko(self):
        return self.__namaToko

    def set_namaToko(self, namaToko):
        self.__namaToko = namaToko

    def get_jumlahKaryawan(self):
        return self.__jumlahKaryawan

    def set_jumlahKaryawan(self, jumlahKaryawan):
        self.__jumlahKaryawan = jumlahKaryawan

    def get_jamBuka(self):
        return self.__jamBuka

    def set_jamBuka(self, jamBuka):
        self.__jamBuka = jamBuka

    def get_jamTutup(self):
        return self.__jamTutup

    def set_jamTutup(self, jamTutup):
        self.__jamTutup = jamTutup

    def get_daftarBarang(self):
        return self.__daftarBarang

    def set_daftarBarang(self, daftarBarang):
        self.__daftarBarang = daftarBarang

    def tambahkanBarang(self, barang):
        self.__daftarBarang.append(barang)

    def kurangiBarang(self, indexBarang):
        self.__daftarBarang.pop(indexBarang)


# test
barangToko1 = [Barang("sepatu x", 5000), Barang("sepatu y", 7000)]
toko1 = Toko("Toko saya", 10, 9, 20, barangToko1)

print(toko1.get_namaToko())
for i in range(len(toko1.get_daftarBarang())):
    print(i, toko1.get_daftarBarang()[i].namaBarang, toko1.get_daftarBarang()[i].hargaBarang)
# end test

# main
daftarToko = [toko1]


def cekToko(indexToko):
    print("Nama Toko: ", daftarToko[indexToko].get_namaToko())
    print("Jumlah Karyawan: ", daftarToko[indexToko].get_jumlahKaryawan())
    print("Jam Buka: ", daftarToko[indexToko].get_jamBuka())
    print("Jam Tutup: ", daftarToko[indexToko].get_jamTutup())
    daftarBarang = daftarToko[indexToko].get_daftarBarang()
    print("Daftar Barang: ")

    index = 0;
    for barang in daftarBarang:
        print(index, barang.namaBarang, barang.hargaBarang)
        index += 1
    # for i in range (len(daftarNamaBarang)):
    #     print(i, daftarNamaBarang[i], daftarHargaBarang[i])


def cekSemuaToko():
    for i in range(len(daftarToko)):
        print("Index Toko: ", i)
        cekToko(i)


def tambahToko(tokoBaru):
    daftarToko.append(tokoBaru)


def kurangiToko(indexToko):
    daftarToko.remove(indexToko)


def tambahkanBarangToko(indexToko, barang):
    daftarToko[indexToko].tambahkanBarang(barang)


def kurangiBarangToko(indexToko, indexBarang):
    daftarToko[indexToko].kurangiBarang(indexBarang)


def cekBarangToko(indexToko):
    for i in range(len(daftarToko[indexToko].get_daftarBarang())):
        print(i, daftarToko[indexToko].get_daftarBarang()[i].namaBarang,
              daftarToko[indexToko].get_daftarBarang()[i].hargaBarang)


def buatDaftarBarang():
    daftarBarang = []
    while True:
        daftarBarang.append(Barang(
            input("Masukkan nama Barang: "),
            int(input("Masukkan harga barang: "))
        ))
        if (input("Apakah ingin menambahkan barang lagi? [Y/N]: ").lower() == "n"):
            break


while True:
    # Menu
    print("=================")
    print("Selamat datang di program manajemen mall, silahkan pilih menu: "
          "\n1.Cek Daftar Toko"
          "\n2.Cek Salah Satu Toko"
          "\n3.Tambah Toko"
          "\n4.Kurangi Toko"
          "\n5.Cek Barang Salah Satu Toko"
          "\n6.Tambah Barang di Salah Satu Toko"
          "\n7.Kurangi Barang di Salah Satu Toko"
          "\n8.Keluar"
          "\nMasukkan pilihan berupa angka: ")
    pilihan = int(input())
    print("=================")

    if pilihan == 1:
        cekSemuaToko()
    elif pilihan == 2:
        cekToko(int(input("Masukkan index Toko: ")))
    elif pilihan == 3:
        tambahToko(Toko(
            input("Masukkan nama toko: "),
            int(input("Masukkan jumlah karyawan: ")),
            int(input("Jam buka toko: ")),
            int(input("Jam tutup toko: ")),
            buatDaftarBarang()
        ))
    elif pilihan == 4:
        kurangiToko(int(input("Masukkan index toko yang ingin dihapus: ")))
    elif pilihan == 5:
        cekBarangToko(int(input("Masukkan index toko yang ingin dilihat daftar barangnya: ")))
    elif pilihan == 6:
        tambahkanBarangToko(
            int(input("Masukkan index toko yang ingin ditambah barangnya: ")),
            Barang(
                input("Masukkan nama Barang: "),
                int(input("Masukkan harga barang: "))
            )
        )
    elif pilihan == 7:
        kurangiBarangToko(
            int(input("Masukkan index toko yang ingin dikurangi barangnya: ")),
            int(input("Masukkan index barang yang ingin dikurangi: ")),
        )
    elif pilihan == 8:
        break
    else:
        print("Maaf inputan salah")





