
# ### Soal Nomer 1
# class Battle:
#
#     def __init__(self, kill, dead, assist):
#         self.bunuh = kill
#         self.mati = dead
#         self.bantuan = assist
#
#
#
#     def cek(self):
#         kda = self.bunuh+(self.bantuan)-(self.mati * 0.75)
#         if(kda > 10):
#             rank = "GOLD"
#         elif(kda <= 10 and kda >= 6):
#             rank = "SILVER"
#         else:
#             rank = "BRONZE"
#
#         return rank
#
# k1 = int(input("Masukkan jumlah kill player pertama = "))
# D1 = int(input("Masukkan jumlah Dead player pertama = "))
# A1 = int(input("Masukkan jumlah Asist player pertama = "))
# hero1 = Battle(k1,D1,A1)
# k2 = int(input("Masukkan jumlah kill player Kedua = "))
# D2 = int(input("Masukkan jumlah Dead player Kedua = "))
# A2 = int(input("Masukkan jumlah Asist player Kedua = "))
# hero2 = Battle(k2,D2,A2)
# k3 = int(input("Masukkan jumlah kill player Ketiga = "))
# D3 = int(input("Masukkan jumlah Dead player Ketiga = "))
# A3 = int(input("Masukkan jumlah Asist player Ketiga = "))
# hero3 = Battle(k3,D3,A3)
#
# print(hero1.cek())
# print(hero2.cek())
# print(hero3.cek())


# ### Soal Nomer 2
# import datetime
#
# class Perpus:
#     def __init__(self, id, title, date):
#         self.id = id
#         self.judul = title
#         self.tanggal = date
#
#     def cek(self):
#         tahun, bulan, hari = map(int, self.tanggal.split("-"))
#         tanggalpinjam = datetime.date(tahun, bulan, hari)
#         today = datetime.date.today()
#         selisih = tanggalpinjam - today
#         print('selisih hari: ' + str(selisih.days))
#         if (selisih.days < -3):
#             dendakedua = 2000 * (selisih.days + 3) * -1
#         else:
#             dendakedua = 0
#
#         return dendakedua
#
#
# idbuku1 = input("Masukkan ID buku pertama = ")
# judul1 = input("Masukkan Judul buku pertama = ")
# tanggal1 = input("Masukkan tanggal peminjaman buku pertama dengan format YYYY-MM-DD = ")
# buku1 = Perpus(idbuku1, judul1, tanggal1)
# idbuku2 = input("Masukkan ID buku ke 2 = ")
# judul2 = input("Masukkan Judul buku ke 2 = ")
# tanggal2 = input("Masukkan tanggal peminjaman buku ke 2 dengan format YYYY-MM-DD = ")
# buku2 = Perpus(idbuku2, judul2, tanggal2)
# idbuku3 = input("Masukkan ID buku ke 3 = ")
# judul3 = input("Masukkan Judul buku ke 3 = ")
# tanggal3 = input("Masukkan tanggal peminjaman buku ke 3 dengan format YYYY-MM-DD = ")
# buku3 = Perpus(idbuku3, judul3, tanggal3)
#
# print(buku1.cek())
# print(buku2.cek())
# print(buku3.cek())

# ### Soal Nomer 3
#
# class Gaji:
#     uangTransportPerhari = 50000
#     uangMakanPerhari = 50000
#     jumlahkaryawan = 0
#
#     def __init__(self, salary, allowance, present):
#         self.gaji = salary
#         self.tunjangan = allowance
#         self.kehadiran = present
#
#
#
#     def cek(self):
#         Gaji.jumlahkaryawan += 1
#         totalUangTransport = Gaji.uangTransportPerhari * self.kehadiran
#         totalUangMakan = Gaji.uangMakanPerhari * self.kehadiran
#         gajiKaryawan = self.gaji + self.tunjangan + totalUangTransport + totalUangMakan
#         return " Gaji Karyawan {} \n - Gaji pokok : {} \n - Tunjangan : {} \n - Transport : {} \n - Makan : {} \n Total = Rp {}".format(self.jumlahkaryawan, self.gaji, self.tunjangan, totalUangTransport, totalUangMakan, gajiKaryawan)
#
#
#
# karyawan1 = Gaji(2500000, 1000000, 20)
# karyawan2 = Gaji(2750000, 1100000, 22)
# karyawan3 = Gaji(2000000, 0, 25)
# karyawan4 = Gaji(3000000, 1250000, 18)
#
# print(karyawan1.cek())
# print(karyawan2.cek())
# print(karyawan3.cek())
# print(karyawan4.cek())


### Soal Nomer 5

class Daftar:
    flashdisk_32_GB = 80000
    flashdisk_64_GB = 150000
    hardisk_1_TB = 1000000
    UPS_1000W = 500000
    CPU_desktop = 5000000

    jumalah = 5

    def __init__(self, shop,jml, shop1,jml1, shop2,jml2, shop3=0,jml3=0, shop4 = 0,jml4=0):
        self.belanja = shop
        self.jumlah = jml
        self.belanja1 = shop1
        self.jumlah1 = jml1
        self.belanja2 = shop2
        self.jumlah2 = jml2
        self.belanja3 = shop3
        self.jumlah3 = jml3
        self.belanja4 = shop4
        self.jumlah4 = jml4

    def cek(self):
        total = self.belanja * self.jumlah + self.belanja1 * self.jumlah1 + self.belanja2 * self.jumlah2 + self.belanja3 * self.jumlah3 + self.belanja4 * self.jumlah4
        if(total < 500000):
            print("masuk 1")
            total1 = total
        elif(total >= 500000 and total < 1500000):
            print("masuk 2")
            total1 = total / 1 * 100
        elif (total >= 1500000 and total < 5000000):
            print("masuk 3")
            total1 = total / 0.004
        else:
            print("masuk 4")
            total1 = total / 10 * 100
        return total1

barang1 = Daftar(Daftar.flashdisk_32_GB,5,Daftar.flashdisk_64_GB,4,Daftar.hardisk_1_TB,1)
barang2 = Daftar(Daftar.flashdisk_32_GB,1,Daftar.flashdisk_64_GB,1,Daftar.hardisk_1_TB,1,Daftar.UPS_1000W,1,Daftar.CPU_desktop,1)

print(barang1.cek())